class StockCalc():
	def get_profit(self, prices):
		profit = 0
		q = len(prices)
		for i in range(0, q ):
			for j in range(i+1, q):
				if(prices[j] - prices[i] > profit):
					profit = prices[j] - prices[i]
		return profit
		
		
class LetterSort():
	def do_sort(self, s_input):
		output = ''
		q = len(s_input)
		for i in range(0, q):
			if s_input[i] not in output:
				aux = s_input[i]
				output = output + aux
				for j in range(i+1, q):
					if s_input[j] == aux:
						 output = output + aux
						 
		return output
		
		
class Obstacle():
	def get_longest_path(self, obstacles):
		return 0
				
				
		
		
