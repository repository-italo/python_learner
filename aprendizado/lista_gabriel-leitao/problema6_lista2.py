class Solution:
	def __init__(self):
		self.entrada = int(input())
		self.resposta = []
	
	def gerar_lista(self):
		while self.entrada > 0:
			self.entrada = self.entrada - 1
			self.resposta.append(self.entrada)
			self.resposta.sort()
		return self.resposta


if __name__ == "__main__":
   solution = Solution()
   print(solution.gerar_lista())