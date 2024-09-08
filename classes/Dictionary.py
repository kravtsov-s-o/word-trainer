from classes.fields.Term import Term
from classes.fields.Translation import Translation
from classes.fields.Examples import Example
from classes.Word import Word
from filemanager.Filemanager import Filemanager


class Dictionary:
    def __init__(self, file_dictionary: str):
        self.file_dictionary = file_dictionary
        self.dictionary = Filemanager.load_dictionary(self.file_dictionary)

    # Save dictionary in file for save data
    def save_dictionary(self):
        Filemanager.save_dictionary(self.dictionary, self.file_dictionary)
        return "Dictionary was saved in file!"

    # find word in dictionary
    def find_word(self, word: str):
        return next((word_obj for word_obj in self.dictionary if str(word_obj.term).lower() == word.lower()), None)

    # Save word in dictionary
    def _save_word(self, user_input: str):
        try:
            word = [part.strip() for part in user_input.strip().split(';')]
            if len(word) != 3:
                raise ValueError("Invalid word format. Use 'term;translations;examples'")

            new_word = Word(Term(word[0]), Translation(word[1]), Example(word[2]))
            if new_word in self.dictionary:
                raise ValueError("Word already exists in the dictionary")

            self.dictionary.append(new_word)
            print(f"Word '{word[0]}' successfully saved!")

        except ValueError as e:
            print(f"Error: {e}")

    # Check word in dictionary list
    def check_word(self, word: str):
        founded_word = self.find_word(word)

        if not founded_word:
            return f"Word {word} is not in list of words"

        return founded_word

    # Save word in dictionary
    def add_word(self, word: str):
        self._save_word(word)

    # Add words from file
    def add_few_words(self, file_path: str):
        with open(file_path, 'r', encoding='utf-8') as file:
            line = file.readline().strip()
            while line:
                self._save_word(line)
                line = file.readline().strip()

    # Delete word
    def delete(self, word: str):
        word_to_delete = self.find_word(word)

        if not word_to_delete:
            return f"Word '{word}' not found in the dictionary"

        self.dictionary.remove(word_to_delete)
        return f'Word "{word}" was deleted!'

    def edit_word(self, word, new_word: str):
        new_word = [part.strip() for part in new_word.strip().split(';')]
        word.edit_term(new_word[0])
        word.edit_translations(new_word[1])
        word.edit_example(new_word[2])

        return word

    def show(self):
        for word in self.dictionary:
            print(word)
            print()
