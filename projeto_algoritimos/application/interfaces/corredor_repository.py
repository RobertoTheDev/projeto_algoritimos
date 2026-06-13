from abc import ABC, abstractmethod


class CorredorRepository(ABC):

    @abstractmethod
    def salvar(self, corredor):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def remover(self, nome):
        pass