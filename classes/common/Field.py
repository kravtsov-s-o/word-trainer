from abc import ABC


class Field(ABC):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self.validate(new_value)
        self._value = new_value

    def validate(self, value):
        pass
