from ..Abstracts.ControllerAbstract import ControllerAbstract
from ..Abstracts.ConectorAbstract import ConectorAbstract
from ..Abstracts.InterfaceAbstract import InterfaceAbstract

class Controller(ControllerAbstract):
    def __init__(self, interface: InterfaceAbstract, conector: ConectorAbstract):
        self.interface = interface
        self.conector = conector
        self.emExecucao = True
        return
    
    def processar(self):
        while(self.emExecucao):
            opcao = self.interface.exibirMenuPrincipal()
            self.avaliaOpcaoMenuPrincipal(opcao)
        return

    def avaliaOpcaoMenuPrincipal(self, opcao):
        try:
            opcao = int(opcao)
            if(opcao == 1):
                opcao = self.interface.exibirMenuCadastro()
                self.avaliaOpcaoCadastro(opcao)
            elif(opcao == 2):
                opcao = self.interface.exibirMenuListar()
                self.avaliaOpcaoListar(opcao)
            elif(opcao == 3):
                self.interface.exibirMenuAtualizar()
                #avaliar a atualização de registros aqui
            elif(opcao == 4):
                self.interface.exibirMenuRemover()
                #avaliar a remoção de registros aqui
            elif(opcao == 0):
                self.conector.executarQueryDeCommit()
                self.emExecucao = False
                return
            else:
                self.interface.exibirErroDeOpcaoInvalida()
                return
        except Exception as e:
            self.interface.exibirErroDeOpcaoInvalida()
        return
        
    def avaliaOpcaoCadastro(self, opcao):
        try:
            opcao = int(opcao)

            if(opcao == 1):
                array = self.interface.exibirCadastroDePontoDeEscavacao()
                self.inserePontoDeEscavacao(array)
            elif(opcao == 2):
                array = self.interface.exibirCadastroDePesquisador()
                self.inserePesquisador(array)
            elif(opcao == 3):
                array = self.interface.exibirCadastroDeTipoDePonto()
                self.insereTipoDePonto(array)
            elif(opcao == 0):
                return
            else:
                self.interface.exibirErroDeOpcaoInvalida()
        except Exception as e:
            self.interface.exibirErroDeOpcaoInvalida()
            
        return
    
    def inserePontoDeEscavacao(self, arrayValores):
        arrayColunas = ["TIPO_DE_PONTO_ID", 
                        "PESQUISADOR_RESPONSAVEL_ID", 
                        "LATITUDE", 
                        "LONGITUDE", 
                        "ALTITUDE", 
                        "DATA_DE_DESCOBERTA", 
                        "DESCRICAO"]
        
        for atributo in arrayValores:
            if atributo == "":
                atributo = "NULL"
        try:
            result = self.conector.executarQueryDeInsercao(arrayValores, arrayColunas, "PONTO_DE_ESCAVACAO")
            self.interface.exibirSucessoInsercao(result)
        except Exception as e:
            self.interface.exibirErroDeInsercao()
            print(e)
    
    def inserePesquisador(self, arrayValores):
        arrayColunas = ["NOME_COMPLETO", "TELEFONE", "EMAIL", "ESPECIALIDADE"]
        
        for atributo in arrayValores:
            if atributo == "":
                atributo = "NULL"
        try:
            result = self.conector.executarQueryDeInsercao(arrayValores, arrayColunas, "PESQUISADOR")
            self.interface.exibirSucessoInsercao(result)
        except Exception as e:
            self.interface.exibirErroDeInsercao(e)
    
    def insereTipoDePonto(self, arrayValores):
        arrayColunas = ["DESCRICAO"]
        
        for atributo in arrayValores:
            if atributo == "":
                atributo = "NULL"
        try:
            result = self.conector.executarQueryDeInsercao(arrayValores, arrayColunas, "TIPO_DE_PONTO")
            self.interface.exibirSucessoInsercao(result)
        except Exception as e:
            self.interface.exibirErroDeInsercao(e)
    
    def avaliaOpcaoListar(self, opcao):
        try:
            opcao = int(opcao)
            if(opcao == 1):
                arrayFiltro, arrayOrdem = self.interface.exibirListagemDePontoDeEscavacao()
                resultado = self.buscaPontoDeEscavacao(arrayFiltro, arrayOrdem)
                if resultado != None:
                    nomesColunas = self.conector.obterNomesDasColunas()
                    self.interface.exibirResultado(resultado, nomesColunas)
            elif(opcao == 2):
                #listar pesquisadores
                pass
            elif(opcao == 3):
                #listar tipos de ponto
                pass
            elif(opcao == 0):
                return
            else:
                self.interface.exibirErroDeOpcaoInvalida()
                return
        except Exception as e:
            self.interface.exibirErroDeOpcaoInvalida(e)
            
        return

    def buscaPontoDeEscavacao(self, arrayFiltro, arrayOrdem):
        condicao = ""
        if(arrayFiltro):
            condicao = "WHERE "+" AND ".join(arrayFiltro)
        if(arrayOrdem):
            condicao += " ORDER BY " +", ".join(arrayOrdem)
        try:
            resultado = self.conector.executarQueryDeSelecao(['*'],'PONTO_DE_ESCAVACAO', condicao)
            return resultado
        except Exception as e:
            self.interface.exibirErroDeListagem(e)
            return None
        