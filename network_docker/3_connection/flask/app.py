import flask
from flask import request, json, jsonify
import requests
import flask_mysqldb
from flask_mysqldb import MySQL

##Vamos inicializar o flask
app = flask.Flask(__name__)
##Comando para ver no terminal o que ele está rodando
app.config["DEBUG"] = True

##Configuração do banco
app.config['MYSQL_HOST'] = 'mysql_api_container'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskdocker'

##declarando para o meu mysql que ele está usando o MySQL com o app como parâmetro
mysql = MySQL(app)

##Criando rota na API que seria o / e está usando o metódo GET(recebendo dados)
@app.route("/", methods=["GET"])
##função para receber dados
def index():
    ##pega os dados de um api pública e retorna no corpo do JSON
    data = requests.get('https://randomuser.me/api')
    return data.json()

##Criando rota na API que o seria o /inserthost e está usando o método POST(inserir dados)
@app.route("/inserthost", methods=['POST'])
##Função para inserir os dados
def inserthost():
    ##Fazer uma requisição na api
    data = requests.get('https://randomuser.me/api').json()
    ##Inserir um nome de usuário, acessando o primeiro nome do primeiro usuário
    username = data['results'][0]['name']['first']

    ##Conectando no banco
    cur = mysql.connection.cursor()
    ##Executando a Query para inserir o usuário na tabela os valores que está vindo da API
    cur.execute("""INSERT INTO users(name) VALUES(%s)""", (username,))
    ##Salvar os dados que foram inseridos
    mysql.connection.commit()
    ##Fechando a conexão
    cur.close()

    ##Retorna na API o usuário do banco
    return username

##Configurações iniciais da API para funcionar corretamente
##Se o nome do aplicativo foi = a main irá rodar nas seguintes configurações
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5000")