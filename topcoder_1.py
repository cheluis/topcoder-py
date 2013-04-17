class StringDup():
	def get_max(self, entry):
		len_entry = len(entry)
		entry_quants = {}
		for letter in entry:
			if not letter in entry_quants:
				entry_quants[letter] = 1
			else:
				entry_quants[letter] = entry_quants[letter] + 1
		output_item = entry[0]
		output_item_value = entry_quants[output_item]
		for k, v in entry_quants.items():
			if k > output_item_value:
				output_item = k
				output_item_value = v
		return output_item


class Syntax():
	def match(self, entry):
		stack = []
		for char in entry:
			if char == '(' or char == '[' or char == '{':
				stack.append(char)
			elif char == ']':
				try:
					aux = stack.pop()
					if aux != '[':
						return False
				except:
					return False		
			elif char == '}':
				try:
					aux = stack.pop()
					if aux != '{':
						return False
				except:
					return False
			elif char == ')':
				try:
					aux = stack.pop()
					if aux != '(':
						return False
				except:
					return False
		if len(stack) > 0:
			return False
		return True
		
