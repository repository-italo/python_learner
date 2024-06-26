class Prisma_Hexagonal:
	def __init__(self, lado, h):
		self.lado = lado
		self.h = h
		
	def volume(self):
		area_base = (3 * (self.lado ** 2) * (3 ** 0.5)) / 2
		volume = area_base * h
		return volume

if __name__ == "__main__":
	lado = float(input())
	h = float(input())
	prisma_hexagonal = Prisma_Hexagonal(lado, h)
	print(round(prisma_hexagonal.volume(), 2))