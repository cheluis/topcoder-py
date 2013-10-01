class Finances():
	def timeleft(self, initial_value, interest, money_taken):
		time = -1
		while(initial_value >= 0):
			aux = (initial_value * interest) / 100
			initial_value = initial_value + aux
			initial_value = initial_value - money_taken
			time = time + 1
			if time >= 1200:
				return time
		return time


class Fraction():
	def get_x_smallest(self, x, a):
		aux_index = 0
		arr = [float(1) for y in range(1, 10001)]
		for i in range(1, a + 1):
			for j in range(1, i):
				val = float(j) / float(i)
				aux_index = aux_index + 1
				arr[aux_index] = val
		arr.sort()
		return arr[x - 1]


