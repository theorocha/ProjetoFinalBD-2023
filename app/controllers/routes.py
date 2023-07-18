from flask import Flask, render_template, request, redirect, url_for, session, flash,get_flashed_messages
from flask_login import LoginManager
from functools import wraps

import mysql.connector
from app import app
app.secret_key = 'TheoS2'

config = {
    'user': 'root',
    'password': 'Theotheo2003@',
    'host': '192.168.0.5',
    'database': 'trabalhobd'
}

def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return decorated_function


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        matricula = request.form['matricula']
        senha = request.form['senha']

        if verificar_credenciais(matricula, senha):
            usuario = obter_usuario(matricula)
            session['usuario'] = usuario
            return redirect(url_for('departamentos'))
        
        else:
            mensagem = 'Matrícula ou senha inválidos. Tente novamente.'
            return render_template('login.html', mensagem=mensagem)
    return render_template('login.html')

   
    

@app.route('/departamentos')
@login_required
def departamentos():
    try:
        usuario = session['usuario']
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM Departamentos"
        cursor.execute(query)
        departamentos = cursor.fetchall()
        cursor.close()
        cnx.close()
        return render_template('dpt.html', departamentos = departamentos, usuario=usuario)

    except mysql.connector.Error as err:
        return f"Erro de conexão ao banco de dados: {err}"
    

@app.route('/disciplinas/<dpt_id>')
@login_required
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
                mensagem ='Matrícula já cadastrada. Faça Login.'
                return render_template('login.html', mensagem=mensagem)
            
            
            nome = request.form['nome']
            email = request.form['email']
            curso = request.form['curso']
            senha = request.form['senha']

            
            try:
                cnx = mysql.connector.connect(**config)
                cursor = cnx.cursor()
                query = "INSERT INTO Estudantes (nome, matricula, email, curso, senha) VALUES (%s, %s, %s, %s, %s)"
                values = (nome, matricula, email, curso, senha)
                cursor.execute(query, values)
                cnx.commit()
                cursor.close()
                cnx.close()
    
                return redirect('/') 
    
            except mysql.connector.Error as err:
                return f"Erro de conexão ao banco de dados: {err}"
        
        except mysql.connector.Error as err:
            return f"Erro de conexão ao banco de dados: {err}"
    else:
        return render_template('registerES.html')
    

@app.route('/registerPR', methods=['GET', 'POST'])
@login_required
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

            return redirect('/professores') 

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
        
@app.route('/logout')
@login_required
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/meuperfil')
@login_required
def perfil():
    return render_template('perfil.html')


@app.route('/deleteprof/<int:id>')
@login_required
def deleteProf(id):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        # Excluir turmas relacionadas ao professor
        query_turmas = "DELETE FROM Turmas WHERE professor_id = %s"
        values_turmas = (id,)
        cursor.execute(query_turmas, values_turmas)

        # Excluir o professor
        query_professores = "DELETE FROM Professores WHERE id = %s"
        values_professores = (id,)
        cursor.execute(query_professores, values_professores)

        cnx.commit()
        cursor.close()
        cnx.close()

        flash("Professor excluído com sucesso!", "success")
        return redirect(url_for('professores'))

    except mysql.connector.Error as err:
        return f"Erro ao excluir professor do banco de dados: {err}"



@app.route('/autodelete/<int:id>')
@login_required
def autoDelete(id):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        query = "DELETE FROM Estudantes WHERE id = %s"
        values = (id,)
        cursor.execute(query, values)
        cnx.commit()
        cursor.close()
        cnx.close()
        session.clear()
        return redirect(url_for('login'))
    except mysql.connector.Error as err:
        return f"Erro ao excluir estudante do banco de dados: {err}"
    

@app.route('/selfEditProfile',methods=['GET', 'POST'])
@login_required
def editProfile():
    return render_template('edit_profile.html')


@app.route('/editProf/<int:id>',methods=['GET', 'POST'])
@login_required
def editProf(id):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(dictionary=True)
    query = "SELECT id, nome FROM Departamentos"
    cursor.execute(query)
    departamentos = cursor.fetchall()
    cursor.close()
    cnx.close()
    
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(dictionary=True)
    query = "SELECT * FROM Professores WHERE id = %s"
    values = (id,)
    cursor.execute(query, values)
    professor = cursor.fetchone()
    cursor.close()
    cnx.close()
    return render_template('edit_prof.html', departamentos=departamentos, professor = professor)



@app.route('/updateProf', methods=['GET', 'POST'])
@login_required
def updateProf():
    id = request.form['id']
    nome = request.form['nome']
    email = request.form['email']
    departamento_id = request.form['departamento']
    matricula = request.form['matricula']
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        query = "UPDATE Professores SET nome = %s, email = %s, departamento_id = %s, matricula = %s WHERE id = %s"
        values = (nome, email, departamento_id, matricula, id)
        cursor.execute(query, values)
        cnx.commit()
        cursor.close()
        cnx.close()
        return redirect(url_for('professores'))
    except mysql.connector.Error as err:
        return f"Erro ao atualizar dados do professor no banco de dados: {err}"
    


