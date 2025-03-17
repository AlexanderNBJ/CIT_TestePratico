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
                self.interface.exibirMenuListar()
                #avaliar a listagem aqui
            elif(opcao == 3):
                self.interface.exibirMenuAtualizar()
                #avaliar a atualização de registros aqui
            elif(opcao == 4):
                self.interface.exibirMenuRemover()
                #avaliar a remoção de registros aqui
            elif(opcao == 5):
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
                pass
            elif(opcao == 3):
                pass
            elif(opcao == 4):
                return
            else:
                self.interface.exibirErroDeOpcaoInvalida()
                print("Ué")
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
