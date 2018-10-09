Populador de banco de dados
=============================

**Exemplos de uso**

1 - Instanciar o db_populator:

`db = DbPopulator()`

2 - Setar a tabela que será populada:

`db.setTable('usuario') `

3 - Especificar a tipagem de dado que cada coluna da sua tabela irá receber:
```
db.setColumnType('nome', 'completeName')
db.setColumnType('email', 'email')
db.setColumnType('telefone', 'phoneNumber')
db.setColumnType('nascimento', 'date')
```

4- Gerar a massa.

`db.generateMass(100)`

**Tipos de dados que ele gera até o momento:**

* Nomes simples `simpleName`
* Nomes completos `completeName`
* Números aleatórios `randomNumber`
* Números aleatórios dentro de uma faixa de valores `randomNumberInRange`
    - Especificar a faixa de valores com `setRange(valor_inicial, valor_final)`
* Valores aleatórios retirados de uma coluna de uma tabela já existente
* Telefone fixo
* Celular
* CEP
* E-mail
* Data e hora
* Data
* Hora
* RG
* CPF
 
Necessário um arquivo config.ini com as seguintes informações:
```
[db]
host=localhost
user=root
password=
db=teste
```
