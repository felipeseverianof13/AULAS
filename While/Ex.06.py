#escreva um programa que pede ao usuario para advinhar um numero secreto entre 1 e 10. o programa deve continuar pedindo ate que o numero correto seja advinhado.

numero_secreto = 2

print(" advinhe o numero secreto entre 1 a 10...")
numero = int(input(" qual numero que voçe acha que é o numero secrero? "))
while numero != numero_secreto:
    numero = int(input(" qual numero que voçe acha que é o numero secrero? "))

print(f"parabens, voçe acertou o numero secreto, o numero era {numero_secreto}")
