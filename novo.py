import sqlite3

# Conectar ao banco de dados (será criado se não existir)
conexao = sqlite3.connect('meu_banco_de_dados.db')

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Criar uma tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        cidade TEXT NOT NULL
    )
''')

# Inserir dados na tabela
nome = 'Paula'
idade = 30
cidade = 'São Paulo'
cursor.execute('''
    INSERT INTO pessoas (nome, idade, cidade)
    VALUES (?, ?, ?)
''', (nome, idade, cidade))

# Confirmar a transação
conexao.commit()

# Consultar dados da tabela
cursor.execute('SELECT * FROM pessoas')
pessoas = cursor.fetchall()

# Mostrar os dados consultados
for pessoa in pessoas:
    print(f'ID: {pessoa[0]}, Nome: {pessoa[1]}, Idade: {pessoa[2]}, Cidade: {pessoa[3]}')

# Fechar a conexão
conexao.close()
