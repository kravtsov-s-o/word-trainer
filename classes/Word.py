from classes.fields.Term import Term
from classes.fields.Translation import Translation
from classes.fields.Examples import Example
from datetime import datetime


class Word:
    def __init__(self,
                 term: Term,
                 translation: Translation,
                 example: Example,
                 repeat_count: int = 0,
                 repeat_after: int = 0,
                 repeat_date: datetime = datetime.now().date()):
        self.term = Term(term)
        self.translation = Translation(translation)
        self.example = Example(example)
        self.repeat_count = repeat_count
        self.repeat_after = repeat_after
        self.repeat_date = repeat_date

    def __str__(self):
        return (f"{'Word:':<15} {self.term.value}\n"
                f"{'Translations:':<15} {self.translation.value}\n"
                f"{'Examples:':<15} {self.example.value}"
                # f"{'Repeat:':<20} Correct answers {self.repeat_count}\n"
                # f"{'Next repeat after:':<20} {self.repeat_after} days\n"
                # f"{'Next repeat date:':<20} {self.repeat_date}"
                )

    # Edit Term
    def edit_term(self, value):
        self.term = Term(value)

    # Edit Translations
    def edit_translations(self, value):
        self.translation = Translation(value)

    # Edit example
    def edit_example(self, value):
        self.example = Example(value)

    # Edit example
    def edit_repeat_count(self, value):
        self.repeat_count = value

    # Edit example
    def edit_repeat_after(self, value):
        self.repeat_after = value

    # Edit example
    def edit_repeat_date(self, value):
        self.repeat_date = value

    # To dictionary method for saving to JSON BACKUP file
    def to_dict(self) -> dict:
        return {
            "word": str(self.term.value),
            "translations": str(self.translation.value),
            "example": str(self.example.value),
            "repeat_count": self.repeat_count,
            "repeat_after": self.repeat_after,
            "repeat_date": self.repeat_date.strftime("%Y-%m-%d"),
        }

    # From dictionary method for loading from JSON BACKUP file
    @classmethod
    def from_dict(cls, word_dict: dict):
        return cls(Term(word_dict["word"]),
                   Translation(word_dict["translations"]),
                   Example(word_dict["example"]),
                   word_dict["repeat_count"],
                   word_dict["repeat_after"],
                   datetime.strptime(word_dict["repeat_date"], "%Y-%m-%d"))
