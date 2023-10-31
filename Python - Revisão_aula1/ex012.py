# FAÇA UM PROGRAMA QUE PEDE PARA O USÚARIO ESCREVER O NOME DE UMA FRUTA E QUE FIQUE EM UM LOOP INFINITO ATÉ O USUÁRIOS ESCREVER "FIM" NO LUGAR DO NOME DA FRUTA.

while True:
    fruta = str(input("Digite o nome de uma fruta: "))

    if fruta.lower() == "fim":
        break