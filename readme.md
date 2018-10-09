Populador de banco de dados
=============================

**Exemplos de uso**

1 - Instanciar o db_populator:

`db = DbPopulator()`

2 - Setar a tabela que será populada:

`db.setTable('usuario') `

3 - Especificar a tipagem de dado que cada coluna da sua tabela irá receber com o comando `setColumnType(coluna, tipo)`:
```
db.setColumnType('nome', 'completeName')
db.setColumnType('email', 'email')
db.setColumnType('telefone', 'phoneNumber')
db.setColumnType('nascimento', 'date')
```

4- Gerar a massa.

`db.generateMass(100)`

**Tipos de dados que ele gera até o momento:**

* Nomes simples: `simpleName`
* Nomes completos: `completeName`
* Números aleatórios: `randomNumber`
* Números aleatórios dentro de uma faixa de valores: `randomNumberInRange`
    - Especificar a faixa de valores com: `setRange(valor_inicial, valor_final)`
* Valores aleatórios retirados de uma coluna de uma tabela já existente:
    - Primeiro guardar os valores em uma variável com `valores = getValuesFrom(tabela, coluna)`
    - Depois usar: `setListOfValues(valores)`
    - Em seguida usar o setColumnType normalmente com: `randomValueInList`
* Telefone fixo: `phoneNumber`
* Celular: `celNumber`
* CEP (atualmente vindo no formato americano): `cep`
* E-mail: `email`
* Data e hora: `dateTime`
* Data: `date`
* Hora: `time`
 
Necessário um arquivo config.ini com as seguintes informações do banco mySQL:
```
[db]
host=localhost
user=root
password=
db=teste
```
