from classes.common.Field import Field


class Example(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate(value)

    def validate(self, value):
        return str(value).strip()