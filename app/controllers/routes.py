from flask import Flask, render_template
import mysql.connector
from app import app

config = {
    'user': 'root',
    'password': 'Theotheo2003@',
    'host': '192.168.0.5',
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
    

@app.route('/departamentos')
def departamentos():
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM Departamentos"
        cursor.execute(query)
        departamentos = cursor.fetchall()
        cursor.close()
        cnx.close()
        return render_template('dpt.html', departamentos = departamentos)

    except mysql.connector.Error as err:
        return f"Erro de conexão ao banco de dados: {err}"
    

@app.route('/disciplinas/<dpt_id>')
def disciplinas(dpt_id):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor(dictionary=True)
        query =  f"SELECT * FROM Disciplinas WHERE departamento_id = {dpt_id}"
        cursor.execute(query)
        disciplinas = cursor.fetchall()
        cursor.close()
        cnx.close()

        nome_departamento = obter_nome_departamento(dpt_id)

        return render_template('disciplinas.html', disciplinas = disciplinas,dpt = nome_departamento)

    except mysql.connector.Error as err:
        return f"Erro de conexão ao banco de dados: {err}"
    
    
    
@app.route('/turmas/<disciplina_id>')
def turmas(disciplina_id):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor(dictionary=True)
        query = f"SELECT t.id, t.disciplina_id, t.professor_id, p.nome AS nome_professor FROM Turmas t INNER JOIN Professores p ON t.professor_id = p.id WHERE disciplina_id = {disciplina_id}"
        cursor.execute(query)
        turmas_com_prof = cursor.fetchall()
        cursor.close()
        cnx.close()

        nome_disciplina = obter_nome_disciplina(disciplina_id)

        return render_template('turmas.html', turmas_com_prof=turmas_com_prof, disciplina=nome_disciplina)

    except mysql.connector.Error as err:
        return f"Erro de conexão ao banco de dados: {err}"

    


#################################################################################################
#################################################################################################
#################################################################################################
#################################################################################################
#Funções adicionais auxiliares
#################################################################################################
#################################################################################################
#################################################################################################

def obter_nome_departamento(departamento_id):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor(dictionary=True)
        query = f"SELECT nome FROM Departamentos WHERE id = {departamento_id}"
        cursor.execute(query)
        departamento = cursor.fetchone()
        cursor.close()
        cnx.close()
        return departamento['nome'] if departamento else None

    except mysql.connector.Error as err:
        return None
    

def obter_nome_disciplina(disciplina_id):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor(dictionary=True)
        query = f"SELECT * FROM Disciplinas WHERE id = {disciplina_id}"
        cursor.execute(query)
        disciplina = cursor.fetchone()
        cursor.close()
        cnx.close()
        return disciplina if disciplina else None

    except mysql.connector.Error as err:
        return None
    

