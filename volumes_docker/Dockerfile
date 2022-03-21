#Usando o php na versão 8 com a tag apache pois já vem instalado junto
FROM php:8-apache

#O diretório da aplicação
WORKDIR /var/www/html/

#Vou copiar todos so arquivos presente nessa pasta do VS Code para a imagem
COPY . .

#Exposta na porta 80
EXPOSE 80

#Executar um comando para dar a permissão que todos os arquivos que vai executar
#Dar permissão para um usuário X: para um grupo X e no diretório X
RUN chown -R www-data:www-data /var/www