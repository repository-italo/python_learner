from math import pi
class Cilindro:
	def __init__(self, r, h):
		self.r = r
		self.h = h
	
	def volume(self):
		area_base = pi * (self.r ** 2)
		volume = area_base * self.h
		return volume

if __name__ == "__main__":
	r = float(input())
	h = float(input())
	cilindro = Cilindro(r, h)
	print(round(cilindro.volume(), 2))