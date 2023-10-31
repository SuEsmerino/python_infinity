# 2 - Faça um Programa que peça ao usuário um
# valor e mostre na tela se o valor é positivo ou
# negativo.

numero = float(input("Digite um número: "))

if numero > 0:
    print(f"O {numero} é positivo")
elif numero < 0:
    print(f"O {numero} é negativo")
else:
    print(f"O {numero} é neutro")