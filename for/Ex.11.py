#crie um programa que defina um texto, e ultilizando (for) conte quantas vezes A aparece no texto

# Definindo a string 'texto' que será analisada
texto = "a dona aranha caiu pela parede veio a chuva fraca e a levantou"

# Inicializando a variável 'contar' para contar quantas vezes a letra 'a' aparece no texto
contar = 0

# Iniciando um loop para percorrer cada caractere da string 'texto'
for var in texto:
    
    # Verificando se o caractere atual é a letra 'a'
    if var == "a":
        
        # Se for, incrementa o contador 'contar' em 1
        contar = contar + 1

# Imprime o valor final de 'contar', que é o número de ocorrências da letra 'a' no texto
print(contar)

