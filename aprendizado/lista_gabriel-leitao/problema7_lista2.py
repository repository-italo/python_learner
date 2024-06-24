class Solution:
	def __init__(self):
		self.capital = float(input())
		self.JUROS_TAXA = 0.05
		self.precisa_fiador = True and (self.capital >= 10000)
		self.juros = self.capital * self.JUROS_TAXA * 12.00
	
	def juros_calculo(self):
		print( "Voce precisa apresentar fiador" if self.precisa_fiador else "Voce nao precisa apresentar fiador")
		print("O valor dos juros para um ano e de: R$", round(self.juros, 1))

if __name__ == "__main__":
	solution = Solution()
	solution.juros_calculo()