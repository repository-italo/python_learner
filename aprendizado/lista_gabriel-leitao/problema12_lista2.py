class Solution:
	def __init__(self):
		self.acertos = eval(input())
	def pontos(self) -> int:
		if (len(self.acertos) < 4):
			raise Exception("erro")
		pontos = self.acertos.count(1) * 80 + self.acertos.count(2) * 40 + self.acertos.count(3) * 20 + self.acertos.count(4) * 10 
		return pontos

if __name__ == "__main__":
	solution = Solution()
	print(solution.pontos())
	