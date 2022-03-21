#de qual imagem ele está buscando
FROM node

#qual será o diretório que irá executar a aplicação do nosso container
WORKDIR /src

#vamos copiar os arquvios para o nosso container, que seria o package.json e o package-lock.json
#o * significa que vamos pegar todos os package
#o ponto significa que estamos copiando do mesmo diretório
COPY package*.json .

#Vai rodar um npm install para instalar o projeto no container do docker
RUN npm install

#Vai copiar os demais arquivos da nossa aplicação que seria o app.js
#Pois ele irá executar toda a lógica da aplicação
# Esses dois pontos significa para copiar tudo desse diretório para o outro
COPY . .

#Expor a porta 3000
EXPOSE 3000

#Para comandos não usamos o RUN, utilizamos o CMD
#Esse comando é pra rodar o app.js
CMD ["node", "app.js"]