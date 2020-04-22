# looks for aminoacid, code and weight
aminoacid = [
	{
		"name":"Alanine",
		"1_letter_symbol" : "A",
		"weight": 98.09
	},
	{
		"name":"Isoleucine",
		"1_letter_symbol" : "I",
		"weight": 131.17
	},
	{
		"name":"Leucine",
		"1_letter_symbol" : "L",
		"weight": 131.17
	},
	{
		"name":"Valine",
		"1_letter_symbol" : "V",
		"weight": 117.15
	},
	{
		"name":"Phenylalanine",
		"1_letter_symbol" : "F",
		"weight": 165.19
	},
	{
		"name":"Tryptophan",
		"1_letter_symbol" : "W",
		"weight": 204.23
	},
	{
		"name":"Tyrosine",
		"1_letter_symbol" : "Y",
		"weight": 181.19
	},
	{
		"name":"Asparagine",
		"1_letter_symbol" : "N",
		"weight": 132.12
	},
	{
		"name":"Cysteine",
		"1_letter_symbol" : "C",
		"weight": 121.16
	},
	{
		"name":"Glutamine",
		"1_letter_symbol" : "Q",
		"weight": 146.15
	},
	{
		"name":"Methionine",
		"1_letter_symbol" : "M",
		"weight": 149.21
	},
	{
		"name":"Serine",
		"1_letter_symbol" : "S",
		"weight": 105.09
	},
	{
		"name":"Threonine",
		"1_letter_symbol" : "T",
		"weight": 119.12
	},
	{
		"name":"Arginine",
		"1_letter_symbol" : "R",
		"weight": 174.2
	},
	{
		"name":"Histidine",
		"1_letter_symbol" : "H",
		"weight": 155.16
	},
	{
		"name":"Lysine",
		"1_letter_symbol" : "K",
		"weight": 146.19
	},
	{
		"name":"Aspartic Acid",
		"1_letter_symbol" : "D",
		"weight": 133.1
	},
	{
		"name":"Glutamic Acid",
		"1_letter_symbol" : "E",
		"weight": 147.13
	},
	{
		"name":"Glycine",
		"1_letter_symbol" : "G",
		"weight": 75.07
	},
	{
		"name":"Proline",
		"1_letter_symbol" : "P",
		"weight": 115.13
	},
	{
		"name":"Selenocysteine",
		"1_letter_symbol" : "U",
		"weight": 150.95
	},
		{
		"name":"Pyrrolysine",
		"1_letter_symbol" : "O",
		"weight": 237.14
	},
	
]

def aminoacid_weight(letter):
	for i in aminoacid:
		if letter == i["1_letter_symbol"]:
			return i["weight"]
	

def total_weight(aminoacid_Chain):
	# loops over all molecules
	for molecule in aminoacid_Chain:
		
		#set to 0 every new molecule
		weight_molecule = 0

		#loops over all letters in the chain
		for letter in molecule:
			weight_molecule = weight_molecule + aminoacid_weight(letter)





		#total weight of the molecule
		print(str(weight_molecule))
	# found = True
	# for i in aminoacid_Chain:
	# 	print(i)

	# return (tuples)


test = ["ASFG","KVUA","RSTA"]
total_weight(test)
