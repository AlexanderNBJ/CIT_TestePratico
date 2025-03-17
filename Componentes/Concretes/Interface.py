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
        print("5 - Confirmar alterações")
        print("6 - Reverter alterações")
        print("0 - Encerrar progama\n")
        print("Digite uma operação...", end=" ")
        return input().strip()

    def exibirMenuCadastro(self):
        os.system("clear")
        print("------ Menu de Cadastro:")
        print("1 - Cadastrar Ponto de Escavação")
        print("2 - Cadastrar Pesquisador")
        print("3 - Cadastrar Tipo de Ponto")
        print("0 - Retornar\n")
        print("Digite uma operação...", end=" ")
        return input().strip()
    
    def exibirMenuListar(self):
        os.system("clear")
        print("------ Menu de Listagem:")
        print("1 - Listar Ponto de Escavação")
        print("2 - Listar Pesquisador")
        print("3 - Listar Tipo de Ponto")
        print("4 - Listar Ponto de Escavação + Tipo de Ponto")
        print("5 - Listar Ponto de Escavação + Pesquisador")
        print("6 - Listar Ponto de Escavação + Tipo de Ponto + Pesquisador")
        print("0 - Retornar\n")
        print("Digite uma operação...", end=" ")
        return input().strip()
    
    def exibirMenuAtualizar(self):
        os.system("clear")
        print("------ Menu de Atualização de Cadastro:")
        print("1 - Atualizar Ponto de Escavação")
        print("2 - Atualizar Pesquisador")
        print("3 - Atualizar Tipo de Ponto")
        print("0 - Retornar\n")
        print("Digite uma operação...", end=" ")
        return input().strip()
    
    def exibirMenuRemover(self):
        os.system("clear")
        print("------ Menu de Exclusão de Cadastro:")
        print("1 - Excluir Ponto de Escavação")
        print("2 - Excluir Pesquisador")
        print("3 - Excluir Tipo de Ponto")
        print("0 - Retornar\n")
        print("Digite uma operação...", end=" ")
        return input().strip()
    
    def exibirCadastroDePontoDeEscavacao(self):
        os.system("clear")
        array = []
        print("Digite o número do tipo de ponto:", end=" ")
        array.append(input().strip())
        print("Digite o ID do pesquisador responsável:", end=" ")
        array.append(input().strip())
        print("Digite o SRID:", end=" ")
        array.append(input().strip())
        print("Digite a latitude do ponto:", end=" ")
        array.append(input().strip())
        print("Digite a longitude do ponto:", end=" ")
        array.append(input().strip())
        print("Digite a altitude do ponto:", end=" ")
        array.append(input().strip())
        print("Digite a data de catalogação do ponto:", end=" ")
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
        arrayFiltro = ""
        arrayOrdem = ""
        if(self.gostariaDeFiltrar()):
            arrayFiltro = self.opcoesFiltragemPontoDeEscavacao()
        if(self.gostariaDeOrdenar()):
            arrayOrdem = self.opcoesOrdenacaoPontosDeEscavacao()
        
        return arrayFiltro, arrayOrdem
    
    def exibirListagemDePesquisador(self):
        os.system("clear")
        arrayFiltro = ""
        arrayOrdem = ""
        if(self.gostariaDeFiltrar()):
            arrayFiltro = self.opcoesFiltragemPesquisadores()
        
        if(self.gostariaDeOrdenar()):
            arrayOrdem = self.opcoesOrdenacaoPesquisadores()
        return arrayFiltro, arrayOrdem
    
    def exibirListagemDeTipoDePonto(self):
        os.system("clear")
        arrayFiltro = ""
        arrayOrdem = ""
        if(self.gostariaDeFiltrar()):
            arrayFiltro = self.opcoesFiltragemTipoDePonto()
        
        if(self.gostariaDeOrdenar()):
            arrayOrdem = self.opcoesOrdenacaoTipoDePonto()
        return arrayFiltro, arrayOrdem
    
    def exibirListagemDePontoDeEscavacaoTipoDePonto(self):
        os.system("clear")
        arrayFiltro = ""
        arrayOrdem = ""
        if self.gostariaDeFiltrar():
            arrayFiltro = self.opcoesFiltragemPontoTipo()
        if self.gostariaDeOrdenar():
            arrayOrdem = self.opcoesOrdenacaoPontoTipo()
        return arrayFiltro, arrayOrdem

    def exibirListagemDePontoDeEscavacaoPesquisador(self):
        os.system("clear")
        arrayFiltro = ""
        arrayOrdem = ""
        if self.gostariaDeFiltrar():
            arrayFiltro = self.opcoesFiltragemPontoPesquisador()
        if self.gostariaDeOrdenar():
            arrayOrdem = self.opcoesOrdenacaoPontoPesquisador()
        return arrayFiltro, arrayOrdem

    def exibirListagemDePontoDeEscavacaoTipoDePontoPesquisador(self):
        os.system("clear")
        arrayFiltro = ""
        arrayOrdem = ""
        if self.gostariaDeFiltrar():
            arrayFiltro = self.opcoesFiltragemCompleta()
        if self.gostariaDeOrdenar():
            arrayOrdem = self.opcoesOrdenacaoCompleta()
        return arrayFiltro, arrayOrdem

    def opcoesFiltragemPontoTipo(self):
        array = []
        opcao = -1
        while opcao != 0:
            os.system("clear")
            print("Filtros para Ponto + Tipo:")
            print("1 - ID do Ponto")
            print("2 - Tipo de Ponto (ID)")
            print("3 - Latitude")
            print("4 - Longitude")
            print("5 - Altitude")
            print("6 - Data de Descoberta")
            print("7 - Descrição do Ponto")
            print("8 - Descrição do Tipo")
            print("0 - Terminar filtragem")
            try:
                opcao = int(input())
                if opcao == 0:
                    return array
                
                colunas = {
                    1: "PONTO_DE_ESCAVACAO.ID",
                    2: "PONTO_DE_ESCAVACAO.TIPO_DE_PONTO_ID",
                    3: "PONTO_DE_ESCAVACAO.LATITUDE",
                    4: "PONTO_DE_ESCAVACAO.LONGITUDE",
                    5: "PONTO_DE_ESCAVACAO.ALTITUDE",
                    6: "PONTO_DE_ESCAVACAO.DATA_DE_DESCOBERTA",
                    7: "PONTO_DE_ESCAVACAO.DESCRICAO",
                    8: "TIPO_DE_PONTO.DESCRICAO"
                }
                
                if opcao in colunas:
                    print("Operador (=, <, >, <=, >=, LIKE):", end=" ")
                    operador = input().strip()
                    print("Valor:", end=" ")
                    valor = input().strip()
                    array.append(f"{colunas[opcao]} {operador} '{valor}'")
                else:
                    self.exibirErroDeOpcaoInvalida()
            except:
                self.exibirErroDeOpcaoInvalida()
        return array

    def opcoesOrdenacaoPontoTipo(self):
        array = []
        opcao = -1
        while opcao != 0:
            os.system("clear")
            print("Ordenação para Ponto + Tipo:")
            print("1 - ID do Ponto")
            print("2 - SRID")
            print("3 - Latitude")
            print("4 - Longitude")
            print("5 - Altitude")
            print("6 - Data de Descoberta")
            print("7 - Data de Catalogação")
            print("8 - Descrição do Tipo de Ponto")
            print("0 - Terminar ordenação")
            try:
                opcao = int(input())
                if opcao == 0:
                    return array
                
                colunas = {
                    1: "PONTO_DE_ESCAVACAO.ID",
                    2: "PONTO_DE_ESCAVACAO.SRID",
                    3: "PONTO_DE_ESCAVACAO.LATITUDE",
                    4: "PONTO_DE_ESCAVACAO.LONGITUDE",
                    5: "PONTO_DE_ESCAVACAO.ALTITUDE",
                    6: "PONTO_DE_ESCAVACAO.DATA_DE_DESCOBERTA",
                    7: "PONTO_DE_ESCAVACAO.DATA_CATALOGACAO",
                    8: "TIPO_DE_PONTO.DESCRICAO"
                }
                
                if opcao in colunas:
                    print("Direção (ASC/DESC):", end=" ")
                    direcao = input().strip().upper()
                    array.append(f"{colunas[opcao]} {direcao}")
                else:
                    self.exibirErroDeOpcaoInvalida()
            except:
                self.exibirErroDeOpcaoInvalida()
        return array

    def opcoesFiltragemPontoPesquisador(self):
        array = []
        opcao = -1
        while opcao != 0:
            os.system("clear")
            print("Filtros para Ponto + Pesquisador:")
            print("1 - ID do Ponto")
            print("2 - Pesquisador (ID)")
            print("3 - SRID")
            print("4 - Latitude")
            print("5 - Longitude")
            print("6 - Altitude")
            print("7 - Data de Descoberta")
            print("8 - Data de Catalogação")
            print("9 - Descrição do Ponto")
            print("10 - Nome do Pesquisador")
            print("11 - Telefone")
            print("12 - Email")
            print("13 - Especialidade")
            print("0 - Terminar filtragem")
            try:
                opcao = int(input())
                if opcao == 0:
                    return array
                
                colunas = {
                    1: "PONTO_DE_ESCAVACAO.ID",
                    2: "PONTO_DE_ESCAVACAO.PESQUISADOR_RESPONSAVEL_ID",
                    3: "PONTO_DE_ESCAVACAO.SRID",
                    4: "PONTO_DE_ESCAVACAO.LATITUDE",
                    5: "PONTO_DE_ESCAVACAO.LONGITUDE",
                    6: "PONTO_DE_ESCAVACAO.ALTITUDE",
                    7: "PONTO_DE_ESCAVACAO.DATA_DE_DESCOBERTA",
                    8: "PONTO_DE_ESCAVACAO.DATA_CATALOGACAO",
                    9: "PONTO_DE_ESCAVACAO.DESCRICAO",
                    10: "PESQUISADOR.NOME_COMPLETO",
                    11: "PESQUISADOR.TELEFONE",
                    12: "PESQUISADOR.EMAIL",
                    13: "PESQUISADOR.ESPECIALIDADE"
                }
                
                if opcao in colunas:
                    print("Operador (=, <, >, <=, >=, LIKE):", end=" ")
                    operador = input().strip()
                    print("Valor:", end=" ")
                    valor = input().strip()
                    array.append(f"{colunas[opcao]} {operador} '{valor}'")
                else:
                    self.exibirErroDeOpcaoInvalida()
            except:
                self.exibirErroDeOpcaoInvalida()
        return array

    def opcoesOrdenacaoPontoPesquisador(self):
        array = []
        opcao = -1
        while opcao != 0:
            os.system("clear")
            print("Ordenação para Ponto + Pesquisador:")
            print("1 - ID do Ponto")
            print("2 - Pesquisador (ID)")
            print("3 - SRID")
            print("4 - Latitude")
            print("5 - Longitude")
            print("6 - Altitude")
            print("7 - Data de Descoberta")
            print("8 - Data de Catalogação")
            print("9 - Descrição do Ponto")
            print("10 - Nome do Pesquisador")
            print("11 - Telefone")
            print("12 - Email")
            print("13 - Especialidade")
            print("0 - Terminar filtragem")
            try:
                opcao = int(input())
                if opcao == 0:
                    return array
                
                colunas = {
                    1: "PONTO_DE_ESCAVACAO.ID",
                    2: "PONTO_DE_ESCAVACAO.PESQUISADOR_RESPONSAVEL_ID",
                    3: "PONTO_DE_ESCAVACAO.SRID",
                    4: "PONTO_DE_ESCAVACAO.LATITUDE",
                    5: "PONTO_DE_ESCAVACAO.LONGITUDE",
                    6: "PONTO_DE_ESCAVACAO.ALTITUDE",
                    7: "PONTO_DE_ESCAVACAO.DATA_DE_DESCOBERTA",
                    8: "PONTO_DE_ESCAVACAO.DATA_CATALOGACAO",
                    9: "PONTO_DE_ESCAVACAO.DESCRICAO",
                    10: "PESQUISADOR.NOME_COMPLETO",
                    11: "PESQUISADOR.TELEFONE",
                    12: "PESQUISADOR.EMAIL",
                    13: "PESQUISADOR.ESPECIALIDADE"
                }
                
                if opcao in colunas:
                    print("Direção (ASC/DESC):", end=" ")
                    direcao = input().strip().upper()
                    array.append(f"{colunas[opcao]} {direcao}")
                else:
                    self.exibirErroDeOpcaoInvalida()
            except:
                self.exibirErroDeOpcaoInvalida()
        return array

    def opcoesFiltragemCompleta(self):
        array = []
        opcao = -1
        while opcao != 0:
            os.system("clear")
            print("Filtros para Ponto + Tipo + Pesquisador:")
            print("1 - ID do Ponto")
            print("2 - Tipo de Ponto (ID)")
            print("3 - Pesquisador (ID)")
            print("4 - SRID")
            print("5 - Latitude")
            print("6 - Longitude")
            print("7 - Altitude")
            print("8 - Data de Descoberta")
            print("9 - Data de Catalogação")
            print("10 - Descrição do Ponto")
            print("11 - Descrição do Tipo")
            print("12 - Nome do Pesquisador")
            print("13 - Telefone")
            print("14 - Email")
            print("15 - Especialidade")
            print("0 - Terminar filtragem")
            try:
                opcao = int(input())
                if opcao == 0:
                    return array
                
                colunas = {
                    1: "PONTO_DE_ESCAVACAO.ID",
                    2: "TIPO_DE_PONTO.ID",
                    3: "PESQUISADOR.ID",
                    4: "PONTO_DE_ESCAVACAO.SRID",
                    5: "PONTO_DE_ESCAVACAO.LATITUDE",
                    6: "PONTO_DE_ESCAVACAO.LONGITUDE",
                    7: "PONTO_DE_ESCAVACAO.ALTITUDE",
                    8: "PONTO_DE_ESCAVACAO.DATA_DE_DESCOBERTA",
                    9: "PONTO_DE_ESCAVACAO.DATA_CATALOGACAO",
                    10: "PONTO_DE_ESCAVACAO.DESCRICAO",
                    11: "TIPO_DE_PONTO.DESCRICAO",
                    12: "PESQUISADOR.NOME_COMPLETO",
                    13: "PESQUISADOR.TELEFONE",
                    14: "PESQUISADOR.EMAIL",
                    15: "PESQUISADOR.ESPECIALIDADE"
                }
                
                if opcao in colunas:
                    print("Operador (=, <, >, <=, >=, LIKE):", end=" ")
                    operador = input().strip()
                    print("Valor:", end=" ")
                    valor = input().strip()
                    array.append(f"{colunas[opcao]} {operador} '{valor}'")
                else:
                    self.exibirErroDeOpcaoInvalida()
            except:
                self.exibirErroDeOpcaoInvalida()
        return array

    def opcoesOrdenacaoCompleta(self):
        array = []
        opcao = -1
        while opcao != 0:
            os.system("clear")
            print("Ordenação para Ponto + Tipo + Pesquisador:")
            print("1 - ID do Ponto")
            print("2 - Tipo de Ponto (ID)")
            print("3 - Pesquisador (ID)")
            print("4 - Latitude")
            print("5 - Longitude")
            print("6 - Altitude")
            print("7 - Data de Descoberta")
            print("8 - Descrição do Ponto")
            print("9 - Descrição do Tipo")
            print("10 - Nome do Pesquisador")
            print("11 - Telefone")
            print("12 - Email")
            print("13 - Especialidade")
            print("0 - Terminar filtragem")
            try:
                opcao = int(input())
                if opcao == 0:
                    return array
                
                colunas = {
                    1: "PONTO_DE_ESCAVACAO.ID",
                    2: "TIPO_DE_PONTO.ID",
                    3: "PESQUISADOR.ID",
                    4: "PONTO_DE_ESCAVACAO.LATITUDE",
                    5: "PONTO_DE_ESCAVACAO.LONGITUDE",
                    6: "PONTO_DE_ESCAVACAO.ALTITUDE",
                    7: "PONTO_DE_ESCAVACAO.DATA_DE_DESCOBERTA",
                    8: "PONTO_DE_ESCAVACAO.DESCRICAO",
                    9: "TIPO_DE_PONTO.DESCRICAO",
                    10: "PESQUISADOR.NOME_COMPLETO",
                    11: "PESQUISADOR.TELEFONE",
                    12: "PESQUISADOR.EMAIL",
                    13: "PESQUISADOR.ESPECIALIDADE"
                }
                
                if opcao in colunas:
                    print("Direção (ASC/DESC):", end=" ")
                    direcao = input().strip().upper()
                    array.append(f"{colunas[opcao]} {direcao}")
                else:
                    self.exibirErroDeOpcaoInvalida()
            except:
                self.exibirErroDeOpcaoInvalida()
        return array

    def exibirAtualizacaoDePontoDeEscavacao(self):
        os.system("clear")
        print("Digite o ID do ponto de escavação que deseja atualizar:", end=" ")
        id_ponto = input().strip()
        
        print("Selecione os campos para atualizar (separados por vírgula):")
        print("1 - Tipo de Ponto")
        print("2 - Pesquisador Responsável")
        print("3 - SRID")
        print("4 - Latitude")
        print("5 - Longitude")
        print("6 - Altitude")
        print("7 - Data de Catalogação")
        print("8 - Data de Descoberta")
        print("9 - Descrição")
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
                print("Novo SRID:", end=" ")
                atualizacoes['SRID'] = input().strip()
            elif campo == '4':
                print("Nova Latitude:", end=" ")
                atualizacoes['LATITUDE'] = input().strip()
            elif campo == '5':
                print("Nova Longitude:", end=" ")
                atualizacoes['LONGITUDE'] = input().strip()
            elif campo == '6':
                print("Nova Altitude:", end=" ")
                atualizacoes['ALTITUDE'] = input().strip()
            elif campo == '7':
                print("Nova Data de Catalogação (YYYY-MM-DD):", end=" ")
                atualizacoes['DATA_CATALOGACAO'] = input().strip()
            elif campo == '8':
                print("Nova Data de Descoberta (YYYY-MM-DD):", end=" ")
                atualizacoes['DATA_DE_DESCOBERTA'] = input().strip()
            elif campo == '9':
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

    def exibirResultado(self, resultado, nomeColunas):
        os.system("clear")
        print("Resultado da operação:\n")
        
        for linha in resultado:
            for coluna, nomeDaColuna in zip(linha, nomeColunas):
                if(nomeDaColuna.upper()!='DESCRICAO' and nomeDaColuna.upper()!='DESCRICAO_PONTO'):
                    if(str(coluna).upper()!='NONE'):
                        print(f"{nomeDaColuna.upper()}: {coluna}")
                    else:
                        print(f"{nomeDaColuna.upper()}: n/a")
                else:
                    if(str(coluna).upper()!='NONE'):
                        print(f"{nomeDaColuna.upper()}:\n{coluna}")
                    else:
                        print(f"{nomeDaColuna.upper()}:\nn/a")
                    
            print()    
        print("\nPressione Enter para continuar...", end=" ")
        input()
    
    def exibirTitulo(self):
        print("\t\t\tSistema de Catálogo de Pontos de Escavação\n")
        return
    
    def exibirErroDeOpcaoInvalida(self, e: Exception):
        os.system("clear")
        print("Por favor, escolha uma opção válida.")
        print(e)
        print("\nPressione Enter para continuar...", end=" ")
        input()
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
        array = []
        opcao = -1
        while opcao !=0:
            os.system("clear")
            print("Para os pontos de escavação, existem esses critérios:")
            print("1 - ID do tipo de ponto")
            print("2 - ID do pesquisador")
            print("3 - SRID ")
            print("4 - Latitude")
            print("5 - Longitude")
            print("6 - Altitude")
            print("7 - Data de catalogação")
            print("8 - Data de descoberta")
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
                        array.append(f"TIPO_DE_PONTO_ID {operador} '{valor}'")
                    elif(opcao == 2):
                        array.append(f"PESQUISADOR_RESPONSAVEL_ID {operador} '{valor}'")
                    elif(opcao == 3):
                        array.append(f"SRID {operador} '{valor}'")
                    elif(opcao == 4):
                        array.append(f"LATITUDE {operador} '{valor}'")
                    elif(opcao == 5):
                        array.append(f"LONGITUDE {operador} '{valor}'")
                    elif(opcao == 6):
                        array.append(f"ALTITUDE {operador} '{valor}'")
                    elif(opcao == 7):
                        array.append(f"DATA_CATALOGACAO {operador} '{valor}'")
                    elif(opcao == 8):
                        array.append(f"DATA_DE_DESCOBERTA {operador} '{valor}'")
                    else:
                        self.exibirErroDeOpcaoInvalida()
                else:
                    self.exibirErroDeOpcaoInvalida()
            
            except Exception as e:
                self.exibirErroDeOpcaoInvalida()

        return array
    
    def opcoesOrdenacaoPontosDeEscavacao(self):
        array = []
        opcao = -1

        while opcao !=0:
            os.system("clear")
            print("Para os pontos de escavação, existem esses critérios:")
            print("1 - ID do tipo de ponto")
            print("2 - ID do pesquisador")
            print("3 - SRID ")
            print("4 - Latitude")
            print("5 - Longitude")
            print("6 - Altitude")
            print("7 - Data de catalogação")
            print("8 - Data de descoberta")
            print("0 - Terminar a filtragem")
            try:
                opcao = int(input())
                if(opcao ==0):
                    return array
                
                print("Caso queira ordenação crescente, coloque ASC")
                print("Caso queira ordenação decrescente, coloque DESC")
                direcao = input().strip().upper()
                if direcao in ["ASC", "DESC"]:
                    if (opcao == 1):
                        array.append(f"TIPO_DE_PONTO_ID {direcao}")
                    elif(opcao == 2):
                        array.append(f"PESQUISADOR_RESPONSAVEL_ID {direcao}")
                    elif(opcao == 3):
                        array.append(f"SRID {direcao}")
                    elif(opcao == 4):
                        array.append(f"LATITUDE {direcao}")
                    elif(opcao == 5):
                        array.append(f"LONGITUDE {direcao}")
                    elif(opcao == 6):
                        array.append(f"ALTITUDE {direcao}")
                    elif(opcao == 7):
                        array.append(f"DATA_CATALOGACAO {direcao}")
                    elif(opcao == 8):
                        array.append(f"DATA_DE_DESCOBERTA {direcao}")
                    else:
                        self.exibirErroDeOpcaoInvalida()
                else:
                    self.exibirErroDeOpcaoInvalida()
            
            except Exception as e:
                self.exibirErroDeOpcaoInvalida()

        return array
    
    def opcoesFiltragemPesquisadores(self):
        array = []
        opcao = -1
        while opcao !=0:
            os.system("clear")
            print("Para os pesquisadores, existem esses critérios:")
            print("1 - Nome Completo")
            print("2 - Telefone")
            print("3 - Email")
            print("4 - Especialidade")
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
                        array.append(f"NOME_COMPLETO {operador} '{valor}'")
                    elif(opcao == 2):
                        array.append(f"TELEFONE {operador} '{valor}'")
                    elif(opcao == 3):
                        array.append(f"EMAIL {operador} '{valor}'")
                    elif(opcao == 4):
                        array.append(f"ESPECIALIDADE {operador} '{valor}'")
                    else:
                        self.exibirErroDeOpcaoInvalida()
                else:
                    self.exibirErroDeOpcaoInvalida()
            
            except Exception as e:
                self.exibirErroDeOpcaoInvalida()

        return array

    def opcoesOrdenacaoPesquisadores(self):
        array = []
        opcao = -1
        while opcao !=0:
            os.system("clear")
            print("Para os pesquisadores, existem esses critérios:")
            print("1 - Nome Completo")
            print("2 - Telefone")
            print("3 - Email")
            print("4 - Especialidade")
            print("0 - Terminar a filtragem")
            
            try:
                opcao = int(input())
                if(opcao ==0):
                    return array
                
                print("Caso queira ordenação crescente, coloque ASC")
                print("Caso queira ordenação decrescente, coloque DESC")
                direcao = input().strip().upper()
                if direcao in ["ASC", "DESC"]:
                    if(opcao == 1):
                        array.append(f"NOME_COMPLETO {direcao}")
                    elif(opcao == 2):
                        array.append(f"TELEFONE {direcao}")
                    elif(opcao == 3):
                        array.append(f"EMAIL {direcao}")
                    elif(opcao == 4):
                        array.append(f"ESPECIALIDADE {direcao}")
                    else:
                        self.exibirErroDeOpcaoInvalida()
                else:
                    self.exibirErroDeOpcaoInvalida()
            
            except Exception as e:
                self.exibirErroDeOpcaoInvalida()

        return array
    
    def opcoesFiltragemTipoDePonto(self):
        array = []
        opcao = -1
        while opcao !=0:
            os.system("clear")
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
                        array.append(f"ID {operador} '{valor}'")
                    elif(opcao == 2):
                        array.append(f"DESCRICAO {operador} '{valor}'")
                    else:
                        self.exibirErroDeOpcaoInvalida()
                else:
                    self.exibirErroDeOpcaoInvalida()
            
            except Exception as e:
                self.exibirErroDeOpcaoInvalida()

        return array

    def opcoesOrdenacaoTipoDePonto(self):
        array = []
        opcao = -1
        while opcao !=0:
            os.system("clear")
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
    
    def exibirErroDeInsercao(self, e: Exception):
        os.system("clear")
        print("Falha na inserção de registro: ")
        print(e)
        print("\nPressione Enter para continuar...", end=" ")
        input()
    
    def exibirErroDeAlteracao(self, e: Exception):
        os.system("clear")
        print("Falha na atualização de registro!")
        print(e)
        print("\nPressione Enter para continuar...", end=" ")
        input()
    
    def exibirErroDeExclusao(self, e: Exception):
        os.system("clear")
        print("Falha na exclusão de registro!")
        print(e)
        print("\nPressione Enter para continuar...", end=" ")
        input()
    
    def exibirErroDeListagem(self, e: Exception):
        os.system("clear")
        print("Erro ao listar registros!")
        print(e)
        print("\nPressione Enter para continuar...", end=" ")
        input()

    def exibirSucessoInsercao(self, numero: int):
        os.system("clear")
        print(f"{numero} registros cadastrados com sucesso!\nConfirme a mudança no Menu Principal.")
        print("\nPressione Enter para continuar...", end=" ")
        input()

    def exibirSucessoAtualizacao(self, numero: int):
        os.system("clear")
        print(f"{numero} registros atualizados com sucesso!\nConfirme a mudança no Menu Principal.")
        print("\nPressione Enter para continuar...", end=" ")
        input()
    
    def exibirSucessoExclusao(self, numero: int):
        os.system("clear")
        print(f"{numero} registros excluídos com sucesso!\nConfirme a mudança no Menu Principal.")
        print("\nPressione Enter para continuar...", end=" ")
        input()
    
    def exibirMensagemCommit(self, adds: int, alts: int, excls: int):
        os.system("clear")
        print(f"{adds} registros adicionados com sucesso!")
        print(f"{alts} registros alterados com sucesso!")
        print(f"{excls} registros excluídos com sucesso!")
        print("\nPressione Enter para continuar...", end=" ")
        input()
    
    def exibirMensagemRollback(self, adds: int, alts: int, excls: int):
        os.system("clear")
        print(f"{adds} novos registros revertidos com sucesso!")
        print(f"{alts} registros alterados revertidos com sucesso!")
        print(f"{excls} registros excluídos  revertidos com sucesso!")
        print("\nPressione Enter para continuar...", end=" ")
        input()