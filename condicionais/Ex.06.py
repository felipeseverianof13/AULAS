# 6. Comparação de Dois Números:
# Peça ao usuário dois números e verifique qual é o maior. Exiba uma mensagem indicando o maior número ou se são iguais.
print("comparador de numeros")
Nmr1 = int(input("Qual o seu primeiro numero? "))
Nmr2 = int(input("Qual o seu segundo numero? "))
if Nmr1 > Nmr2 :
    print("o nomero maior é", Nmr1)
elif Nmr2 > Nmr1 :
    print("o numero maior é", Nmr2)
else :
    print("os numeros sao iguais!! ")