from classes.common.Field import Field


class Translation(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate(value)

    def validate(self, value):
        phrase = str(value).strip()

        if not phrase:
            raise ValueError(f"Cannot be empty!")