from application.Application import Application
from datamanager.DataManager import DataManager
from trainer_manager.WriteTranslationManager import WriteTranslationManager
from ui.UIManager import UIManager


class ConsoleApplication(Application):
    MAIN_MENU = {
        'title': 'Commands list',
        'items': [
            f"{'dictionary':<10} - show dictionary",
            f"{'train':<10} - start learning words",
            f"{'q':<10} - end of program",
        ]
    }

    def __init__(self, ui_manager: UIManager, dictionary_manager: DataManager, trainer_manager: WriteTranslationManager):
        self.ui_manager = ui_manager
        self.dictionary_manager = dictionary_manager
        self.trainer_manager = trainer_manager

    def run(self):
        while True:
            self.ui_manager.clear_console()
            self.ui_manager.show_menu(self.MAIN_MENU)

            choice = self.ui_manager.get_user_input('Choose action')

            if choice == 'dictionary':
                self.dictionary_manager.run()
            elif choice == 'train':
                self.trainer_manager.run()
            elif choice == 'q':
                self.dictionary_manager.save()
                break
            else:
                self.ui_manager.show_message('Unknown command. Please try again.')
