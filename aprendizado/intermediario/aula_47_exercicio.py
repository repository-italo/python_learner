nome = input("Digite seu nome: ")
idade = (input("Digite sua idade: "))
if idade and nome:
   print(f"Seu nome é {nome}")
   print(f"Seu nome invertido é {nome[::-1]}")
   if ' ' in nome:
      print(f"Seu nome contém espaços")
   print(f"Seu nome contém {len(nome)} caracteres")
   print(f"A primeira letra do seu nome é {nome[0]}")
   print(f"A ultima letra do seu nome é {nome[-1]}")

else:
   print("O campo esta vazio")