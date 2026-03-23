# conexão com o bnaco 

import mysql.connector 

banco = mysql.connector.connect(
    host= "10.30.29.162",
    port= 3309,
    user= "root",
    password= "root123"

)


cursor = banco.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS guilherme_jayme")




