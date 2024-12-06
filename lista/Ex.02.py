#crie um programa que peça ao usuario uma lista de compras. o usuario deve adcionaar um elemento por vez na lista. o programa acaba quando o usuario escrever a palavra sair.

lista = []
elementos = (input(" adicione os elementos a sua lista de compras... caso tenha acabado digite  #sair# "))
while elementos != "sair":
    lista.append(elementos)
    elementos = (input(" adicione os elementos a sua lista de compras... caso tenha acabado digite  #sair# "))

print(lista)