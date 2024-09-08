from classes.common.Field import Field


class Term(Field):
    MIN_LENGTH = 2

    def __init__(self, value):
        super().__init__(value)
        self.validate(value)

    def validate(self, value):
        word = str(value).strip()

        if not word:
            raise ValueError(f"Cannot be empty!")

        if len(word) < self.MIN_LENGTH:
            raise ValueError(f"Word must be at least {self.MIN_LENGTH} characters long!")
