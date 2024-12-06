#Crie um jogo de adivinhação onde o usuário tem que adivinhar um número entre 1 e 20. O usuário tem apenas 5 tentativas para acertar. Ao final, informe se ele acertou ou perdeu. 
# Utilize a biblioteca random para gerar o número aleatório (random, randint)
import random

numero_aleatorio = random.randint(1,20)
numero_tentativas = 5
numero = int(input("Digite um numero entre 1 a 20: "))

while numero_tentativas > 0:
    numero_tentativas = numero_tentativas - 1
    if numero == numero_aleatorio:
        print(f" voce acertou, o numero correto é: {numero_aleatorio}")
        break
    elif numero_tentativas == 0:
        print("acabou as tentativas ")
        break
    elif numero > numero_aleatorio:
        print(f" o numero correto é menor que: {numero} o seu numero de tentativas sao: {numero_tentativas}")
        numero = int(input("Digite um numero entre 1 a 20: "))
    elif numero < numero_aleatorio:
        print(f" o numero correto é maior que: {numero} o seu numero de tentativas sao: {numero_tentativas} ")
        numero = int(input("Digite um numero entre 1 a 20: "))
 
