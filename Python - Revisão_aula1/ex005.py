# 3 - Faça um Programa que imprima na tela
# "Feminino
# "
# ,
# "Masculino
# "
# ou
# "Sexo inválido
# "
# a partir
# de uma letra digitada: F ou f para feminino, M
# ou m para masculino e qualquer outra letra
# para sexo inválido.

letra = str(input("""
                  Digite uma letra:
                  F - Feminino
                  M - Masculino
                   """)).upper().strip()

if len(letra) == 1:
    match letra:
        case "F":
            print("Sexo Feminino")
        case "M":
            print("Sexo Masculino")
        case _:
            print("Sexo inválido")
else:
    print("Digite apenas uma letra")
