import requests, random, pymysql.cursors, configparser

def getConfig():
    """ Pega os dados do config """
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['db']

def generatePeople(quantidade):
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

def saveData(table, data):
    """ Insere os dados no banco de dados. """

    db = getConfig()

    conexao = pymysql.connect(
        host = db['host'],
        user = db['user'],
        password = db['password'],
        db = db['db'],
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = conexao.cursor()
    sql = "INSERT INTO {} (nome) VALUES (%s)".format(table)
    cursor.execute(sql, (data[0]['nome']))
    conexao.commit()
    conexao.close()

def getColumnsOfTable(table):
    """ Retorna um array com os nomes das colunas de uma tabela. """

    db = getConfig()

    conexao = pymysql.connect(
        host = db['host'],
        user = db['user'],
        password = db['password'],
        db = db['db'],
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = conexao.cursor()

    sql = "SHOW COLUMNS FROM {}".format(table)
    cursor.execute(sql)
    result = cursor.fetchall()
    colunas = [column.get('Field') for column in result]
    return colunas

def main():

    print("Bem vindo ao populador de banco de dados!")

    tabela = input("Qual tabela deseja popular?\n")
    colunas = getColumnsOfTable(tabela)
    print("Colunas da tabela:")
    [print(coluna) for coluna in colunas]
    campos = input("Digite as colunas que deseja popular, separadas por virgula:\n")
    campos = campos.replace(" ", "")
    colunasSelecionadas = campos.split(",")

    # quantidade  = int(input("Quantas pessoas pretende gerar?\n"))
    # gerados     = generatePeople(quantidade)
    # [print(i['nome']) for i in gerados]

    # saveData(tabela, gerados)

if __name__ == '__main__':
    main()