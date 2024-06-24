class Solution:
	def __init__(self):
		self.num_alunos = int(input("Número de alunos: "))
		self.students = {}
		
	def dict_students(self):
		for x in range(self.num_alunos):
			print("Aluno {}".format(x+1))
			nome = input("Nome: ")
			notas = eval(input("Notas: "))
			media_aluno = sum(notas)/len(notas)
			self.students.update({nome : round(media_aluno, 1)})
		print(self.students)

if __name__ == "__main__":
	solution = Solution()
	solution.dict_students()