#Formatação de números

#(caractere)> - adiciona caracteres a esquerda
#(caractere)< - adiciona caracteres a direita
#
#
variavel = 150
print(f"{variavel}")
print(f"{variavel: >10}") # adiciona ' ' a esquerda 10 vezes
print(f"{variavel: <10}") # adiciona ' ' a direita 10 vezes
print(f"{variavel: ^10}") # centraliza o numero e adiciona metade dos espaços dos lados
print(f"{1000.79859785735:0=+10,.1f}") # faz mt coisa adiciona o sinal do número e arredonda para uma casa decimal
print(f"O hexadecimal de 1500 é {1500:08X}") # deixa no formato de 8 caracteres de hexadecimal
print(f"{variavel!r}") # Conversion flags