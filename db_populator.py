#!python3
# Autor: Renan Santana Desiderio
import requests, random, pymysql.cursors, configparser
from tkinter import *

class DbPopulator:

    params = []
    types = [
        'simpleName',
        'completName',
        'randomNumber',
        'randomNumberInRange',
        'phoneNumber',
        'celNumber',
        'email',
        'dateTime',
        'date',
        'time',
    ]

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

    def generatePeople(self):
        """ Busca uma pessoa no 4devs e retorna um dict com ela. """

        idade = random.randint(18, 90)
        sexo  = random.choice(['H', 'M'])

        pessoa = requests.post('https://www.4devs.com.br/ferramentas_online.php', data = {
            'acao'      : 'gerar_pessoa',
            'idade'     : idade,
            'pontuacao' : 'S',
            'sexo'      : sexo
        })

        return pessoa.json()

    def saveData(self, data):
        """ Insere os dados no banco de dados. """

        sql = "INSERT INTO {} (nome) VALUES (%s)".format(self.table)
        self.cursor.execute(sql)
        self.conexao.commit()
        # self.conexao.close()

    def getColumnsOfTable(self):
        """ Retorna um array com os nomes das colunas de uma tabela. """

        sql = "SHOW COLUMNS FROM {}".format(self.table)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        colunas = [column.get('Field') for column in result]
        return colunas

    def setColumnType(self, column, type):
        """ Seta um campo e um tipo de dado para ser preenchido na tabela. """

        # Verificar se a coluna passada existe:
        if not column in self.getColumnsOfTable():
            print('Coluna inválida')
            return False
        # Verificar se o tipo passado é válido:
        if not type in self.types:
            print('Tipo inválido')
            return False

        self.params.append({column : type})

    def generateValue(self, type):
        """ Recebe um tipo, e gera um valor aleatório de acordo com o mesmo. """

        if type == 'simpleName':
            return self.generatePeople()['nome'].split(" ")[0]
        elif type == 'completeName':
            return self.generatePeople()['nome']
        elif type == 'randomNumber':
            return random.randint(1, 1000)
        elif type == 'randomNumberInRange':
            pass
        elif type == 'phoneNumber':
            return self.generatePeople()['telefone_fixo']
        elif type == 'celNumber':
            return self.generatePeople()['celular']
        elif type == 'email':
            return self.generatePeople()['email']
        elif type == 'date':
            return self.generatePeople()['data_nasc']