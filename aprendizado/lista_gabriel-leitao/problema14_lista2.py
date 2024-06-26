class Viagem:
	def __init__(self, destino):
		self.destino = destino

destinos = ["Manaus", "Sao Paulo", "Porto Alegre", "Rio de Janeiro", "Belo Horizonte"]
		
def programa ():
	print("Seja bem-vindo(a)! Viagens Gama tem algumas ofertas para voce!")
	print("Digite seu nome: ")
	nome = input()
	print("%s selecione o codigo da viagem a ser solicitada." % nome)
	for i in range(len(destinos)):
		print("%i  -  %s" % (i + 1, destinos[i]))
	
	num = int(input())
	if (num not in range(1, len(destinos) + 1)):
		print("Esta opcao nao esta incluida em nossos destinos.")
	else:
		for i in range(len(destinos)):
			if(num == i + 1):
				print("%s sua viagem para %s esta marcada." % (nome, destinos[i]))
				return destinos[i]
if __name__ == "__main__":
	destino = programa()
	viagem = Viagem(destino)