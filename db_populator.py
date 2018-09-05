#!python3
# Autor: Renan Santana Desiderio
import requests, random, pymysql.cursors, configparser, datetime
from tkinter import *

class DbPopulator:

    rangeStart  = False
    rangeEnd    = False
    list        = []
    params      = {} # {'column' : 'type'}
    mass        = {} # {'column' : 'value'}
    types       = [
        'simpleName',
        'completeName',
        'randomNumber',
        'randomNumberInRange',
        'randomValueInList',
        'phoneNumber',
        'celNumber',
        'cep',
        'email',
        'dateTime',
        'date',
        'time',
    ] # Lista de tipos de dados que podem ser gerados pela classe.

    def __init__(self):
        """ Cria a conexão com o banco de dados. """

        db = self.getConfig()

        self.conexao = pymysql.connect(
            host = db['host'],
            user = db['user'],
            password = db['password'],
            db = db['db'],
            cursorclass = pymysql.cursors.DictCursor
        )

        self.cursor = self.conexao.cursor()

    def getConfig(self):
        """ Pega os dados do config.ini. """

        config = configparser.ConfigParser()
        config.read('config.ini')
        return config['db']

    def getColumnsOfTable(self):
        """ Retorna um array com os nomes das colunas de uma tabela. """

        sql = "SHOW COLUMNS FROM {}".format(self.table)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        colunas = [column.get('Field') for column in result]
        return colunas

    def getValuesFrom(self, table, column):
        """ Pega todos os dados de uma determinada coluna de uma determinada tabela. """

        sql = "SELECT {} FROM {}".format(column, table)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        valores = [i.get('idade') for i in result]
        return valores

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

    def setListOfValues(self, list):
        """ Recebe e salva uma lista de valores, para posteriormente ser usada com randomValueInList """

        self.list = list

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

        self.params[column] = type

    def setRange(self, start, end):
        """ Seta um valor inicial e um valor final, para posteriormente gerar um número dentro desta faixa. """

        self.rangeStart = start
        self.rangeEnd = end

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

    def generateValue(self, type):
        """ Recebe um tipo, e gera um valor aleatório de acordo com o mesmo. """

        if type == 'simpleName':
            return self.pessoa['nome'].split(" ")[0]

        elif type == 'completeName':
            return self.pessoa['nome']

        elif type == 'randomNumber':
            return random.randint(1, 1000)

        elif type == 'randomNumberInRange':
            if self.rangeStart and self.rangeEnd:
                return random.randint(self.rangeStart, self.rangeEnd)
            else:
                print("Range inicial / final não configurado. Configure com a função setRange(x, y).")
                exit()

        elif type == 'phoneNumber':
            return self.pessoa['telefone_fixo']

        elif type == 'celNumber':
            return self.pessoa['celular']

        elif type == 'email':
            return self.pessoa['email']

        elif type == 'date':
            return self.generateDate()

        elif type == 'cep':
            return self.pessoa['cep']

        elif type == 'time':
            return self.generateHour()

        elif type == 'dateTime':
            return "{} {}".format(self.generateDate(), self.generateHour())

        elif type == 'randomValueInList':
            if len(self.list) != 0:
                return random.choice(self.list)
            else:
                print("Lista vazia ou não definida. Defina uma lista com setListOfValues().")
                exit()

    def generateMass(self, lines):
        """ Gera a quantidade de massa informada de acordo com os parâmetros. """

        for i in range(lines):
            self.pessoa = self.generatePeople() # Gerar uma pessoa para cada linha
            for param in self.params:
                # Montar o dicionário self.mass com as {colunas : valores}
                self.mass[param] = "'{}'".format(str(self.generateValue(self.params[param])))
            self.saveData()

    def generateHour(self):
        """ Gera uma string com um horário aleatório. """

        hora = str(random.randint(0, 23))
        minuto = str(random.randint(0, 59))
        return hora + ':' + minuto + ':00'

    def generateDate(self):
        """ Gera uma data aleatória já no formato 'YYYY-MM-DD'. """

        data = datetime.datetime.strptime(self.pessoa['data_nasc'], '%d/%m/%Y')
        return data.strftime('%Y-%m-%d')

    def saveData(self):
        """ Insere os dados no banco de dados. """

        listKeys = list(self.mass.keys())
        listValues = list(self.mass.values())
        columns = ", ".join(listKeys)
        values = ", ".join(listValues)

        sql = "INSERT INTO {} ({}) VALUES ({})".format(self.table, columns, values)
        self.cursor.execute(sql)
        self.conexao.commit()
        # self.conexao.close()
