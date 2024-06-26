from math import pi
class Cone:
	def __init__(self, r, h):
		self.r = r
		self.h = h
	
	def volume(self):
		area_base = pi * (self.r ** 2)
		volume = (area_base * self.h) / 3
		return volume

if __name__ == "__main__":
	r = float(input())
	h = float(input())
	cone = Cone(r, h)
	print(round(cone.volume(), 2))