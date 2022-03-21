//chamando o framework que acabou de instalar
const express = require ('express')
//inicializando o express
const app = express()
//criando a porta da aplicação
const port = 3000

//aqui criamos o get para acessar o / da nossa aplicação e vai nos retornar uma requisição ou resposta
//são paramâmetros utilizados pelo express
app.get('/', (req, res) => {
    //mensagem de sucesso que será exibida na web
    res.send('Olá minha imagem')
})

//porta que vai estar escutando
app.listen(port, () => {
    //irá nos retornar a porta que o container estará executando
    console.log(`Executando na porta: ${port}`)
});