@app.route('/updateProfile',methods=['GET', 'POST'])
@login_required
def updateProfile():
        nome = request.form['nome']
        email = request.form['email']
        curso = request.form['curso']
        # matricula = request.form['matricula']
        senha = request.form['senha']
        try:
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()
            query = "UPDATE Estudantes SET nome = %s, email = %s, curso = %s,  senha = %s WHERE id = %s"
            values = (nome, email, curso, senha, session['usuario']['id'])
            cursor.execute(query, values)
            cnx.commit()
            cursor.close()
            cnx.close()
            return redirect(url_for('login'))

        except mysql.connector.Error as err:
                return f"Erro ao atualizar dados do usuário no banco de dados: {err}"
    
@app.route('/professores')
@login_required
def professores():
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT p.id, p.nome AS nome_professor, d.nome AS nome_departamento FROM Professores p INNER JOIN Departamentos d ON p.departamento_id = d.id"
        cursor.execute(query)
        professores = cursor.fetchall()
        cursor.close()
        cnx.close()
        
        return render_template('prof.html', professores=professores)

    except mysql.connector.Error as err:
        return f"Erro de conexão ao banco de dados: {err}"
    
@app.route('/turmas/<disciplina_id>')
@login_required
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
    
@app.route('/avaliacoes/<int:turma_id>')
@login_required
def avaliacoes(turma_id):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor(dictionary=True)
        query = f"""
            SELECT a.id, a.nota, a.comentario, a.estudante_id AS estudante_avaliador_id, e.nome AS nome_estudante, t.id AS turma_id
            FROM Avaliacoes a
            INNER JOIN Estudantes e ON a.estudante_id = e.id
            INNER JOIN Turmas t ON a.turma_id = t.id
            WHERE a.turma_id = {turma_id}
        """

        cursor.execute(query)
        avaliacoes = cursor.fetchall()
        cursor.close()
        cnx.close()

        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor(dictionary=True)
        query_disciplina_id = f"SELECT disciplina_id FROM Turmas WHERE id = {turma_id}"
        cursor.execute(query_disciplina_id)
        disciplina_id = cursor.fetchone()['disciplina_id']

        return render_template('avaliacoes.html', avaliacoes=avaliacoes, turma_id=turma_id, disciplina = disciplina_id)

    except mysql.connector.Error as err:
        return f"Erro de conexão ao banco de dados: {err}"
    
@app.route('/formaval/<int:turma_id>')
@login_required
def formaval(turma_id):
        return render_template('formAval.html', turma_id = turma_id)

@app.route('/criaval/<int:turma_id>', methods=['GET', 'POST'])
@login_required
def criaval(turma_id):
    if request.method == 'POST':
        nota = request.form['nota']
        comentario = request.form['comentario']
        estudante_id = session['usuario']['id']
        
        try:
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()
            query = "INSERT INTO Avaliacoes (estudante_id, turma_id, nota, comentario) VALUES (%s, %s, %s, %s)"
            values = (estudante_id, turma_id, nota, comentario)
            cursor.execute(query, values)
            cnx.commit()
            cursor.close()
            cnx.close()
            
            return redirect(url_for('avaliacoes', turma_id=turma_id))
        
        except mysql.connector.Error as err:
            return f"Erro ao cadastrar avaliação: {err}"
    
    return redirect(url_for('avaliacoes', turma_id=turma_id))

@app.route('/minhasavaliacoes')
@login_required
def minhasAvaliacoes():
    try:
        estudante_id = session['usuario']['id']
        
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor(dictionary=True)
        
        query = f"""
            SELECT a.id, a.nota, a.comentario, t.id AS turma_id, d.nome AS nome_disciplina
            FROM Avaliacoes a
            INNER JOIN Turmas t ON a.turma_id = t.id
            INNER JOIN Disciplinas d ON t.disciplina_id = d.id
            WHERE a.estudante_id = {estudante_id}
        """
        
        cursor.execute(query)
        avaliacoes = cursor.fetchall()
        
        cursor.close()
        cnx.close()
        
        return render_template('minhasAvaliacoes.html', avaliacoes=avaliacoes)
    
    except mysql.connector.Error as err:
        return f"Erro de conexão ao banco de dados: {err}"

@app.route('/excluiraval/<int:id>')
@login_required
def excluiraval(id):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        query = "DELETE FROM Avaliacoes WHERE id = %s"
        values = (id,)
        cursor.execute(query, values)
        cnx.commit()
        cursor.close()
        cnx.close()
        
        return redirect(url_for('minhasAvaliacoes'))
    
    except mysql.connector.Error as err:
        return f"Erro ao excluir avaliação: {err}"

