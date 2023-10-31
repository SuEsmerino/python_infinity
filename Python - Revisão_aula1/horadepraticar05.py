# 5 - Hora de otimizar a questão número 3, após ter criado seu programa que
# conta quantas vogais existem numa frase, implemente mais uma
# funcionalidade. O programa agora deve imprimir a quantidade de vogais e
# consoantes encontradas.



frase = str(input("Digite uma frase: "))
contador_de_vogal = 0
contador_de_consoante = 0

for letra in frase:
    if letra.lower() in "aeiouâáêéîíôóúã":
        contador_de_vogal += 1
    if letra.lower() in "bcdfghjkmlnpqrstvxywz":
        contador_de_consoante += 1


print(f"A frase digitada possui {contador_de_vogal} vogais e {contador_de_consoante} consoantes. ")

