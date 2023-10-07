from classes.Filenamager import Filemanager
from classes.Word import Word
import random


class Dictionary:
    def __init__(self, file_dictionary: str, stop_list: list) -> None:
        self.file_dictionary = file_dictionary
        self.words = Filemanager.load_dictionary(self.file_dictionary)
        self.stop_list = stop_list

    def save_dictionary(self):
        Filemanager.save_dictionary(self.words, self.file_dictionary)

    def check_word(self) -> None:
        while True:
            word = input('Проверить: ').lower()
            if word in self.stop_list:
                break

            found_word = next((word_obj for word_obj in self.words if word_obj.word == word), None)

            if found_word:
                print(f'{"Слово":<10}: {found_word.word}')
                print(f'{"Перевод":<10}: {", ".join(found_word.translations)}')
                print(f'{"Категории":<10}: {", ".join(found_word.categories)}\n_________')
            else:
                print(f'Слово "{word}" в словаре не найдено')

    def _save_new_word(self, word):
        try:
            word = word.split(';')
            if len(word) != 3:
                raise ValueError('Неверный формат данных!\n(Пример: cat;кот,кошка;animal)')

            new_word = Word(word[0], word[1].split(','), word[2].split(','))

            if new_word not in self.words:
                self.words.append(new_word)
                print(f'Слово "{word[0]}" успешно сохранено в словарь')
                self.save_dictionary()
            else:
                print(f'Слово "{word[0]}" уже в словаре')
        except ValueError as e:
            print(f'Ошибка: {e}')

    def add_word(self, word=None) -> None:
        if not word:
            while True:
                word = input('Добавить: ').lower()
                if word in self.stop_list:
                    break
                self._save_new_word(word)

    def add_few_words(self) -> None:
        file_with_words = input('Путь к файлу: ')

        with open(file_with_words, 'r', encoding='utf-8') as file:
            line = file.readline().strip()
            while line:
                self._save_new_word(line)
                line = file.readline().strip()

    # TODO new method Update word
    def delete_word(self) -> None:
        while True:
            word = input('Удалить: ').lower()
            if word in self.stop_list:
                break

            found_word = next((word_obj for word_obj in self.words if word_obj.word == word), None)

            if found_word:
                self.words.remove(found_word)
                print(f'Слово "{word}" успешно удалено из словаря')
                self.save_dictionary()
            else:
                print(f'Слово "{word}" в словаре не найдено')

    def drill_words(self) -> None:
        while True:
            random_word = random.choice(self.words)
            print(random_word.word)
            word = input('Перевод: ')

            if word in self.stop_list:
                break

            if word in random_word.translations:
                print('Поздравляю, правильный ответ!')
            else:
                print(f'Ответ неверный. Варианты ответов: {", ".join(random_word.translations)}')
