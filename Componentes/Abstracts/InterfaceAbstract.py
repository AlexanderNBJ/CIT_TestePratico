from abc import ABC, abstractmethod

class InterfaceAbstract(ABC):
    @abstractmethod
    def exibirMenuPrincipal(self):
        pass

    @abstractmethod
    def exibirMenuCadastro(self):
        pass
    
    @abstractmethod
    def exibirMenuListar(self):
        pass
    
    @abstractmethod
    def exibirMenuAtualizar(self):
        pass

    @abstractmethod
    def exibirMenuRemover(self):
        pass

    @abstractmethod
    def exibirCadastroDePontoDeEscavacao(self):
        pass

    @abstractmethod
    def exibirCadastroDeTipoDePonto(self):
        pass

    @abstractmethod
    def exibirCadastroDePesquisador(self):
        pass

    @abstractmethod
    def exibirListagemDePontoDeEscavacao(self):
        pass

    @abstractmethod
    def exibirListagemDePesquisador(self):
        pass

    @abstractmethod
    def exibirListagemDeTipoDePonto(self):
        pass

    @abstractmethod
    def exibirListagemDePontoDeEscavacaoTipoDePonto(self):
        pass
    
    @abstractmethod
    def exibirListagemDePontoDeEscavacaoPesquisador(self):
        pass

    @abstractmethod
    def exibirListagemDePontoDeEscavacaoTipoDePontoPesquisador(self):
        pass

    @abstractmethod
    def exibirAtualizacaoDePontoDeEscavacao(self):
        pass

    @abstractmethod
    def exibirAtualizacaoDePesquisador(self):
        pass

    @abstractmethod
    def exibirAtualizacaoDeTipoDePonto(self):
        pass

    @abstractmethod
    def exibirExclusaoDePontoDeEscavacao(self):
        pass

    @abstractmethod
    def exibirExclusaoDePesquisador(self):
        pass

    @abstractmethod
    def exibirExclusaoDeTipoDePonto(self):
        pass

    @abstractmethod
    def exibirTitulo(self):
        pass
    
    @abstractmethod
    def exibirErroDeOpcaoInvalida(self):
        pass

    @abstractmethod
    def exibirErroDeInsercao(self):
        pass

    @abstractmethod
    def exibirErroDeAlteracao(self):
        pass

    @abstractmethod
    def exibirErroDeExclusao(self):
        pass

    @abstractmethod
    def exibirErroDeListagem(self):
        pass

    @abstractmethod
    def exibirResultado(self, resultado):
        pass

    @abstractmethod
    def exibirSucessoInsercao(self, numero: int):
        pass

    @abstractmethod
    def exibirSucessoAtualizacao(self, numero: int):
        pass

    @abstractmethod
    def exibirSucessoExclusao(self, numero: int):
        pass

    @abstractmethod
    def exibirMensagemCommit(self, adds: int, alts: int, excls: int):
        pass
    
    @abstractmethod
    def exibirMensagemRollback(self, adds: int, alts: int, excls: int):
        pass

    @abstractmethod
    def encerrarInterface(self):
        pass

