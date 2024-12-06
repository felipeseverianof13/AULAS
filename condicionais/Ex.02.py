#Escreva um programa que reseba uma nota de 0 a 100 e exiba uma classificaçao 
nota = int(input("Qual a sua nota? "))
if nota >= 90 and nota <= 100:
    print("excelente")
elif nota >= 70 and nota <= 89:
    print("bom")
elif nota >= 50 and nota <= 69:
    print("regular")
elif nota >= 0 and nota <= 50:
    print("ruim")
else:
    print("informe uma nota entre 0 a 100 ")
