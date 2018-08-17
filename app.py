import requests, random, pprint

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

def saveData(data):
    """ Insere os dados no banco de dados. """
    pass

def main():

    print("Bem vindo ao populador de banco de dados!")
    quantidade = int(input("Quantas pessoas pretende gerar?\n"))
    gerados = generatePeople(quantidade)
    [print(i['nome']) for i in gerados]

if __name__ == '__main__':
    main()