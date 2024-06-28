class Solucao:
	def inverteLista(self, entrada : list) -> list:
		novaLista = []
		for i in range(len(entrada)):
			novaLista.append(0)
		for i in range(len(entrada)):
			novaLista[i] = entrada[len(entrada) - i - 1]
		return novaLista

	def entradaLista(self) -> list:
		numeros = []
		while True:
			entrada = int(input())
			if entrada == 0:
				break
			numeros.append(entrada)
		return numeros

solucao = Solucao()
lista = solucao.entradaLista()
print(solucao.inverteLista(lista))