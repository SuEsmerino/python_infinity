# 3 - Escreva um programa que solicite ao usuário uma frase e conte
# quantas vogais (a, e, i, o, u) existem nessa frase.

palavra = str(input("Digite uma frase: ")).lower()
contador = 0

for letra in palavra:
    if letra in "aeiouáéãô":
        contador += 1

print(f"A frase {palavra} possui {contador} vogais.")