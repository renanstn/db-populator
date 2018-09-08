Populador de banco de dados
=============================

**Exemplos de uso**
1 - Instanciar o db_pupulator:
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

* Nomes simples
* Nomes completos
* Números aleatórios
* Números aleatórios dentro de uma faixa de valores
* Valores aleatórios retirados de uma coluna de uma tabela já existente
* Telefone fixo
* Celular
* CEP
* E-mail
* Data e hora
* Data
* Hora
 
Necessário um arquivo config.ini com as seguintes informações:
```
[db]
host=localhost
user=root
password=
db=teste
```
