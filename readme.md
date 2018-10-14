Populador de banco de dados
=============================

Primeiramente, inicializar o virtualenv com o seguinte comando:

`source buildVenv.sh`

Isso irá inicializar o virtualenv assim como instalar todas as dependências necessárias.

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
    - Especificar a faixa de valores **antes** com: `setRange(valor_inicial, valor_final)`
* Valores aleatórios retirados de uma coluna de uma tabela já existente:
    - Primeiro guardar os valores em uma variável com `valores = getValuesFrom(tabela, coluna)`
    - Depois usar: `setListOfValues(valores)`
    - Em seguida usar o setColumnType normalmente com o tipo: `randomValueInList`
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

Exemplo:

![exemplo](https://github.com/Doc-McCoy/db_populator/blob/master/exemplo.png)

*Este app faz consumo da API: [Random User Generator](https://randomuser.me/).*
