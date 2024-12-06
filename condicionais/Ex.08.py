# 8. Calculadora de Preço com Desconto:
# Peça ao usuário o preço de um produto e a porcentagem de desconto. Calcule e exiba o preço final do produto após o desconto.

print("calculadora de preço com desconto")
preço = float(input("qual o preço do produto? "))
desconto = float(input("qual o valor de desconto? "))/100
resultado = preço * desconto
valor = preço - resultado 
print(f"o seu desconto ficou no valor de {resultado}")
print(f"o seu valor final com desconto é de: {valor}")