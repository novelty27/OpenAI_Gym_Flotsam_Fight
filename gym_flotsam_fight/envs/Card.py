class Card:
	def __init__(self, value):
		self.value = value
		self.factors = self.get_factors()
		self.valid = len(self.factors) >= 1

	def get_factors(self):
		factors = []
		if (self.value):
			for i in [3, 4, 5, 6, 7, 8, 9, 10]:
				if self.value % i == 0:
					factors.append(i)
			return factors

	def factors(self):
		return self.factors

	def valid(self):
		return self.valid

	def __str__(self):
		return str(self.value)

	def __lt__(self, other):
		return self.value < other.value