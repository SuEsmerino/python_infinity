# 1 - Escreva um programa que solicite ao usuário um número inteiro positivo
# e realize uma contagem regressiva a partir desse número até zero,
# imprimindo cada número no processo.


# numero = int(input("Digite um número: "))

# for i in range(numero, -1, -1):
#     print(i)



# com o while dá para fazer da seguinte forma:

numero = int(input("Digite um número: "))


while numero >=0:
    print(numero)
    numero -= 1
    
# for i in range(numero, -1, -1):
#     print(i)