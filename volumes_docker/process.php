<?php
//Irá pegar a mensagem lá do POST que estou enviando por formulário
 $message = $_POST["message"];

 //Pegando o nosso diretório de messages para armazenar esses txts
 $files = scandir('./messages');

//Verificando de números de arquivos, para anexar nomes únicos de acordo com
//O total de arquivos criados
 $num_files = count($files) - 2; // . e ..

 //Ele irá dar um nome par ao arquivos, de acordo com o contador de arquivos criados
 $fileName = "msg-{$num_files}.txt";

//Abrir o arquivos criado nesse diretório message
 $file = fopen("./messages/{$fileName}", "x");

 //Escrever no arquivo a mensagem enviamos pelo post
 fwrite($file, $message);

 //Fechar o arquivo
 fclose ($file);
 
 //Voltar para o formulário depois que terminar todo o processo
 header("Location: ./index.php");
 ?>