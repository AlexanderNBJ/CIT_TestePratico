import psycopg2
import os
from Abstracts import ConectorAbstract

class Conector(ConectorAbstract):
    def __init__(self, dbname, user, password, host, port):
        try:
            self.connector = psycopg2.connect(dbname=dbname,user=user,password=password,host=host,port=port)
            self.cursor = self.connector.cursor()
        except psycopg2.OperationalError as e:
            print("A database não existe ainda. Será executado um script de criação:")
            os.system("cd ../..")
            os.system("sudo -u postgres psql < Setup/setup.sql")
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
        colunas = ""

        for i in range(0, len(atributos)-1):
            colunas+=atributos[i]+", "

        colunas+= atributos[len(atributos)-1]

        self.cursor.execute("SELECT "+colunas+" FROM "+tabela+" "+condicoes)
        return self.cursor.fetchall()
    
    def executarQueryDeDelecao(self, tabela: str, condicoes=""):
        colunas = ""

        for i in range(0, len(atributos)-1):
            colunas+=atributos[i]+", "

        colunas+= atributos[len(atributos)-1]

        self.cursor.execute("SELECT "+colunas+" FROM "+tabela+" "+condicoes)
        return self.cursor.fetchall()
    
    def executarQueryDeInsercao(self, atributos: list[str], tabela: str):
        colunas = ""

        for i in range(0, len(atributos)-1):
            colunas+=atributos[i]+", "

        colunas+= atributos[len(atributos)-1]

        self.cursor.execute("SELECT "+colunas+" FROM "+tabela+" "+condicoes)
        return self.cursor.fetchall()
    
    def executarQueryDeCommit(self):
        self.cursor.execute("COMMIT")
        return
    
    def executarQueryDeRollback(self):
        self.cursor.execute("ROLLBACK")
        return
    
    def encerrarConexao(self):
        self.connector.close()
        self.cursor.close()
        return