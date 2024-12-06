# Crie uma função chamada par_ou_impar que receba um número e imprima "Par" se o número for par e "Ímpar" se for ímpar. o numero deve ser fornecido pelo usuario.

numero = int(input("digite o numero: "))
def par_ou_impar (numero):
    if numero % 2 == 0:
        print(f"o numero {numero} é par")
    else:
        print(f"o numero {numero} é impar")
par_ou_impar(numero)
