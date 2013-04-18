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
