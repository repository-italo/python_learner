"""
DocsString
Como fazer print
"""
'''
Também é uma DocString, é usado para documentação
'''
# \r\n -> CLRF
#\N -> CF
#Comentário
nome = "Italo"
altura = 1.70
peso = 53

imc = peso / pow(altura, 2) 

formated = 'nome: {}, altura: {}, peso: {}'.format(nome, altura, peso)

print(formated)