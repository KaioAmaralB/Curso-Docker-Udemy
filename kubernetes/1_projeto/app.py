import flask
# render_template serve para renderizar uma instrução em um HTML
from flask import Flask, render_template

#instrução de inicialização do projeto
app = flask.Flask(__name__)
#para acompanhar se tiver alguma mensagem de erro
app.config["DEBUG"] = True

#definir uma rota para poder acessar do navegador
@app.route('/')
#criando a função
def index():
    #mandando uma função para ser renderizada
    return  render_template('index.html')

#função que irá fazer a incialização do meu projeto no localhost na porta que eu quiser
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port='5000')