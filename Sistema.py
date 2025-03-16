import os
from Componentes.Concretes.ConcetorBD import Conector
from Componentes.Concretes.Interface import Menu
from Componentes.Abstracts.ConectorAbstract import ConectorAbstract
from Componentes.Abstracts.InterfaceAbstract import InterfaceAbstract

class Aplicacao:
    def __init__(self, conector: ConectorAbstract, interface: InterfaceAbstract):
        self.emExecucao = True
        self.conector = conector
        self.interface = interface
        pass

    def iniciar(self):
        self.interface.exibirTitulo()

        while(self.emExecucao):
            self.interface.exibirMenuPrincipal()

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
    
    Aplicacao = Aplicacao(conexao, Menu())


if(__name__ == "__main__"):
    main()