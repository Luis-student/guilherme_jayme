# conexão com o bnaco 

import mysql.connector 

banco = mysql.connector.connect(
    host= "10.30.29.162",
    port= 3309,
    user= "root",
    password= "root123",
    database= "guilherme_jayme"

)

# add tabela 
cursor = banco.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS guilherme_jayme")

# add dados na tabela
cursor.execute("""
  CREATE TABLE IF NOT EXISTS usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
     username VARCHAR(255),
     email VARCHAR(50),
     senha VARCHAR(100),
     idade INT
)
""")

# cadastro usuario 
def cadastro():
    username = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = int (input("Digite sua senha: "))
    idade = int (input("Digite sua idade: "))
    
    sql = "INSERT INTO usuario (username, email, senha, idade) VALUES (%s, %s, %s, %s)" 
    valores = (username, email, senha, idade)
    
    cursor.execute(sql, valores)
    banco.commit()
    
    print ("USUARIO CADASTRADO!!")
    
# listar usuarios 

def listar():
    cursor.execute("SELECT * FROM usuario")

    for linha in cursor.fetchall():
        print(linha)




