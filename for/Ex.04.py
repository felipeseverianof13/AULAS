# peça ao usuario para escolher um numero e exiba a tabuada desse numero de 1 a 10. (for)

numero = int(input(" escreva um numero: "))
for var in range(1,11):
    print(f" {numero} X {var}: {numero * var}")
    