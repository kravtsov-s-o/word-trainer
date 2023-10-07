class Word:
    def __init__(self, word: str, translations: list, categories: list) -> None:
        self.word = word
        self.translations = translations
        self.categories = categories

    def __str__(self) -> str:
        return (f'Word: {self.word},'
                f'Translations: {", ".join(self.translations)},'
                f'Categories: {", ".join(self.categories)}')

    def to_dict(self) -> dict:
        return {
            "word": self.word,
            "translations": self.translations,
            "categories": self.categories,
        }

    @classmethod
    def from_dict(cls, word_dict: dict):
        return cls(word_dict["word"], word_dict["translations"], word_dict["categories"])
