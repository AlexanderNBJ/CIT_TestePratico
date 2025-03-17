import psycopg2
import os
from ..Abstracts.ConectorAbstract import ConectorAbstract

class Conector(ConectorAbstract):
    def __init__(self, dbname, user, password, host, port):
        try:
            self.connector = psycopg2.connect(dbname=dbname,user=user,password=password,host=host,port=port)
            self.cursor = self.connector.cursor()
        except psycopg2.OperationalError as e:
            print("A database não existe ainda. Será executado um script de criação:")
            os.system("cd ../..")
            os.system("sudo -u postgres psql < Setup/setup.sql")
            self.connector = psycopg2.connect(dbname=dbname,user=user,password=password,host=host,port=port)
            self.cursor = self.connector.cursor()
        except Exception as e:
            self.connector = self.cursor = None

    def executarQueryDeSelecao(self, atributos: list[str], tabela: str, condicoes=""):
        colunas = ""

        for i in range(0, len(atributos)-1):
            colunas+=atributos[i]+", "

        colunas+= atributos[len(atributos)-1]

        self.cursor.execute("SELECT "+colunas+" FROM "+tabela+" "+condicoes)
        return self.cursor.fetchall()
    
    def executarQueryDeAtualizacao(self, atualizar: dict[str, str], tabela: str, condicoes=""):
        set_clause = ", ".join([f"{coluna} = %s" for coluna in atualizar.keys()])

        valores = list(atualizar.values())

        query = f"UPDATE {tabela} SET {set_clause}"

        if condicoes:
            query += f" WHERE {condicoes}"
        
        self.cursor.execute(query, valores)
        return self.cursor.rowcount
    
    def executarQueryDeDelecao(self, tabela: str, condicoes=""):
        query = "DELETE FROM " + tabela

        if condicoes:
            query += " WHERE " + condicoes

        self.cursor.execute(query)
        return self.cursor.rowcount
    
    def executarQueryDeInsercao(self, atributosReais: list[str], colunasDaTabela:list[str], tabela: str):
        if not(isinstance(atributosReais, str)):
            valor = []
            for atributo in atributosReais:
                atributo = atributo.strip()
                if atributo == '':
                    valor.append("NULL")
                else:
                    valor.append(f"'{atributo}'")
            valorReal = " ,".join(valor)
        else:
            if atributosReais.strip() == '':
                valorReal = "NULL"
            else:
                valorReal = "'"+atributosReais+"'"

        colunasAInserir = ", ".join(colunasDaTabela)
        query = f"INSERT INTO {tabela} ({colunasAInserir}) VALUES ({valorReal})"
        self.cursor.execute(query)
    
        return self.cursor.rowcount
    
    def executarQueryDeCommit(self):
        self.connector.commit()
        return
    
    def executarQueryDeRollback(self):
        self.connector.rollback()
        return
    
    def encerrarConexao(self):
        self.connector.close()
        self.cursor.close()
        return
    
    def obterNomesDasColunas(self):
        nomesColunas = [coluna.name for coluna in self.cursor.description]
        return nomesColunas