from classes.Dictionary import Dictionary
from datamanager.DataManager import DataManager
from helpers.Paginator import Paginator
from ui.UIManager import UIManager


class DictionaryManager(DataManager):
    MAIN_MENU = {
        'title': 'Dictionary Menu',
        'items': [
            f"{'view':<10} - show dictionary",
            f"{'check':<10} - check word in your dictionary",
            f"{'add':<10} - new word",
            f"{'add_few':<10} - add list of new words from file",
            f"{'edit':<10} - edit word record in dictionary",
            f"{'delete':<10} - delete word from dictionary",
            f"{'save':<10} - make backup for dictionary",
            f"{'q':<10} - end of program",
        ]
    }
    
    def __init__(self, dictionary: Dictionary, ui_manager: UIManager, items_per_page: int = 20):
        self.dictionary = dictionary
        self.ui_manager = ui_manager
        self.items_per_page = items_per_page

    def check(self):
        self.ui_manager.clear_console()
        choose_word = self.ui_manager.get_user_input("Search word in dictionary")

        self.ui_manager.message(self.dictionary.check_word(choose_word))
        self.ui_manager.wait_to_continue()

    def add(self):
        self.ui_manager.clear_console()
        while True:
            self.ui_manager.show_message("Phrase like: word;translation1,translation2;Example1,Example2")
            self.ui_manager.show_message("q - for exit")
            new_word = self.ui_manager.get_user_input('Write new word')

            if new_word == "q":
                break

            self.dictionary.add_word(new_word)

    def add_few(self):
        file_path = self.ui_manager.get_user_input("Enter the file path")
        self.ui_manager.show_message(self.dictionary.add_few_words(file_path))
        self.ui_manager.wait_to_continue()

    def edit(self):
        self.ui_manager.clear_console()
        while True:
            user_input = self.ui_manager.get_user_input("Enter the word to edit")
            word = self.dictionary.find_word(user_input)
            if word == 'q':
                break
            if not word:
                self.ui_manager.show_message(f"Word {user_input} did not find")
            else:
                print(word)
                break

        self.ui_manager.show_message("Phrase like: word;translation1,translation2;Example1,Example2")
        edit_word = self.ui_manager.get_user_input("Enter update:")
        self.ui_manager.show_message(self.dictionary.edit_word(word, edit_word))

        self.ui_manager.wait_to_continue()

    def delete(self):
        self.ui_manager.clear_console()
        word = self.ui_manager.get_user_input("Enter the word to delete")
        self.ui_manager.show_message(self.dictionary.delete(word))
        self.ui_manager.wait_to_continue()

    def save(self):
        self.ui_manager.show_message(self.dictionary.save_dictionary())

    def show_all(self):
        self.ui_manager.clear_console()

        if len(self.dictionary.dictionary) > 0:
            items = Paginator(self.dictionary.dictionary, self.items_per_page)
            self.ui_manager.show_items(items)
        else:
            self.ui_manager.show_message('Dictionary is empty...')

        self.ui_manager.wait_to_continue()

    def run(self):
        while True:
            self.ui_manager.clear_console()
            self.ui_manager.show_menu(self.MAIN_MENU)

            choice = self.ui_manager.get_user_input('Choose action')

            if choice == 'view':
                self.show_all()
            elif choice == 'check':
                self.check()
            elif choice == 'add':
                self.add()
            elif choice == 'add_few':
                self.add_few()
            elif choice == 'edit':
                self.edit()
            elif choice == 'delete':
                self.delete()
            elif choice == 'save':
                self.save()
                self.ui_manager.wait_to_continue()
            elif choice == 'q':
                self.save()
                break
            else:
                self.ui_manager.show_message('Unknown command. Please try again.')
                