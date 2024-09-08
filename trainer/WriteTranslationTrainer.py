import random
from datetime import datetime, timedelta

from classes.Dictionary import Dictionary
from trainer.Trainer import Trainer
from ui.UIManager import UIManager


class WriteTranslationTrainer(Trainer):
    def __init__(self, ui_manager: UIManager, dictionary: Dictionary):
        self.ui_manager = ui_manager
        self.dictionary = dictionary

    def _get_today_date(self):
        return datetime.today().date()

    def _update_word(self, random_word):
        today = self._get_today_date()
        random_word.repeat_after += 1
        time_delta = self._get_time_delta(random_word.repeat_after)
        random_word.repeat_count = 0
        random_word.repeat_after = time_delta
        random_word.repeat_date = today + timedelta(days=time_delta)

    def _update_dictionary(self, selected_words, random_word):
        index = self.dictionary.dictionary.index(random_word)
        self.dictionary.dictionary[index] = random_word
        self.dictionary.save_dictionary()
        selected_words.remove(random_word)

    def _get_time_delta(self, delta: int):
        if delta <= 1:
            return 1
        elif delta <= 3:
            return 3
        elif delta <= 5:
            return 5
        elif delta <= 7:
            return 7
        elif delta <= 14:
            return 14
        elif delta <= 30:
            return 30
        else:
            return 30

    def _prepare_words_list(self, count_words):
        today = self._get_today_date()

        selected_words = [word for word in self.dictionary.dictionary if word.repeat_date.date() == today]

        if len(self.dictionary.dictionary) > len(selected_words):
            if len(selected_words) < count_words:
                past_words = [word for word in self.dictionary.dictionary if word.repeat_date.date() < today]
                selected_words.extend(past_words)

            if len(selected_words) < count_words:
                future_days = 1
                while len(selected_words) < count_words and future_days <= 31:
                    future_words = [word for word in self.dictionary.dictionary if
                                    word.repeat_date.date() == today + timedelta(days=future_days)]
                    selected_words.extend(future_words)
                    future_days += 1

        return selected_words[:count_words]

    def learn_words(self, selected_words):
        while len(selected_words) > 0:
            self.ui_manager.clear_console()
            random_word = random.choice(selected_words)
            self.ui_manager.show_message(self.ui_manager.get_divider(30))
            self.ui_manager.show_message(random_word.term.value)
            self.ui_manager.show_message(self.ui_manager.get_divider(30))
            self.ui_manager.show_message("If you know this word, write '+'")
            user_input = self.ui_manager.get_user_input("Write translation")

            if user_input.lower() == 'q' or len(selected_words) == 0:
                if len(selected_words) == 0:
                    self.ui_manager.show_message('You learned all words for today!')
                self.ui_manager.wait_to_continue()
                self.dictionary.save_dictionary()
                break

            if user_input == '+':
                self._update_word(random_word)
                self._update_dictionary(selected_words, random_word)
                continue

            # if user_input.lower() in str(random_word.translation.value).split(','):
            if user_input.lower() in [part.strip().lower() for part in str(random_word.translation.value).split(',')]:
                if random_word.repeat_count < 3:
                    random_word.repeat_count += 1
                    self.ui_manager.show_message(self.ui_manager.get_divider(30))
                    self.ui_manager.show_message('Correct!')
                    self.ui_manager.wait_to_continue()
                else:
                    self._update_word(random_word)
                    self._update_dictionary(selected_words, random_word)
            else:
                self.ui_manager.show_message(self.ui_manager.get_divider(30))
                self.ui_manager.show_message(f'Oops, wrong answer!\nRight answer(s): {random_word.translation.value}')
                self.ui_manager.wait_to_continue()

    def run(self, count_words):
        selected_words = self._prepare_words_list(count_words)
        self.learn_words(selected_words)
