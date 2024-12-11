# Crie um jogo onde o usuário joga contra o computador. O programa deve calcular quem ganhou cada rodada e exibir o placar final.
import random 

jogadas = ['pedra','papel','tesoura']

maquina = random.choice(jogadas)

print (" Jogo PEDRA, PAPEL E TESOURA")
escolha = input("escolha entre  'pedra', 'papel','tesoura': ")
if maquina == 'pedra' and escolha == 'papel':
    print(f" voce ganhou {escolha} ganha de {maquina}") #papel ganha pedra
elif maquina == 'papel' and escolha == 'pedra':
    print(f" voce perdeu {maquina} ganha de {escolha}") #pedra perde papel
elif maquina == 'tesoura' and escolha == 'pedra':
    print(f" voce ganhou {escolha} ganha de {maquina}")#pedra ganha tesoura
elif maquina == 'pedra' and escolha == 'tesoura':
    print(f" voce perdeu {maquina} ganha de {escolha}")#tesoura ganha pedra
elif maquina == 'papel' and escolha == 'tesoura':
    print(f" voce ganhou {escolha} ganha de {maquina}")
elif maquina == 'tesoura' and escolha == 'papel':
    print(f" voce perdeu {maquina} ganha de {escolha}")
else:
    print("empate")