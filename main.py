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


