# 5 - Faça um programa para a leitura de quatro
# notas de um aluno. O programa deve calcular a
# média alcançada apresentar:

# a. par ou ímpar;
# b. positivo ou negativo;

# a. A mensagem

# "Aprovado
# "
# , se a média alcançada for

# maior ou igual a sete;
# b. A mensagem

# "Reprovado
# "
# , se a média for menor

# do que sete;
# c. A mensagem

# "Aprovado com Distinção
# "
# , se a média

# for igual a dez.


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7 and media < 10:
    print("Aprovado")
elif media < 7 and media >= 0:
    print("Reprovado")
elif media == 10:
    print("Aprovado com distinção")
else:
    print("Média inválida, digite notas entre 0 e 10")