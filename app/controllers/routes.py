from flask import Flask, render_template
import mysql.connector
from app import app

config = {
    'user': 'root',
    'password': 'Theotheo2003@',
    'host': '192.168.0.69',
    'database': 'trabalhobd'
}

@app.route('/')
def main():
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM Estudantes"
        cursor.execute(query)
        estudantes = cursor.fetchall()
        cursor.close()
        cnx.close()
        return render_template('extends.html', estudantes = estudantes)

    except mysql.connector.Error as err:
        return f"Erro de conexão ao banco de dados: {err}"
    
