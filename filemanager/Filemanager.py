from classes.Word import Word


class Filemanager:
    @staticmethod
    def load_dictionary(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                dictionary_str = file.read()

                word_dicts = eval(dictionary_str)
                if not isinstance(word_dicts, list):
                    word_dicts = list()

                words = [Word.from_dict(word_dict) for word_dict in word_dicts]
        except (FileNotFoundError, SyntaxError, ValueError):
            words = list()
        return words

    @staticmethod
    def save_dictionary(dictionary, file_path):
        word_dicts = [word.to_dict() for word in dictionary]
        with open(file_path, 'w', encoding='utf-8') as file:
            dictionary_str = repr(word_dicts)
            file.write(dictionary_str)

    @staticmethod
    def new_words_from_file(file_path: str):
        pass
