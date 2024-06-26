class Pesquisa:
	def __init__(self):
		self.num_entrevistados = int(input())
		self.entrevistados = []
	
	def coleta(self):
		for x in range(self.num_entrevistados):
			entrevistado = {}
			sexo = input()
			idade = int(input())
			if (idade <= 15): faixa_etaria = 1
			elif (16 <= idade <= 30): faixa_etaria = 2
			elif (31 <= idade <= 45):faixa_etaria = 3
			elif (46 <= idade <= 60): faixa_etaria = 4
			elif (idade > 60): faixa_etaria = 5
			entrevistado.update({"sexo": sexo, "idade": idade, "faixa_etaria" : faixa_etaria})
			self.entrevistados.append(entrevistado)
			
	def estatisticas(self):	
		idades = [e["idade"] for e in self.entrevistados]
		media_idades = sum(idades) / len(idades)
		print("%.1f" % media_idades)
		
		idade_mulheres = [e["idade"] for e in self.entrevistados if e["sexo"] == "Mulher"]
		media_idade_mulheres = sum(idade_mulheres) / len(idade_mulheres)
		print("%.1f" % media_idade_mulheres)
		
		idade_homens = [e["idade"] for e in self.entrevistados if e["sexo"] == "Homem"]
		media_idade_homens = sum(idade_homens) / len(idade_homens)
		print("%.1f" % media_idade_homens)
		
		faixas_etarias = [e["faixa_etaria"] for e in self.entrevistados]
		for i in range(1,6):
			print("%i" % faixas_etarias.count(i))
			
		faixa_etaria_homens = [e["faixa_etaria"] for e in self.entrevistados if e["sexo"] == "Homem"]
		faixa_4_count = faixa_etaria_homens.count(4)
		print("%.1f" % float((faixa_4_count / len(faixa_etaria_homens)) * 100))
		
if __name__ == "__main__":
	pesquisa = Pesquisa()
	pesquisa.coleta()
	pesquisa.estatisticas()