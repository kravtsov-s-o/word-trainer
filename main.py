from classes.Dictionary import Dictionary
from constants import WORDS_DICTIONARY
from constants import STOP_LIST

class App:
    def __init__(self, dictionary_file: str, stop_list: list):
        self.dictionary = Dictionary(dictionary_file, stop_list)
        self.stop_list = stop_list

    def show_commands_list(self):
        """
        Show commands list
        :return: nothing
        """
        print("Список доступных команд:\n"
              "add / добавить - добавить слово в словарь\n"
              "delete / удалить - удалить слово из словаря\n"
              "check / проверить - если хотите проверить наличие слова в словаре\n"
              "drill / учить - начать тренировку\n"
              "help / помощь - список команд\n"
              "exit / stop / стоп - завершение скрипта\n")


    def start(self):

        while True:
            command = input('С чего начнет? ').lower()

            if command == 'check':
                self.dictionary.check_word()

            if command == 'add':
                note = ("*************\n"
                        "Слово, его переводы и категории разделяются ';'.\n"
                        "Переводы и категории ','\n"
                        "Пример: cat;кот,кошка;animal\n*************")
                print(note)
                self.dictionary.add_word()

            if command == 'add_few':
                self.dictionary.add_few_words()

            if command == 'delete':
                self.dictionary.delete_word()

            if command == 'drill':
                self.dictionary.drill_words()

            if command == 'help':
                self.show_commands_list()

            if command in self.stop_list:
                print('До следующей встречи')
                break


if __name__ == '__main__':
    app = App(WORDS_DICTIONARY, STOP_LIST)
    app.start()
