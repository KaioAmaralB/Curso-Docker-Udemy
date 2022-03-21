##Importa o Flask que seria o framework
import flask
##Importa do flask o request, json, jsonify
from flask import request, json, jsonify
##Importa o requests
import requests

##Vamos inicializar o flask
app = flask.Flask(__name__)
##Comando para ver no terminal o que ele está rodando
app.config["DEBUG"] = True

##Criando rota na API que seria o / e está usando o metódo GET(recebendo dados)
@app.route("/", methods=["GET"])
##função para receber dados
def index():
    ##pega os dados de um api pública e retorna no corpo do JSON
    data = requests.get('https://randomuser.me/api')
    return data.json()

##Configurações iniciais da API para funcionar corretamente
##Se o nome do aplicativo foi = a main irá rodar nas seguintes configurações
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="5000")