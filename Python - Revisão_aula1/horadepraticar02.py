# 2 - Escreva um programa que solicite ao usuário um número inteiro e
# imprima a tabuada desse número, de 1 a 10.


# tabuada=int(input("Digite um número e vamos ver a tabuada:  "))

# for count in range(10):
#     print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )



# TAMBÉM PODE SER FEITO ASSIM:

numero = int(input("Digite um número: "))

for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")