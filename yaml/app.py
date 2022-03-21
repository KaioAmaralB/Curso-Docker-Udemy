import yaml

##Se nome for igual a main
if __name__ == '__main__':

    ##Vamos abrir um arquivo, ele irá ler
    stream = open("test.yaml", "r")
    ##Vamos criar um dicionário com esses valores
    dictionary = yaml.safe_load(stream)

    ##Para cada chave/valor nos itens do dicionário, imprimir com o :
    for key, value in dictionary.items():
        print(key + " : " + str(value))