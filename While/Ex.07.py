# faça um programa que peça ao usuario uma senha e continue pedindo ate que ele insira a senha correta (1234) correta
senha_correta = 1234
senha = int(input(" Qual a senha do cofre? "))
while senha != senha_correta:
    print(" sua senha esta incorreta, tente novamente. ")
    senha = int(input(" Qual a senha do cofre? "))
print(f"senha correta. {senha_correta}")