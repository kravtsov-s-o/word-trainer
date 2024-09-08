from abc import ABC, abstractmethod


class Trainer(ABC):
    @abstractmethod
    def _prepare_words_list(self):
        pass

    @abstractmethod
    def learn_words(self):
        pass

    @abstractmethod
    def run(self):
        pass
