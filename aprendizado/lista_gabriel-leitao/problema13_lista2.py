class Circulo:
	def __init__(self, raio):
		self.raio = raio
	
	def calculaArea(self) -> float:
		area = 3.14 * (self.raio ** 2)
		return area

if __name__ == "__main__":
	raio = float(input())
	circulo = Circulo(raio)
	area = circulo.calculaArea()
	print("%.2f" % area)