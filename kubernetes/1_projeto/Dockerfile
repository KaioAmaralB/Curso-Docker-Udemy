FROM python:3

#atualiza os repositórios e instala o pip e o python dev
RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

#defino o diretório
WORKDIR /app

#rodo a instalação do Flask
RUN pip install Flask

#copio as pasta deste projeto para o meu diretório de trabalho
COPY . .

#exponho minha porta 5000
EXPOSE 5000

#rodo o comando para executar minha aplicação
CMD ["python", "./app.py"]