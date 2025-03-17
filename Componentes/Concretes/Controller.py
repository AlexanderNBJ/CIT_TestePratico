from ..Abstracts.ControllerAbstract import ControllerAbstract
from ..Abstracts.ConectorAbstract import ConectorAbstract
from ..Abstracts.InterfaceAbstract import InterfaceAbstract

class Controller(ControllerAbstract):
    def __init__(self, interface: InterfaceAbstract, conector: ConectorAbstract):
        self.registrosAdd = 0
        self.registrosAlt = 0
        self.registrosExcl = 0
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
                opcao = self.interface.exibirMenuAtualizar()
                self.avaliaOpcaoAtualizar(opcao)
            elif(opcao == 4):
                opcao = self.interface.exibirMenuRemover()
                self.avaliaOpcaoRemover(opcao)
            elif(opcao == 5):
                self.conector.executarQueryDeCommit()
                self.interface.exibirMensagemCommit(self.registrosAdd, self.registrosAlt, self.registrosExcl)
                self.registrosAdd = 0
                self.registrosAlt = 0
                self.registrosExcl = 0
            elif (opcao == 6):
                self.conector.executarQueryDeRollback()
                self.interface.exibirMensagemRollback(self.registrosAdd, self.registrosAlt, self.registrosExcl)
                self.registrosAdd = 0
                self.registrosAlt = 0
                self.registrosExcl = 0
            elif(opcao == 0):
                self.conector.executarQueryDeCommit()
                self.conector.encerrarConexao()
                self.emExecucao = False
                return
            else:
                self.interface.exibirErroDeOpcaoInvalida(e)
                return
        except Exception as e:
            self.interface.exibirErroDeOpcaoInvalida(e)
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
                self.interface.exibirErroDeOpcaoInvalida(e)
        except Exception as e:
            self.interface.exibirErroDeOpcaoInvalida(e)
            
        return
    
    def inserePontoDeEscavacao(self, arrayValores):
        arrayColunas = ["TIPO_DE_PONTO_ID", 
                        "PESQUISADOR_RESPONSAVEL_ID", 
                        "SRID",
                        "LATITUDE", 
                        "LONGITUDE", 
                        "ALTITUDE", 
                        "DATA_CATALOGACAO",
                        "DATA_DE_DESCOBERTA", 
                        "DESCRICAO"]
        
        for atributo in arrayValores:
            if atributo == "":
                atributo = "NULL"
        try:
            result = self.conector.executarQueryDeInsercao(arrayValores, arrayColunas, "PONTO_DE_ESCAVACAO")
            self.interface.exibirSucessoInsercao(result)
            self.registrosAdd+=result
        except Exception as e:
            self.interface.exibirErroDeInsercao(e)
            print(e)
    
    def inserePesquisador(self, arrayValores):
        arrayColunas = ["NOME_COMPLETO", "TELEFONE", "EMAIL", "ESPECIALIDADE"]
        
        for atributo in arrayValores:
            if atributo == "":
                atributo = "NULL"
        try:
            result = self.conector.executarQueryDeInsercao(arrayValores, arrayColunas, "PESQUISADOR")
            self.interface.exibirSucessoInsercao(result)
            self.registrosAdd+=result
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
            self.registrosAdd+=result
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
                arrayFiltro, arrayOrdem = self.interface.exibirListagemDePesquisador()
                resultado = self.buscaPesquisador(arrayFiltro, arrayOrdem)
                if resultado != None:
                    nomesColunas = self.conector.obterNomesDasColunas()
                    self.interface.exibirResultado(resultado, nomesColunas)
            elif(opcao == 3):
                arrayFiltro, arrayOrdem = self.interface.exibirListagemDeTipoDePonto()
                resultado = self.buscaTipoDePonto(arrayFiltro, arrayOrdem)
                if resultado != None:
                    nomesColunas = self.conector.obterNomesDasColunas()
                    self.interface.exibirResultado(resultado, nomesColunas)
            elif(opcao == 4):
                arrayFiltro, arrayOrdem = self.interface.exibirListagemDePontoDeEscavacaoTipoDePonto()
                resultado = self.buscaPontoTipoPonto(arrayFiltro, arrayOrdem)
                if resultado != None:
                    nomesColunas = self.conector.obterNomesDasColunas()
                    self.interface.exibirResultado(resultado, nomesColunas)
            elif(opcao == 5):
                arrayFiltro, arrayOrdem = self.interface.exibirListagemDePontoDeEscavacaoPesquisador()
                resultado = self.buscaPontoPesquisador(arrayFiltro, arrayOrdem)
                if resultado != None:
                    nomesColunas = self.conector.obterNomesDasColunas()
                    self.interface.exibirResultado(resultado, nomesColunas)
            elif(opcao == 6):
                arrayFiltro, arrayOrdem = self.interface.exibirListagemDePontoDeEscavacaoTipoDePontoPesquisador()
                resultado = self.buscaPontoTipoPontoPesquisador(arrayFiltro, arrayOrdem)
                if resultado != None:
                    nomesColunas = self.conector.obterNomesDasColunas()
                    self.interface.exibirResultado(resultado, nomesColunas)
            elif(opcao == 0):
                return
            else:
                self.interface.exibirErroDeOpcaoInvalida(e)
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
    
    def buscaPesquisador(self,arrayFiltro, arrayOrdem):
        condicao = ""
        if(arrayFiltro):
            condicao = "WHERE "+" AND ".join(arrayFiltro)
        if(arrayOrdem):
            condicao += " ORDER BY " +", ".join(arrayOrdem)
        try:
            resultado = self.conector.executarQueryDeSelecao(['*'],'PESQUISADOR', condicao)
            return resultado
        except Exception as e:
            self.interface.exibirErroDeListagem(e)
            return None
    
    def buscaTipoDePonto(self,arrayFiltro, arrayOrdem):
        condicao = ""
        if(arrayFiltro):
            condicao = "WHERE "+" AND ".join(arrayFiltro)
        if(arrayOrdem):
            condicao += " ORDER BY " +", ".join(arrayOrdem)
        try:
            resultado = self.conector.executarQueryDeSelecao(['*'],'TIPO_DE_PONTO', condicao)
            return resultado
        except Exception as e:
            self.interface.exibirErroDeListagem(e)
            return None
        
    def buscaPontoTipoPonto(self, arrayFiltro, arrayOrdem):
        condicao = ""
        if arrayFiltro:
            condicao = "WHERE " + " AND ".join(arrayFiltro)
        if arrayOrdem:
            condicao += " ORDER BY " + ", ".join(arrayOrdem)
        
        colunas = ["PONTO_DE_ESCAVACAO.ID AS PONTO_ID",
                    "PONTO_DE_ESCAVACAO.TIPO_DE_PONTO_ID",
                    "PONTO_DE_ESCAVACAO.PESQUISADOR_RESPONSAVEL_ID",
                    "PONTO_DE_ESCAVACAO.SRID",
                    "PONTO_DE_ESCAVACAO.LATITUDE",
                    "PONTO_DE_ESCAVACAO.LONGITUDE",
                    "PONTO_DE_ESCAVACAO.ALTITUDE",
                    "TO_CHAR(PONTO_DE_ESCAVACAO.DATA_CATALOGACAO, 'DD-MM-YYYY') AS DATA_CATALOGACAO",
                    "TO_CHAR(PONTO_DE_ESCAVACAO.DATA_DE_DESCOBERTA, 'DD-MM-YYYY') AS DATA_DESCOBERTA",
                    "PONTO_DE_ESCAVACAO.DESCRICAO AS DESCRICAO_PONTO",
                    "TIPO_DE_PONTO.DESCRICAO AS DESCRICAO_TIPO"]

        tabela ="""PONTO_DE_ESCAVACAO 
                        JOIN TIPO_DE_PONTO 
                        ON 
                            PONTO_DE_ESCAVACAO.TIPO_DE_PONTO_ID = TIPO_DE_PONTO.ID"""
        
        try:
            resultado = self.conector.executarQueryDeSelecao(colunas, tabela, condicao)
            return resultado
        except Exception as e:
            self.interface.exibirErroDeListagem(e)
            return None

    def buscaPontoPesquisador(self, arrayFiltro, arrayOrdem):
        condicao = ""
        if arrayFiltro:
            condicao = "WHERE " + " AND ".join(arrayFiltro)
        if arrayOrdem:
            condicao += " ORDER BY " + ", ".join(arrayOrdem)
        
        colunas = ["PONTO_DE_ESCAVACAO.ID AS PONTO_ID",
                    "PONTO_DE_ESCAVACAO.TIPO_DE_PONTO_ID",
                    "PONTO_DE_ESCAVACAO.PESQUISADOR_RESPONSAVEL_ID",
                    "PONTO_DE_ESCAVACAO.SRID",
                    "PONTO_DE_ESCAVACAO.LATITUDE",
                    "PONTO_DE_ESCAVACAO.LONGITUDE",
                    "PONTO_DE_ESCAVACAO.ALTITUDE",
                    "TO_CHAR(PONTO_DE_ESCAVACAO.DATA_CATALOGACAO, 'DD-MM-YYYY') AS DATA_CATALOGACAO",
                    "TO_CHAR(PONTO_DE_ESCAVACAO.DATA_DE_DESCOBERTA, 'DD-MM-YYYY') AS DATA_DESCOBERTA",
                    "PONTO_DE_ESCAVACAO.DESCRICAO AS DESCRICAO_PONTO",
                    "PESQUISADOR.NOME_COMPLETO AS PESQUISADOR_NOME",
                    "PESQUISADOR.TELEFONE AS PESQUISADOR_TELEFONE",
                    "PESQUISADOR.EMAIL AS PESQUISADOR_EMAIL",
                    "PESQUISADOR.ESPECIALIDADE AS PESQUISADOR_ESPECIALIDADE"]
        tabela ="""PONTO_DE_ESCAVACAO 
                        JOIN PESQUISADOR
                        ON 
                            PONTO_DE_ESCAVACAO.PESQUISADOR_RESPONSAVEL_ID = PESQUISADOR.ID"""
        
        try:
            resultado = self.conector.executarQueryDeSelecao(colunas, tabela, condicao)
            return resultado
        except Exception as e:
            self.interface.exibirErroDeListagem(e)
            return None

    def buscaPontoTipoPontoPesquisador(self, arrayFiltro, arrayOrdem):
        condicao = ""
        if arrayFiltro:
            condicao = "WHERE " + " AND ".join(arrayFiltro)
        if arrayOrdem:
            condicao += " ORDER BY " + ", ".join(arrayOrdem)
            
        colunas = [ "PONTO_DE_ESCAVACAO.ID AS PONTO_ID",
                    "PONTO_DE_ESCAVACAO.TIPO_DE_PONTO_ID",
                    "PONTO_DE_ESCAVACAO.PESQUISADOR_RESPONSAVEL_ID",
                    "PONTO_DE_ESCAVACAO.SRID",
                    "PONTO_DE_ESCAVACAO.LATITUDE",
                    "PONTO_DE_ESCAVACAO.LONGITUDE",
                    "PONTO_DE_ESCAVACAO.ALTITUDE",
                    "TO_CHAR(PONTO_DE_ESCAVACAO.DATA_CATALOGACAO, 'DD-MM-YYYY') AS DATA_CATALOGACAO",
                    "TO_CHAR(PONTO_DE_ESCAVACAO.DATA_DE_DESCOBERTA, 'YYYY-MM-DD') AS DATA_DESCOBERTA",
                    "PONTO_DE_ESCAVACAO.DESCRICAO AS DESCRICAO_PONTO",
                    "TIPO_DE_PONTO.DESCRICAO AS DESCRICAO_TIPO",
                    "PESQUISADOR.NOME_COMPLETO AS PESQUISADOR_NOME",
                    "PESQUISADOR.TELEFONE AS PESQUISADOR_TELEFONE",
                    "PESQUISADOR.EMAIL AS PESQUISADOR_EMAIL",
                    "PESQUISADOR.ESPECIALIDADE AS PESQUISADOR_ESPECIALIDADE"]
        tabela = """PONTO_DE_ESCAVACAO
                        JOIN TIPO_DE_PONTO 
                            ON PONTO_DE_ESCAVACAO.TIPO_DE_PONTO_ID = TIPO_DE_PONTO.ID
                        JOIN PESQUISADOR 
                            ON PONTO_DE_ESCAVACAO.PESQUISADOR_RESPONSAVEL_ID = PESQUISADOR.ID
        """ 
        
        try:
            resultado = self.conector.executarQueryDeSelecao(colunas, tabela, condicao)
            return resultado
        except Exception as e:
            self.interface.exibirErroDeListagem(e)
            return None

    def avaliaOpcaoAtualizar(self, opcao):
        try:
            opcao = int(opcao)

            if(opcao == 1):
                id, array = self.interface.exibirAtualizacaoDePontoDeEscavacao()
                self.atualizaPontoDeEscavacao(id, array)
            elif(opcao == 2):
                id, array = self.interface.exibirAtualizacaoDePesquisador()
                self.atualizaPesquisador(id,array)
            elif(opcao == 3):
                id, array = self.interface.exibirAtualizacaoDeTipoDePonto()
                self.atualizaTipoDePonto(id, array)
            elif(opcao == 0):
                return
            else:
                self.interface.exibirErroDeOpcaoInvalida(e)
        except Exception as e:
            self.interface.exibirErroDeOpcaoInvalida(e)
            
        return
    
    def atualizaPontoDeEscavacao(self, id, array: dict[str, str]):
        for chave, valor in array.items():
            if valor.strip() == "":
                array[chave] = None
        try:
            result = self.conector.executarQueryDeAtualizacao(array, "PONTO_DE_ESCAVACAO", f"ID = {id}")
            self.interface.exibirSucessoAtualizacao(result)
            self.registrosAlt+=result
        except Exception as e:
            self.interface.exibirErroDeAlteracao(e)
    
    def atualizaPesquisador(self, id, array: dict[str, str]):
        for chave, valor in array.items():
            if valor.strip() == "":
                array[chave] = None
        try:
            result = self.conector.executarQueryDeAtualizacao(array, "PESQUISADOR", f"ID = {id}")
            self.interface.exibirSucessoAtualizacao(result)
            self.registrosAlt+=result
        except Exception as e:
            self.interface.exibirErroDeAlteracao(e)
        return
    
    def atualizaTipoDePonto(self, id, array: dict[str, str]):
        for chave, valor in array.items():
            if valor.strip() == "":
                array[chave] = None
        try:
            result = self.conector.executarQueryDeAtualizacao(array, "TIPO_DE_PONTO", f"ID = {id}")
            self.interface.exibirSucessoAtualizacao(result)
            self.registrosAlt+=result
        except Exception as e:
            self.interface.exibirErroDeAlteracao(e)
        return

    def avaliaOpcaoRemover(self, opcao):
        try:
            opcao = int(opcao)

            if(opcao == 1):
                id = self.interface.exibirExclusaoDePontoDeEscavacao()
                self.removerPontoDeEscavacao(id)
            elif(opcao == 2):
                id = self.interface.exibirExclusaoDePesquisador()
                self.removerPesquisador(id)
            elif(opcao == 3):
                id  = self.interface.exibirExclusaoDeTipoDePonto()
                self.removerTipoDePonto(id)
            elif(opcao == 0):
                return
            else:
                self.interface.exibirErroDeOpcaoInvalida(e)
        except Exception as e:
            self.interface.exibirErroDeOpcaoInvalida(e)
            
        return
    
    def removerPontoDeEscavacao(self, id):
        try:
            result = self.conector.executarQueryDeDelecao( "PONTO_DE_ESCAVACAO", f"ID = {id}")
            self.interface.exibirSucessoExclusao(result)
            self.registrosExcl+=result
        except Exception as e:
            self.interface.exibirErroDeExclusao(e)
        return
    
    def removerPesquisador(self, id):
        try:
            result = self.conector.executarQueryDeDelecao("PESQUISADOR", f"ID = {id}")
            self.interface.exibirSucessoExclusao(result)
            self.registrosExcl+=result
        except Exception as e:
            self.interface.exibirErroDeExclusao(e)
        return
    
    def removerTipoDePonto(self, id):
        try:
            result = self.conector.executarQueryDeDelecao("TIPO_DE_PONTO", f"ID = {id}")
            self.interface.exibirSucessoExclusao(result)
            self.registrosExcl+=result
        except Exception as e:
            self.interface.exibirErroDeExclusao(e)
        return
    