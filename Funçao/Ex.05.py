# Crie uma função chamada calculadora que receba três parâmetros: dois números e um operador (+, -, *, /). A função deve realizar a operação matemática correspondente e retornar o resultado.

def calc (nmr1, operacao, nmr2):
    if operacao == "+":
        print(f" {nmr1} + {nmr2} = {nmr1 + nmr2} ")
    elif operacao == "-":
        print(f" {nmr1} - {nmr2} = {nmr1 - nmr2} ")
    elif operacao == "*":
        print(f" {nmr1} * {nmr2} = {nmr1 * nmr2} ")
    elif operacao == "/":
        if nmr2 != 0:
            print(f" {nmr1} / {nmr2} = {nmr1 / nmr2} ")
        else:
            print("operacao invalida!!")
calc(5, "+", 1)