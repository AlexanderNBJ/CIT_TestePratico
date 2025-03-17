from Componentes.Concretes.ConcetorBD import Conector
from Componentes.Concretes.Interface import Menu
from Componentes.Concretes.Controller import Controller
from Componentes.Abstracts.ConectorAbstract import ConectorAbstract
from Componentes.Abstracts.InterfaceAbstract import InterfaceAbstract
from Componentes.Abstracts.ControllerAbstract import ControllerAbstract

class Aplicacao:
    def __init__(self, conector: ConectorAbstract, interface: InterfaceAbstract, controller: ControllerAbstract):
        self.conector = conector
        self.interface = interface
        self.controller = controller
        return

    def iniciar(self):
        self.controller.processar()
        return

def main():

    conexao = Conector("sistema_escavacao_alexander",
                                "postgres",
                                "admin123",
                                "localhost",
                                "5432")
    
    if conexao.connector == None:
        print("Erro ao se conectar ao banco de dados.")
        return
    
    interface = Menu()

    aplicacao = Aplicacao(conexao, interface, Controller(interface, conexao))
    aplicacao.iniciar()
    return


if(__name__ == "__main__"):
    main()