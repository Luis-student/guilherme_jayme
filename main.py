# conexão com o bnaco 

import mysql.connector 

banco = mysql.connector.connect(
    host= "10.30.29.162",
    port= 3309,
    user= "root",
    password= "root123"

)

# add tabela 
cursor = banco.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS guilherme_jayme")

cursor.execute("USE guilherme_jayme")

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

# deletar usuario 

def deletar():
  connect = mysql.connect('guilherme_jayme')
  cursor = connect.cursor()
  cursor.execute("DELETE FROM Usuario WHERE id = ?", (id))
  connect.commit()
  connect.close()
  print(f"USUARIO {id} FOI REMOVIDO!!!")
  
  
# login 

def login(email, senha):
  email = input("Ensira seu emial: ")
  senha = input("Ensira sua senha: ")

  sql_login = "SELECT * FROM usuario WHERE email = %s AND senha  %s"
  valores_login = (email, senha )

  cursor.execute(sql_login, valores_login)
  resultado = cursor.fetchall()

  if resultado :
    print("LOGIN REALIZADO COM SUCESSO!!!")
    print(f"Bem-vindo, {resultado[0]}")
  else:
    print("email ou senha incorreta!")


