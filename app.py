from flask import Flask
import mysql.connector
from config import DB_CONFIG


app = Flask(__name__)


def conectar():
    return mysql.connector.connect(**DB_CONFIG)


@app.route("/")
def index():
    return """
    <h1>Sistema Biblioteca Escolar</h1>
    <p>Projeto iniciado com Python, Flask e MySQL.</p>
    <a href="/alunos">Ver alunos cadastrados</a>
    </br>
    <a href="/professores">Ver professor cadastrados</a>
    </br>
    <a href="/biblotecarios">Ver bibliotecario cadastrados</a>
    """


@app.route("/alunos")
def listar_aluno():
    try:
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)


        cursor.execute("SELECT * FROM aluno")
        alunos = cursor.fetchall()


        cursor.close()
        conexao.close()


        html = """
        <h1>Alunos Cadastrados</h1>
        <a href="/">Voltar</a>
        <br><br>


        <table border="1" cellpadding="8">
            <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>Série</th>
                <th>Turma</th>
                <th>Telefone</th>
            </tr>
        """


        for aluno in alunos:
            html += f"""
            <tr>
                <td>{aluno['id_aluno']}</td>
                <td>{aluno['nome']}</td>
                <td>{aluno['serie']}</td>
                <td>{aluno['turma']}</td>
                <td>{aluno['telefone']}</td>
            </tr>
            """


        html += "</table>"


        return html


    except Exception as erro:
        return f"Erro ao listar alunos: {erro}"





@app.route("/professores")
def listar_professor():
    try:
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)


        cursor.execute("SELECT * FROM professor")
        professores = cursor.fetchall()


        cursor.close()
        conexao.close()


        html = """
        <h1>professor Cadastrados</h1>
        <a href="/">Voltar</a>
        <br><br>


        <table border="1" cellpadding="8">
            <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>email</th>
                
                <th>Telefone</th>
            </tr>
        """


        for professor in professores:
            html += f"""
            <tr>
                <td>{professor['id_professor']}</td>
                <td>{professor['nome']}</td>
                <td>{professor['email']}</td>
        
                <td>{professor['telefone']}</td>
            </tr>
            """


        html += "</table>"


        return html


    except Exception as erro:
        return f"Erro ao listar professor: {erro}"
    

    @app.route("/bibliotecarios")
def listar_bibliotecario():
    try:
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)


        cursor.execute("SELECT * FROM bibliotecario")
        bibliotecarios = cursor.fetchall()


        cursor.close()
        conexao.close()


        html = """
        <h1>bibliotecarios Cadastrados</h1>
        <a href="/">Voltar</a>
        <br><br>


        <table border="1" cellpadding="8">
            <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>email</th>
            
            </tr>
        """


        for bibliotecario in bibliotecarios:
            html += f"""
            <tr>
                <td>{bibliotecario['id_bibliotecario']}</td>
                <td>{bibliotecario['nome']}</td>
                <td>{bibliotecario['email']}</td>
               
            </tr>
            """


        html += "</table>"


        return html


    except Exception as erro:
        return f"Erro ao listar bibliotecario: {erro}"

if __name__ == "__main__":
    app.run(debug=True)
