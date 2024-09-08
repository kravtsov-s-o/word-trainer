from trainer.WriteTranslationTrainer import WriteTranslationTrainer


class WriteTranslationManager:
    # Words limit
    DEFAULT = 20
    MIN = 1
    MAX = 50

    def __init__(self, word_trainer):
        self.word_trainer = word_trainer

    def user_setup(self):
        while True:
            self.word_trainer.ui_manager.show_message(f'Only numbers. You can stay it empty!\n'
                                                      f'Default: {self.DEFAULT}; Min: {self.MIN}; Max: {self.MAX};')
            count_words = self.word_trainer.ui_manager.get_user_input('How many words learn? (default=20)')

            if count_words == '' or count_words == 'q':
                count_words = self.DEFAULT
                break
            else:
                try:
                    count_words = int(count_words)
                    if self.MIN < count_words > self.MAX:
                        self.word_trainer.ui_manager.show_message(f'Invalid input. Please enter a number between '
                                                                  f'{self.MIN} and {self.MAX}.')
                        continue
                    break
                except ValueError:
                    self.word_trainer.ui_manager.show_message('Invalid input. Please enter a number.')
                    continue

        return count_words

    def run(self):
        count_words = self.user_setup()
        self.word_trainer.ui_manager.clear_console()
        self.word_trainer.run(count_words)
