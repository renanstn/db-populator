from db_populator import *

def main():

    teste = DbPopulator()

    # Setar a tabela que será populada
    teste.setTable('usuario')
    # Descobrir as colunas da tabela
    # colunas = teste.getColumnsOfTable()
    # [print(coluna) for coluna in colunas]
    # Função que gera as pessoas
    # gerados = teste.generatePeople(4)
    # [print(i['nome']) for i in gerados]
    # print(teste.generateValue('phoneNumber'))
    # print(teste.generateValue('completeName'))
    # print(teste.generateValue('date'))
    # teste.setColumnType('nome', 'completeName')
    # teste.setColumnType('cep', 'cep')
    # teste.setColumnType('numero', 'randomNumber')
    # teste.setColumnType('email', 'email')
    # teste.setColumnType('dia_hora', 'dateTime')
    # teste.setColumnType('dia', 'date')
    # teste.setColumnType('telefone', 'phoneNumber')
    # teste.setColumnType('celular', 'celNumber')
    # teste.setColumnType('dia_hora', 'dateTime')
    # teste.setRange(1, 5)
    teste.setColumnType('numero', 'randomNumberInRange')
    teste.generateMass(5)

if __name__ == '__main__':
    main()