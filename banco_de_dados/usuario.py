import sqlite3  # Importa o módulo sqlite3 para trabalhar com bancos de dados SQLite

# Conectar ao banco de dados
conn = sqlite3.connect('cadastro.db')  # Conecta ao banco de dados chamado 'cadastro.db'. Se não existir, ele será criado.
cursor = conn.cursor()  # Cria um cursor, que será usado para executar comandos SQL no banco.

# Criar a tabela (caso ainda não exista)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID único e incremental para cada usuário
        nome TEXT NOT NULL,                    -- Coluna 'nome' do tipo texto, não pode ser nulo
        idade INTEGER NOT NULL                 -- Coluna 'idade' do tipo inteiro, não pode ser nula
    )
''')  # Executa um comando SQL para criar a tabela 'usuarios', garantindo que ela só será criada se ainda não existir.

# Função para cadastrar um novo usuário
def cadastrar_usuario(nome, idade):
    try:
        cursor.execute('''
            INSERT INTO usuarios (nome, idade)
            VALUES (?, ?)
        ''', (nome, idade))  # Insere os valores de 'nome' e 'idade' na tabela 'usuarios' usando placeholders (?, ?).
        conn.commit()  # Salva as alterações no banco de dados.
        print(f"Usuário {nome} cadastrado com sucesso!")  # Confirmação de que o usuário foi cadastrado.
    except Exception as e:  # Captura erros que possam ocorrer.
        print(f"Erro: {e}")  # Exibe a mensagem de erro caso algo dê errado.

# Lista para armazenar os nomes dos usuários cadastrados
lista = []  # Inicializa uma lista vazia para guardar os nomes dos usuários cadastrados.

# Solicitar os dados do usuário
while True:  # Inicia um loop infinito para permitir o cadastro de múltiplos usuários.
    print("Cadastro de usuário")  # Exibe uma mensagem inicial para o cadastro.
    nome = input("Digite o nome do usuário: ")  # Solicita o nome do usuário.
    idade = int(input("Digite a idade do usuário: "))  # Solicita a idade do usuário e converte para inteiro.
    lista.append(nome)  # Adiciona o nome do usuário à lista 'lista'.
    # Cadastrar o usuário
    cadastrar_usuario(nome, idade)  # Chama a função 'cadastrar_usuario' para inserir os dados no banco.
    pergunta = input("Cadastrar novo usuário? (s/n) ").lower()  # Pergunta se deseja cadastrar outro usuário.
    if pergunta != "s":  # Se a resposta for diferente de "s" (sim), o loop é encerrado.
        break  # Sai do loop.

# Exibir os usuários cadastrados
print("Todos usuários cadastrados")  # Mensagem final.
print(lista)  # Exibe a lista de nomes de usuários cadastrados.

# Fechar a conexão
conn.close()  # Fecha a conexão com o banco de dados, liberando recursos.
