from abc import ABC, abstractmethod

class InterfaceAbstract(ABC):
    @abstractmethod
    def exibirMenuPrincipal():
        pass

    @abstractmethod
    def exibirMenuCadastro():
        pass
    
    @abstractmethod
    def exibirMenuListar():
        pass
    
    @abstractmethod
    def exibirMenuAtualizar():
        pass
    