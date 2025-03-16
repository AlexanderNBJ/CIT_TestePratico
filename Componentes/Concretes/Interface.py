from Abstracts import InterfaceAbstract

class Menu(InterfaceAbstract):
    def exibirMenuPrincipal():
        print("------ Menu Principal:")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Remover")
        print("5 - Encerrar progama\n")
        print("Digite uma operação...", end=" ")
        return

    def exibirMenuCadastro():
        print("------ Menu de Cadastro:")
        print("1 - Cadastrar Ponto de Escavação")
        print("2 - Cadastrar Pesquisador")
        print("3 - Cadastrar Tipo de Ponto")
        print("4 - Retornar\n")
        print("Digite uma operação...", end=" ")
        return
    
    def exibirMenuListar():
        print("------ Menu de Listagem:")
        print("1 - Listar Ponto de Escavação")
        print("2 - Listar Pesquisador")
        print("3 - Listar Tipo de Ponto")
        print("4 - Retornar\n")
        print("Digite uma operação...", end=" ")
        return
    
    def exibirMenuAtualizar():
        print("------ Menu de Atualização de Cadastro:")
        print("1 - Atualizar Ponto de Escavação")
        print("2 - Atualizar Pesquisador")
        print("3 - Atualizar Tipo de Ponto")
        print("4 - Retornar\n")
        print("Digite uma operação...", end=" ")
        return
    
    def exibirMenuAtualizar():
        print("------ Menu de Exclusão de Cadastro:")
        print("1 - Excluir Ponto de Escavação")
        print("2 - Excluir Pesquisador")
        print("3 - Excluir Tipo de Ponto")
        print("4 - Retornar\n")
        print("Digite uma operação...", end=" ")
        return
    
    def exibirTitulo():
        print("\n\t\t\tSistema de Catálogo de Pontos de Escavação\n")
        return

    def exibirMenuFiltrar():
        print("Selecione um critério de filtragem:")
        return