# faça um programa que peça ao usuario um numero e imprima os numeros pares de 1 ate o numero escolhido (for)
numero = int(input(" digite o numero: "))
for var in range(1,numero+1):
    if var % 2 == 0:
        print(var)