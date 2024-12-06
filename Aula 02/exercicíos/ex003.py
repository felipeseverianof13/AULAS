# #Conversor de Temperatura Crie um programa que converta uma temperatura de Celsius para Fahrenheit ou de Fahrenheit para Celsius, dependendo da escolha do usuário. 
# As fórmulas são:Fahrenheit para Celsius: 
# 𝐶 = (𝐹 − 32) × 5 / 9
# Celsius para Fahrenheit: 
# 𝐹 = 𝐶 × 9 / 5 + 32

escolha = input("escolha entre _celsius_ ou _fahreheit_: ")

if escolha == "celsius" :
    graus = float(input("digite quantos fahreheit: "))
    celsius = (graus - 32) * 5 / 9
    print(" a conversao de fahreheit pra celsius é: ", celsius)
elif escolha == "fahreheit" :
    graus = float(input("digite quantos celsius: "))
    fahreheit = graus * 9 / 5 + 32
    print(" a conversao de celsius pra fahreheit é: ", fahreheit)
else :
    print("escolha invalida!!! ")
