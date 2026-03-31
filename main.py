from flask import Flask, jsonify, request 
app = Flask(__name__)


import mysql.connector 

banco = mysql.connector.connect(
    host= "10.30.29.100",
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
@app.route('/cadastro', methods = ['POST'])
def criar ():
    dados = request.json
    print(request.remote_addr)
    user_name = dados['user_name']
    email = dados["email"]
    idade = dados["idade"]
    senha = dados["senha"]

    cadastro(user_name, email, idade, senha)

    return jsonify(dados)


#Cadastro 
def cadastro(username, email, idade, senha):
    cursor.execute(f"INSERT INTO usuario (username, email, senha, idade) VALUES ('{username}', '{email}', '{senha}', {idade})")
    banco.commit()
    
    print ("USUARIO CADASTRADO!!")
   

@app.route("/", methods = ["GET"])
def padrao():
  print(request.remote_addr)
  return "<h1>Bem Vindo!"


# listar usuarios 
@app.route('/usuario', methods = ['GET'] )
def listar():
  cursor.execute("SELECT * FROM usuario")

  usuario = cursor.fetchall()
  return jsonify(usuario)


# deletar usuario 
@app.route('/deletar', methods = ["DELETE"])
def deletar():
  id_usuario = int(input("Insira o ID para deletar: "))

  cursor.execute(f"SELECT * FROM usuario WHERE id = {id_usuario}")
  usuario = cursor.fetchone()

  if usuario:
    cursor.execute(f"DELETE FROM usuario WHERE id = {id_usuario}")
    banco.commit()

    return jsonify('Usuario cadastrado com sucesso !!!')
  

# login 

def login():
  email = input("Ensira seu email: ")
  senha = input("Ensira sua senha: ")

  sql_login = "SELECT * FROM usuario WHERE email = %s AND senha = %s"
  valores_login = (email, senha)

  cursor.execute(sql_login, valores_login)
  resultado = cursor.fetchone()

  if resultado:
    print("LOGIN REALIZADO COM SUCESSO!!!")
    print(f"Bem-vindo, {resultado[1]}")
  else:
    print("email ou senha incorreta!")

# MENU de inicio
def menu():
  while True:
    
    print ("========== MENU ==========")
    print ("1- Inserir Dados")
    print ("2- Listar Usuario")
    print ("3- Deletar Usuario")
    print ("4- Login")
    print ("5- SAIR")
    
    opcao = input("Insira uma das opçoes acima : ")
    
    if opcao == "1":
      cadastro()
    elif opcao == "2":
      listar()
    elif opcao == "3":
      deletar()
    elif opcao == "4":
      login()
    elif opcao == "5":
      print ("VOÇÊ SAIU DO SISTEMAS!") 
      break
    else:
      print ("OPÇÃO NÃO VALIDA")  

#chamar função 
#menu()

app.run(port=3007, host='localhost', debug=True)