# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR 5 NÚMEROS E NO FINAL MOSTRA A SOMA DOS 5 NÚMEROS DIGITADOS USANDO O FOR.

soma = 0 
for i in range(1,6):
    numero = int(input(f"Digite o {i}º número:"))
    soma = soma + numero
print(f"A soma dos valores foi: {soma}")