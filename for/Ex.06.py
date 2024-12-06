# crie um programa que peça ao usuario para inserir um numero inteiro possitivo e, usando um loop for, calcule o favorial desse numero (for)
numero = 1
fatorial = 1
while numero != 0:
    numero = int(input("digite o seu numero: "))
    fatorial = 1
    if numero != 0:
        for var in range(1, numero+1):
            fatorial = fatorial * var
            # print(f" o fatorial de {numero} é {fatorial}")
        print(f'o fatorial do número {numero} é: {fatorial}')