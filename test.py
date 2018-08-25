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
    teste.setColumnType('id', 'simpleName')
    print(teste.generateValue('phoneNumber'))

if __name__ == '__main__':
    main()