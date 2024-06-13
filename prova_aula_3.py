# Escreva um programa em python que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). 
# No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

numero = -1
quantidade = 0
soma = 0
media = 0

print("--------------------------------------------Início!--------------------------------------------")
print("\n\n")

print("Digite números para somar e cálcular a média arítimética até que o número digitado seja 0!")

print("\n\n")

while(numero != 0):
    numero = int(input("Digite um número: "))
    quantidade += 1
    soma += numero

media = soma / quantidade

print("\n\n")

print("-----------------------------------------------------------------------------------------------")

print("\n\n")

print(f"A quantidade de números digitados é: {quantidade}")
print(f"A soma dos números digitados é: {soma}")
print(f"A média aritimética é: {media} ")

print("\n\n")

print("----------------------------------------------Fim!----------------------------------------------")