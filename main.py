import sys

from application.ConsoleApplication import ConsoleApplication
from classes.Dictionary import Dictionary
from datamanager.DictionaryManager import DictionaryManager
from trainer.WriteTranslationTrainer import WriteTranslationTrainer
from ui.ConsoleUIManager import ConsoleUIManager
from trainer_manager.WriteTranslationManager import WriteTranslationManager

sys.stdout.reconfigure(encoding='utf-8')

DICTIONARY_BACKUP = 'dictionary.json'
ITEMS_PER_PAGE = 20


def init():
    ui_manager = ConsoleUIManager()
    dictionary = Dictionary(DICTIONARY_BACKUP)
    dictionary_manager = DictionaryManager(dictionary, ui_manager, ITEMS_PER_PAGE)
    # Тренажер слов, нужно вводить перевод
    word_trainer = WriteTranslationTrainer(ui_manager, dictionary)
    trainer_manager = WriteTranslationManager(word_trainer)

    app = ConsoleApplication(ui_manager, dictionary_manager, trainer_manager)
    app.run()


if __name__ == "__main__":
    init()
