# FAÇA UM PPROGRAMA QUE PEDE PARA O USUÁRIO ESCREVER O SEU NOME E MOSTRE NA TELA QUANTAS LETRAS "A" EXISTEM NO NOME DIGITADO.

palavra = str(input("Digite o seu nome: ")).title()
contador = 0

for letra in palavra:
    if letra in "a":
        contador += 1

print(f"O nome {palavra} possui {contador} letras 'A'. ")



# outro modo, para poder apenas conferir o texto, mas não modificiar o que foi digitado.

# CONTADOR DE LETRAS A:
# nome = str(input("Digite o seu nome: "))

# contador = 0

# for letra in nome:
#     if letra.lower() == 'a':
#         contador += 1
    
# print(f"O nome {nome} possui {contador} letras 'a'")