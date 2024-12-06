#  Conversor de Moedas:
# Escreva um programa que peça um valor em reais e converta para dólares. Use uma taxa de câmbio fixa e exiba o valor convertido com uma mensagem explicativa. 5,71 reais = 1 dolar

print("conversor de moedas")
reais = float(input("Qual o valor em reais? "))
cambio = 5.71
resultado = reais * cambio
print(f"o seu valor em dolares é:{resultado:.2f} ")
