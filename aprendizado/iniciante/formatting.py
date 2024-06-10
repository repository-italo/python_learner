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
formatted_percent = 'nome: %s, altura: %.2f, peso: %.2f e imc: %.2f' % (nome, altura, peso, imc) # Se fosse só uma variável, 
formatted_f = f"nome: {nome}, altura: {altura:.2f}, peso: {peso:.2f} e imc: {imc:.2f}" #seria apenas a variável sem acento
print(formatted_f)