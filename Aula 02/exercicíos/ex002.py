# #Calculadora de Média:
# Crie um programa que peça ao usuário três notas (números entre 0 e 10) e calcule a média delas. Exiba uma mensagem dizendo se o usuário foi aprovado (média maior ou igual a 7) ou reprovado (média menor que 7). 
nota1 = float(input("digite sua primeira nota: "))
nota2 = float(input("digite sua segunda nota: "))
nota3 = float(input("digite sua terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
if media >= 7 :
    print("aprovado ", media)
else :
    print("reprovado ", media)
