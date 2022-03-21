##Vamos puxar a imagem do Python 3
FROM python:3

##Nesse primeiro comando vamos atualizar todos os repositórios do pacote
##No segundo comando para instalar dois pacotes para rodar o Flask
RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

##Diretório será /app
WORKDIR /app

##Pip é o gerenciador de pacote do Python, então ele vai instalar a biblioteca Flask e requests
RUN pip install Flask requests flask_mysqldb

##Irá copiar todo esse diretório que estamos no VS Code para a imagem
COPY . .

##Exportar a porta 5000
EXPOSE 5000

##O comando que irá executar o nosso projeto CMB, que seria o arquivo app.py
CMD ["python", "./app.py"]