@app.route('/editaval/<int:id>', methods=['GET', 'POST'])
@login_required
def editaval(id):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM Avaliacoes WHERE id = %s"
        values = (id,)
        cursor.execute(query, values)
        avaliacao = cursor.fetchone()
        cursor.close()
        cnx.close()
        
        if request.method == 'POST':
            nota = request.form['nota']
            comentario = request.form['comentario']
            
            try:
                cnx = mysql.connector.connect(**config)
                cursor = cnx.cursor(dictionary=True)
                query = "UPDATE Avaliacoes SET nota = %s, comentario = %s WHERE id = %s"
                values = (nota, comentario, id)
                cursor.execute(query, values)
                cnx.commit()
                cursor.close()
                cnx.close()
                
                return redirect(url_for('minhasAvaliacoes'))
            
            except mysql.connector.Error as err:
                return f"Erro ao editar avaliação: {err}"
        
        return render_template('editaval.html', avaliacao=avaliacao)
    
    except mysql.connector.Error as err:
        return f"Erro ao editar avaliação: {err}"
    


@app.route('/denunciar/<int:id>', methods=['GET', 'POST'])
@login_required
def denunciar(id):
    if request.method == 'POST':
        motivo = request.form['motivo']
        estudante_id = session['usuario']['id']

        try:
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()

            query_avaliacao = "SELECT turma_id FROM Avaliacoes WHERE id = %s"
            cursor.execute(query_avaliacao, (id,))
            turma_id = cursor.fetchone()[0]

            
            query_denuncia = "INSERT INTO Denuncias (avaliacao_id, estudante_id, motivo) VALUES (%s,  %s, %s)"
            values = (id, estudante_id, motivo)
            cursor.execute(query_denuncia, values)

            cnx.commit()
            cursor.close()
            cnx.close()
            return redirect(url_for('avaliacoes', turma_id=turma_id))

        except mysql.connector.Error as err:
            return f"Erro ao denunciar avaliação: {err}"

    return render_template('denunciar.html', id=id)


@app.route('/alld')
@login_required
def alld():
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor(dictionary=True)
        query = """
            SELECT d.id, d.motivo, a.comentario, a.id AS avaliacao_id, a.estudante_id, e.nome AS nome_estudante
            FROM Denuncias d
            INNER JOIN Avaliacoes a ON d.avaliacao_id = a.id
            INNER JOIN Estudantes e ON d.estudante_id = e.id
        """

        cursor.execute(query)
        denuncias = cursor.fetchall()
        cursor.close()
        cnx.close()

        return render_template('alld.html', denuncias=denuncias)

    except mysql.connector.Error as err:
        return f"Erro de conexão ao banco de dados: {err}"
    
@app.route('/ignorar_denuncia/<int:id>', methods=['GET', 'POST'])
@login_required
def ignorar_denuncia(id):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        query = "DELETE FROM Denuncias WHERE id = %s"
        values = (id,)
        cursor.execute(query, values)
        cnx.commit()
        cursor.close()
        cnx.close()

        flash("Denúncia ignorada com sucesso!", "success")
        return redirect(url_for('alld'))

    except mysql.connector.Error as err:
        return f"Erro ao ignorar denúncia: {err}"



@app.route('/apagar_avaliacao/<int:id>')
@login_required
def apagar_avaliacao(id):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        
        query_denuncias = "DELETE FROM Denuncias WHERE avaliacao_id = %s"
        values_denuncias = (id,)
        cursor.execute(query_denuncias, values_denuncias)

        
        query_avaliacao = "DELETE FROM Avaliacoes WHERE id = %s"
        values_avaliacao = (id,)
        cursor.execute(query_avaliacao, values_avaliacao)

        cnx.commit()
        cursor.close()
        cnx.close()

        flash("Avaliação excluída com sucesso!", "success")
        return redirect(url_for('alld'))

    except mysql.connector.Error as err:
        return f"Erro ao apagar avaliação: {err}"



@app.route('/apagar_usuario/<int:id>', methods=['GET', 'POST'])
@login_required
def apagar_usuario(id):
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        # Excluir denúncias relacionadas às avaliações do estudante
        query_denuncias = """
            DELETE d FROM Denuncias d
            INNER JOIN Avaliacoes a ON d.avaliacao_id = a.id
            WHERE a.estudante_id = %s
        """
        values_denuncias = (id,)
        cursor.execute(query_denuncias, values_denuncias)

        # Excluir avaliações do estudante
        query_avaliacoes = "DELETE FROM Avaliacoes WHERE estudante_id = %s"
        cursor.execute(query_avaliacoes, values_denuncias)

        # Excluir o estudante
        query_estudantes = "DELETE FROM Estudantes WHERE id = %s"
        cursor.execute(query_estudantes, values_denuncias)

        cnx.commit()
        cursor.close()
        cnx.close()

        flash("Usuário apagado com sucesso!", "success")
        return redirect(url_for('alld'))

    except mysql.connector.Error as err:
        return f"Erro ao apagar usuário: {err}"









    

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



def verificar_credenciais(matricula, senha):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = "SELECT * FROM Estudantes WHERE matricula = %s AND senha = %s"
    values = (matricula, senha)
    cursor.execute(query, values)
    result = cursor.fetchone()
    cursor.close()
    cnx.close()
    return result is not None


def obter_usuario(matricula):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(dictionary=True)
    query = "SELECT * FROM Estudantes WHERE matricula = %s"
    values = (matricula,)
    cursor.execute(query, values)
    usuario = cursor.fetchone()
    cursor.close()
    cnx.close()
    return usuario




    

    

    


