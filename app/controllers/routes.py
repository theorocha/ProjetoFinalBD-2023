from flask import Flask, render_template, request, redirect
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
    

    
@app.route('/registerES', methods=['GET', 'POST'])
def registerES():
    if request.method == 'POST':
        matricula = request.form['matricula']
        try:
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()
            query = "SELECT id FROM Estudantes WHERE matricula = %s"
            cursor.execute(query, (matricula,))
            result = cursor.fetchone()
            cursor.close()
            cnx.close()
        
            if result:
                return "A matrícula já está em uso. Por favor, escolha outra matrícula."
            
            
            nome = request.form['nome']
            email = request.form['email']
            curso = request.form['curso']
            senha = request.form['senha']
            foto = request.files['foto']
            foto_data = foto.read()
            
            try:
                cnx = mysql.connector.connect(**config)
                cursor = cnx.cursor()
                query = "INSERT INTO Estudantes (nome, matricula, email, curso, senha, foto) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (nome, matricula, email, curso, senha, foto_data)
                cursor.execute(query, values)
                cnx.commit()
                cursor.close()
                cnx.close()
    
                return redirect('/login') 
    
            except mysql.connector.Error as err:
                return f"Erro de conexão ao banco de dados: {err}"
        
        except mysql.connector.Error as err:
            return f"Erro de conexão ao banco de dados: {err}"
    else:
        return render_template('registerES.html')
    

@app.route('/registerPR', methods=['GET', 'POST'])
def registerPR():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        departamento_id = request.form['departamento']
        matricula = request.form['matricula']
        
        try:
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()
            query = "INSERT INTO Professores (nome, email, departamento_id, matricula) VALUES (%s, %s, %s, %s)"
            values = (nome, email, departamento_id, matricula)
            cursor.execute(query, values)
            cnx.commit()
            cursor.close()
            cnx.close()

            return redirect('/login') 

        except mysql.connector.Error as err:
            return f"Erro de conexão ao banco de dados: {err}"

    else:
        try:
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor(dictionary=True)
            query = "SELECT id, nome FROM Departamentos"
            cursor.execute(query)
            departamentos = cursor.fetchall()
            cursor.close()
            cnx.close()

            return render_template('registerPR.html', departamentos=departamentos)

        except mysql.connector.Error as err:
            return f"Erro de conexão ao banco de dados: {err}"


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/temp')
def profOuAluno():
    return render_template('pa.html')









































































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
    

