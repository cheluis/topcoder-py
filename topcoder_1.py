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

