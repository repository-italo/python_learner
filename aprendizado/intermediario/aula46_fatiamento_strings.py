#Strings em python são iteráveis
#Dois pontos indicam fatiamento
variavel = "Ola mundo"
#0 1 2  3 4 5 6 7 8
#O l a  m u n d o
#-9 8 7 6 5 4 3 2 1
print(variavel[-3])
print(variavel[4:]) # printa todas as letras a partir do 4 a esquerda
print(variavel[-8:-3]) # fatiamento que tem o começo e o fim do trecho
print(variavel[0:9:3]) # dá pra colocar passos para seguir
print(variavel[::-1]) # String invertida
