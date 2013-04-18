class CommonChar():
	def compare(self, string_1, string_2):
		cant = 0		
		for x in string_1:
			i = string_2.find(x)
			if i != -1:
				cant = cant + 1
				string_2 = string_2[0:i] + string_2[i+1:]
				
		return cant
