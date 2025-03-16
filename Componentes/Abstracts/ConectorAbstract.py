from abc import ABC, abstractmethod

class ConectorAbstract(ABC):
    @abstractmethod
    def executarQueryDeSelecao(self, atributos: list[str], tabela: str, condicoes=""):
        pass
    
    @abstractmethod
    def executarQueryDeAtualizacao(self, atualizar: dict[str, str], tabela: str, condicoes=""):
        pass

    @abstractmethod
    def executarQueryDeDelecao(self, tabela: str, condicoes=""):
        pass
    
    @abstractmethod
    def executarQueryDeInsercao(self, atributos: list[str], tabela: str):
        pass

    @abstractmethod
    def executarQueryDeCommit(self):
        pass

    @abstractmethod
    def executarQueryDeRollback(self):
        pass

    @abstractmethod
    def encerrarConexao(self):
        pass