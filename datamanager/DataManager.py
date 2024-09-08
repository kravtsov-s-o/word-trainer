from abc import ABC, abstractmethod


class DataManager(ABC):
    @abstractmethod
    def check(self):
        pass

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def add_few(self):
        pass

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def show_all(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def run(self):
        pass