from ..Abstracts.InterfaceAbstract import InterfaceAbstract
import os

class Menu(InterfaceAbstract):
    def exibirMenuPrincipal(self):
        os.system("clear")
        self.exibirTitulo()
        print("------ Menu Principal:")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Remover")
        print("5 - Encerrar progama\n")
        print("Digite uma operação...", end=" ")
        return input().strip()

    def exibirMenuCadastro(self):
        os.system("clear")
        print("------ Menu de Cadastro:")
        print("1 - Cadastrar Ponto de Escavação")
        print("2 - Cadastrar Pesquisador")
        print("3 - Cadastrar Tipo de Ponto")
        print("4 - Retornar\n")
        print("Digite uma operação...", end=" ")
        return input().strip()
    
    def exibirMenuListar(self):
        os.system("clear")
        print("------ Menu de Listagem:")
        print("1 - Listar Ponto de Escavação")
        print("2 - Listar Pesquisador")
        print("3 - Listar Tipo de Ponto")
        print("4 - Retornar\n")
        print("Digite uma operação...", end=" ")
        return input().strip()
    
    def exibirMenuAtualizar(self):
        os.system("clear")
        print("------ Menu de Atualização de Cadastro:")
        print("1 - Atualizar Ponto de Escavação")
        print("2 - Atualizar Pesquisador")
        print("3 - Atualizar Tipo de Ponto")
        print("4 - Retornar\n")
        print("Digite uma operação...", end=" ")
        return input().strip()
    
    def exibirMenuRemover(self):
        os.system("clear")
        print("------ Menu de Exclusão de Cadastro:")
        print("1 - Excluir Ponto de Escavação")
        print("2 - Excluir Pesquisador")
        print("3 - Excluir Tipo de Ponto")
        print("4 - Retornar\n")
        print("Digite uma operação...", end=" ")
        return input().strip()
    
    def exibirCadastroDePontoDeEscavacao(self):
        os.system("clear")
        array = []
        print("Digite o número do tipo de ponto:", end=" ")
        array.append(input().strip())
        print("Digite o ID do pesquisador responsável:", end=" ")
        array.append(input().strip())
        print("Digite a latitude ponto:", end=" ")
        array.append(input().strip())
        print("Digite a longitude do ponto:", end=" ")
        array.append(input().strip())
        print("Digite a altitude do ponto:", end=" ")
        array.append(input().strip())
        print("Digite a data de descoberta do ponto:", end=" ")
        array.append(input().strip())
        print("Digite uma descrição:")
        array.append(input().strip())
        return array

    def exibirCadastroDeTipoDePonto(self):
        os.system("clear")
        print("Digite uma descrição para o tipo de ponto:")
        return input().strip()
    
    def exibirCadastroDePesquisador(self):
        os.system("clear")
        array =[]
        print("Digite o nome completo do pesquisador:", end=" ")
        array.append(input().strip())
        print("Digite o telefone do pesquisador (sem parênteses ou traços):", end=" ")
        array.append(input().strip())
        print("Digite o email do pesquisador:", end=" ")
        array.append(input().strip())
        print("Digite a especialidade do pesquisador:", end=" ")
        array.append(input().strip())
        return array
    
    def exibirListagemDePontoDeEscavacao(self):
        os.system("clear")
        if(self.gostariaDeFiltrar()):
            arrayFiltro = self.opcoesFiltragemPontoDeEscavacao()

        if(self.gostariaDeOrdenar()):
            arrayOrdem = self.opcoesOrdenacaoPontosDeEscavacao()
        return arrayFiltro, arrayOrdem
    
    def exibirListagemDePesquisador(self):
        os.system("clear")
        if(self.gostariaDeFiltrar()):
            arrayFiltro = self.opcoesFiltragemPesquisadores()
        
        if(self.gostariaDeOrdenar()):
            arrayOrdem = self.opcoesOrdenacaoPesquisadores()
        return arrayFiltro, arrayOrdem
    
    def exibirListagemDeTipoDePonto(self):
        os.system("clear")
        if(self.gostariaDeFiltrar()):
            arrayFiltro = self.opcoesFiltragemTipoDePonto()
        
        if(self.gostariaDeOrdenar()):
            arrayOrdem = self.opcoesOrdenacaoTipoDePonto()
        return arrayFiltro, arrayOrdem

    def exibirAtualizacaoDePontoDeEscavacao(self):
        os.system("clear")
        print("Digite o ID do ponto de escavação que deseja atualizar:", end=" ")
        id_ponto = input().strip()
        
        print("Selecione os campos para atualizar (separados por vírgula):")
        print("1 - Tipo de Ponto")
        print("2 - Pesquisador Responsável")
        print("3 - Latitude")
        print("4 - Longitude")
        print("5 - Altitude")
        print("6 - Data de Descoberta")
        print("7 - Descrição")
        campos = input().split(',')
        
        atualizacoes = {}
        for campo in campos:
            campo = campo.strip()
            if campo == '1':
                print("Novo ID do Tipo de Ponto:", end=" ")
                atualizacoes['TIPO_DE_PONTO_ID'] = input().strip()
            elif campo == '2':
                print("Novo ID do Pesquisador Responsável:", end=" ")
                atualizacoes['PESQUISADOR_RESPONSAVEL_ID'] = input().strip()
            elif campo == '3':
                print("Nova Latitude:", end=" ")
                atualizacoes['LATITUDE'] = input().strip()
            elif campo == '4':
                print("Nova Longitude:", end=" ")
                atualizacoes['LONGITUDE'] = input().strip()
            elif campo == '5':
                print("Nova Altitude:", end=" ")
                atualizacoes['ALTITUDE'] = input().strip()
            elif campo == '6':
                print("Nova Data de Descoberta (YYYY-MM-DD):", end=" ")
                atualizacoes['DATA_DE_DESCOBERTA'] = input().strip()
            elif campo == '7':
                print("Nova Descrição:", end=" ")
                atualizacoes['DESCRICAO'] = input().strip()
        
        return id_ponto, atualizacoes

    def exibirAtualizacaoDePesquisador(self):
        os.system("clear")
        print("Digite o ID do pesquisador que deseja atualizar:", end=" ")
        id_pesquisador = input().strip()
        
        print("Selecione os campos para atualizar (separados por vírgula):")
        print("1 - Nome Completo")
        print("2 - Telefone")
        print("3 - Email")
        print("4 - Especialidade")
        campos = input().split(',')
        
        atualizacoes = {}
        for campo in campos:
            campo = campo.strip()
            if campo == '1':
                print("Novo Nome Completo:", end=" ")
                atualizacoes['NOME_COMPLETO'] = input().strip()
            elif campo == '2':
                print("Novo Telefone:", end=" ")
                atualizacoes['TELEFONE'] = input().strip()
            elif campo == '3':
                print("Novo Email:", end=" ")
                atualizacoes['EMAIL'] = input().strip()
            elif campo == '4':
                print("Nova Especialidade:", end=" ")
                atualizacoes['ESPECIALIDADE'] = input().strip()
        
        return id_pesquisador, atualizacoes

    def exibirAtualizacaoDeTipoDePonto(self):
        os.system("clear")
        print("Digite o ID do tipo de ponto que deseja atualizar:", end=" ")
        id_tipo = input().strip()
        print("Nova Descrição:", end=" ")
        nova_descricao = input().strip()
        return id_tipo, {'DESCRICAO': nova_descricao}

    def exibirExclusaoDePontoDeEscavacao(self):
        os.system("clear")
        print("Digite o ID do ponto de escavação que deseja excluir:", end=" ")
        return input().strip()

    def exibirExclusaoDePesquisador(self):
        os.system("clear")
        print("Digite o ID do pesquisador que deseja excluir:", end=" ")
        return input().strip()

    def exibirExclusaoDeTipoDePonto(self):
        os.system("clear")
        print("Digite o ID do tipo de ponto que deseja excluir:", end=" ")
        return input().strip()

    def exibirResultado(self, resultado):
        os.system("clear")
        print("\nResultado da operação:")
        if isinstance(resultado, list):
            for item in resultado:
                print(item)
        else:
            print(resultado)
        print("\nPressione Enter para continuar...", end=" ")
        input()
    
    def exibirTitulo(self):
        print("\t\t\tSistema de Catálogo de Pontos de Escavação\n")
        return
    
    def exibirErroDeOpcaoInvalida(self):
        os.system("clear")
        print("Por favor, escolha uma opção válida.")
        return
    
    
    def gostariaDeFiltrar(self):
        os.system("clear")
        print("Você gostaria de filtrar a listagem? (s/n)",end=" ")
        opcao = input().strip().lower()

        if opcao == 's':
            return True
        else:
            return False
    
    def gostariaDeOrdenar(self):
        os.system("clear")
        print("Você gostaria de ordenar a listagem? (s/n)",end=" ")
        opcao = input().strip().lower()

        if opcao == 's':
            return True
        else:
            return False
        
    def opcoesFiltragemPontoDeEscavacao(self):
        os.system("clear")
        array = []
        opcao = -1
        while opcao !=0:
            print("Para os pontos de escavação, existem esses critérios:")
            print("1 - ID")
            print("2 - ID do tipo de ponto")
            print("3 - ID do pesquisador")
            print("4 - Latitude")
            print("5 - Longitude")
            print("6 - Altitude")
            print("7 - Data de descoberta")
            print("0 - Terminar a filtragem")
            
            try:
                opcao = int(input())
                if(opcao ==0):
                    return array
                
                print("Operador (=, <, <=, >, >=):", end=" ")
                operador = input().strip()

                print("Valor:", end=" ")
                valor = input().strip()

                if operador in ["=", "<", ">", "<=", ">="]:
                    if(opcao == 1):
                        array.append(f"ID {operador} {valor}")
                    elif(opcao == 2):
                        array.append(f"TIPO_DE_PONTO_ID {operador} {valor}")
                    elif(opcao == 3):
                        array.append(f"PESQUISADOR_RESPONSAVEL_ID {operador} {valor}")
                    elif(opcao == 4):
                        array.append(f"LATITUDE {operador} {valor}")
                    elif(opcao == 5):
                        array.append(f"LONGITUDE {operador} {valor}")
                    elif(opcao == 6):
                        array.append(f"ALTITUDE {operador} {valor}")
                    elif(opcao == 7):
                        array.append(f"DATA_DE_DESCOBERTA {operador} {valor}")
                    else:
                        self.exibirErroDeOpcaoInvalida()
                else:
                    self.exibirErroDeOpcaoInvalida()
            
            except Exception as e:
                self.exibirErroDeOpcaoInvalida()

        return array
    
    def opcoesOrdenacaoPontosDeEscavacao(self):
        os.system("clear")
        array = []
        opcao = -1

        while opcao !=0:
            print("Para os pontos de escavação, existem esses critérios:")
            print("1 - ID")
            print("2 - ID do tipo de ponto")
            print("3 - ID do pesquisador")
            print("4 - Latitude")
            print("5 - Longitude")
            print("6 - Altitude")
            print("7 - Data de descoberta")
            print("0 - Terminar a ordenação")
            try:
                opcao = int(input())
                if(opcao ==0):
                    return array
                
                print("Caso queira ordenação crescente, coloque ASC")
                print("Caso queira ordenação decrescente, coloque DESC")
                direcao = input().strip().upper()
                if direcao in ["ASC", "DESC"]:
                    if (opcao == 1):
                        array.append(f"ID {direcao}")
                    elif(opcao == 2):
                        array.append(f"TIPO_DE_PONTO_ID {direcao}")
                    elif(opcao == 3):
                        array.append(f"PESQUISADOR_RESPONSAVEL_ID {direcao}")
                    elif(opcao == 4):
                        array.append(f"LATITUDE {direcao}")
                    elif(opcao == 5):
                        array.append(f"LONGITUDE {direcao}")
                    elif(opcao == 6):
                        array.append(f"ALTITUDE {direcao}")
                    elif(opcao == 7):
                        array.append(f"DATA_DE_DESCOBERTA {direcao}")
                    else:
                        self.exibirErroDeOpcaoInvalida()
                else:
                    self.exibirErroDeOpcaoInvalida()
            
            except Exception as e:
                self.exibirErroDeOpcaoInvalida()

        return array
    
    def opcoesFiltragemPesquisadores(self):
        os.system("clear")
        array = []
        opcao = -1
        while opcao !=0:
            print("Para os pesquisadores, existem esses critérios:")
            print("1 - ID ")
            print("2 - Nome Completo")
            print("3 - Telefone")
            print("4 - Email")
            print("5 - Especialidade")
            print("0 - Terminar a filtragem")
            
            try:
                opcao = int(input())
                if(opcao ==0):
                    return array
                
                print("Operador (=, <, <=, >, >=):", end=" ")
                operador = input().strip()

                print("Valor:", end=" ")
                valor = input().strip()

                if operador in ["=", "<", ">", "<=", ">="]:
                    if(opcao == 1):
                        array.append(f"ID {operador} {valor}")
                    elif(opcao == 2):
                        array.append(f"NOME_COMPLETO {operador} {valor}")
                    elif(opcao == 3):
                        array.append(f"TELEFONE {operador} {valor}")
                    elif(opcao == 4):
                        array.append(f"EMAIL {operador} {valor}")
                    elif(opcao == 5):
                        array.append(f"ESPECIALIDADE {operador} {valor}")
                    else:
                        self.exibirErroDeOpcaoInvalida()
                else:
                    self.exibirErroDeOpcaoInvalida()
            
            except Exception as e:
                self.exibirErroDeOpcaoInvalida()

        return array

    def opcoesOrdenacaoPesquisadores(self):
        os.system("clear")
        array = []
        opcao = -1
        while opcao !=0:
            print("Para os pesquisadores, existem esses critérios:")
            print("1 - ID ")
            print("2 - Nome Completo")
            print("3 - Telefone")
            print("4 - Email")
            print("5 - Especialidade")
            print("0 - Terminar a ordenação")
            
            try:
                opcao = int(input())
                if(opcao ==0):
                    return array
                
                print("Caso queira ordenação crescente, coloque ASC")
                print("Caso queira ordenação decrescente, coloque DESC")
                direcao = input().strip().upper()
                if direcao in ["ASC", "DESC"]:
                    if(opcao == 1):
                        array.append(f"ID {direcao}")
                    elif(opcao == 2):
                        array.append(f"NOME_COMPLETO {direcao}")
                    elif(opcao == 3):
                        array.append(f"TELEFONE {direcao}")
                    elif(opcao == 4):
                        array.append(f"EMAIL {direcao}")
                    elif(opcao == 5):
                        array.append(f"ESPECIALIDADE {direcao}")
                    else:
                        self.exibirErroDeOpcaoInvalida()
                else:
                    self.exibirErroDeOpcaoInvalida()
            
            except Exception as e:
                self.exibirErroDeOpcaoInvalida()

        return array
    
    def opcoesFiltragemTipoDePonto(self):
        os.system("clear")
        array = []
        opcao = -1
        while opcao !=0:
            print("Para os tipos de pontos, existem esses critérios:")
            print("1 - ID ")
            print("2 - Descrição")
            print("0 - Terminar a filtragem")
            
            try:
                opcao = int(input())
                if(opcao ==0):
                    return array
                
                print("Operador (=, <, <=, >, >=):", end=" ")
                operador = input().strip()

                print("Valor:", end=" ")
                valor = input().strip()

                if operador in ["=", "<", ">", "<=", ">="]:
                    if(opcao == 1):
                        array.append(f"ID {operador} {valor}")
                    elif(opcao == 2):
                        array.append(f"DESCRICAO {operador} {valor}")
                    else:
                        self.exibirErroDeOpcaoInvalida()
                else:
                    self.exibirErroDeOpcaoInvalida()
            
            except Exception as e:
                self.exibirErroDeOpcaoInvalida()

        return array

    def opcoesOrdenacaoTipoDePonto(self):
        os.system("clear")
        array = []
        opcao = -1
        while opcao !=0:
            print("Para os tipos de pontos, existem esses critérios:")
            print("1 - ID ")
            print("2 - Descricao")
            print("0 - Terminar a ordenação")
            
            try:
                opcao = int(input())
                if(opcao ==0):
                    return array
                
                print("Caso queira ordenação crescente, coloque ASC")
                print("Caso queira ordenação decrescente, coloque DESC")
                direcao = input().strip().upper()
                if direcao in ["ASC", "DESC"]:
                    if(opcao == 1):
                        array.append(f"ID {direcao}")
                    elif(opcao == 2):
                        array.append(f"DESCRICAO {direcao}")
                    else:
                        self.exibirErroDeOpcaoInvalida()
                else:
                    self.exibirErroDeOpcaoInvalida()
            
            except Exception as e:
                self.exibirErroDeOpcaoInvalida()

        return array
    
    def exibirErroDeInsercao(self):
        os.system("clear")
        print("Erro ao inserir registro!")
    
    def exibirErroDeAlteracao(self):
        os.system("clear")
        print("Erro ao atualizar registro!")
    
    def exibirErroDeExclusao(self):
        os.system("clear")
        print("Erro ao excluir registro!")
    
    def exibirErroDeListagem(self):
        os.system("clear")
        print("Erro ao listar registros!")

    def exibirSucessoInsercao(self, numero: int):
        os.system("clear")
        print(f"{numero} registros cadastrados com sucesso!")
        print("\nPressione Enter para continuar...", end=" ")
        input()

    def exibirSucessoAtualizacao(self, numero: int):
        os.system("clear")
        print(f"{numero} registros atualizados com sucesso!")
        print("\nPressione Enter para continuar...", end=" ")
        input()
    
    def exibirSucessoExclusao(self, numero: int):
        os.system("clear")
        print(f"{numero} registros excluídos com sucesso!")
        print("\nPressione Enter para continuar...", end=" ")
        input()