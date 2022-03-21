<!-- Usando a estrutura HTML -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Título da estrutura HTML -->
    <title>Mensagens</title>
</head>
<body>
    <!-- Letreito maior da página web -->
    <h1> Escreva sua Mensagem! </h1>
    <!-- Formulário que vai enviar para um arquivo chamado process.php pelo método POST -->
    <form action="./process.php" method="POST">
        <!-- Input de texto com nome e valor message para escrever o queremos -->
        <input type="text" name="message" id="message">
        <!-- Input de submit e valor message para enviar o que escrevemos -->
        <input type="submit" value="Enviar Mensagem">
    </form>
</body>
</html>