#!python3
# Autor: Renan Santana Desiderio
import requests, random, pymysql.cursors, configparser
from tkinter import *

class DbPopulator:

    def __init__(self):
        """ Cria a conexão com o banco de dados """

        db = self.getConfig()

        self.conexao = pymysql.connect(
            host = db['host'],
            user = db['user'],
            password = db['password'],
            db = db['db'],
            cursorclass = pymysql.cursors.DictCursor
        )

        self.cursor = self.conexao.cursor()

    def setTable(self, table):
        """ Seta uma tabela para ser populada. """

        # Verificar se a tabela passada existe
        sql = "SHOW TABLES LIKE '{}'".format(table)
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        if result:
            self.table = table
        else:
            print("A tabela digitada não existe no banco de dados.")

    def getConfig(self):
        """ Pega os dados do config """

        config = configparser.ConfigParser()
        config.read('config.ini')
        return config['db']

    def generatePeople(self, quantidade):
        """ Busca pessoas no 4devs e retorna um dict com elas. """

        gerados = []

        for i in range(quantidade):

            idade   = random.randint(18, 90)
            sexo    = random.choice(['H', 'M'])

            pessoa = requests.post('https://www.4devs.com.br/ferramentas_online.php', data = {
                'acao'      : 'gerar_pessoa',
                'idade'     : idade,
                'pontuacao' : 'S',
                'sexo'      : sexo
            })

            gerados.append(pessoa.json())

        return gerados

    def saveData(self, data):
        """ Insere os dados no banco de dados. """

        sql = "INSERT INTO {} (nome) VALUES (%s)".format(self.table)
        self.cursor.execute(sql, (data[0]['nome']))
        self.conexao.commit()
        # self.conexao.close()

    def getColumnsOfTable(self):
        """ Retorna um array com os nomes das colunas de uma tabela. """

        sql = "SHOW COLUMNS FROM {}".format(self.table)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        colunas = [column.get('Field') for column in result]
        return colunas
