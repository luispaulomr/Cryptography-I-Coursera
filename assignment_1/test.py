import string

files = \
	("msg_1", \
	 "msg_2", \
	 "msg_3", \
	 "msg_4", \
	 "msg_5", \
	 "msg_6", \
	 "msg_7", \
	 "msg_8", \
	 "msg_9", \
	 "msg_10", \
	 "msg_11")
	 
list_hex_strings = []
list_byte_arrays = []
list_of_values = [None] * 255

for f in files:

	fd = open(f, "r")
	
	hex_string = fd.read()
	
	byte_array = bytearray.fromhex(hex_string)
	
	list_byte_arrays.append(byte_array)
	
	#list_hex_strings.append(hex_string)
	
def xor(index_1, index_2):

	min_len = min(len(list_byte_arrays[index_1]), len(list_byte_arrays[index_2]))
	
	for i in range(min_len):
	
		result = list_byte_arrays[index_1][i] ^ list_byte_arrays[index_2][i]
		
		if not list_of_values[result]:
		
			continue
		
		if not list_of_all_combinations[i]:
		
			list_of_all_combinations[i] = []
			
		for j in list_of_values[result]:
		
			list_of_all_combinations[i].append(j)
		
		#print(str(i) +  ": " + hex(result) + " " + chr(result) + " " + hex(a[i]) + " " + hex(b[i]))
		
		#print(str(i) + ": " + hex(result))
		#print(list_of_values[result])
	
def strxor2(a, b):

	min_len = min(len(a), len(b))
	
	for i in range(min_len):
	
		result = a[i] ^ b[i]
		
		#print(str(i) +  ": " + hex(result) + " " + chr(result) + " " + hex(a[i]) + " " + hex(b[i]))
		
		print(str(i) + ": " + hex(result))
		print(list_of_values[result])
	
def strxor(a, b):     # xor two strings of different lengths
	if len(a) > len(b):
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
	else:
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])
	
def print_msg(hex_string):

	byte_array = bytearray.fromhex(hex_string)
	
	print(byte_array)
	
	print(byte_array[1])
	print(byte_array[2])
	print(hex(byte_array[3]))
	
def generate_list_of_values():

	string_iterate = string.printable
	
	#print(string_iterate)
	
	for i, ci in enumerate(string_iterate):
	
		#print(str(ci) + " " + str(i))
		
		if i >= len(string_iterate):
			
			break
		
		for j in range(i + 1, len(string_iterate)):
		
			result_xor = ord(string_iterate[i]) ^ ord(string_iterate[j])
			
			if not list_of_values[result_xor]:
			
				list_of_values[result_xor] = []
			
			list_of_values[result_xor].append((string_iterate[i], string_iterate[j]))
			
#def find_max
				
			
	
generate_list_of_values()

while True:

	selected_msg = 999
	#selected_msg_1 = 999
	#selected_msg_2 = 999
	
	while selected_msg <= 0 or selected_msg > 11:
	
		selected_msg = int(input("m: "))

	#while selected_msg_1 <= 0 or selected_msg_1 > 11:
	
	#	selected_msg_1 = int(input("m1: "))
	
	#while selected_msg_2 <= 0 or selected_msg_2 > 11:
	
	#	selected_msg_2 = int(input("m2: "))

	index_msg = selected_msg - 1
	#index_msg_1 = selected_msg_1 - 1
	#index_msg_2 = selected_msg_2 - 1
	
	list_of_all_combinations = [None] * 500
	
	for i in range(0, 11):
	
		if i == index_msg:
			
			continue
			
		xor(index_msg, i)
		
	#print(list_of_all_combinations[0])
	
	for i_list_combinations, list_combinations in enumerate(list_of_all_combinations):
	
		if not list_combinations:
		
			continue
	
		array_frequency = [0] * 255
	
		for pair in list_combinations:
		
			if (not pair[0].isalpha() and not pair[0] == ' ') or (not pair[1].isalpha() and not pair[1] == ' '):
			
				continue
	
			array_frequency[ord(pair[0])] = array_frequency[ord(pair[0])] + 1
			array_frequency[ord(pair[1])] = array_frequency[ord(pair[1])] + 1
				
		#print(array_frequency)
		
		#for i, freq in enumerate(array_frequency):
		
			#print(chr(i) + " " + str(freq))
		
		#break
		
		max_value = max(array_frequency)
		
		indices = [index for index, element in enumerate(array_frequency) if element == max_value]
		
		str_indices = ""
		
		for i in indices:
		
			str_indices = chr(i) + ", " + str_indices
			
		print(str(i_list_combinations) + " " + str_indices)
		
		#find max
		#find indexes

	#print(files[index_msg_1])
	#print()
	#print(list_byte_arrays[index_msg_1])
	#print_msg(list_hex_strings[index_msg_1])
	#print()

	#print(files[index_msg_2])
	#print()
	#print(list_byte_arrays[index_msg_2])
	#print_msg(list_hex_strings[index_msg_2])
	#print()

	#print(strxor(list_hex_strings[index_msg_1], list_hex_strings[index_msg_2]))
	#print()
	#print_msg(strxor(list_hex_strings[index_msg_1], list_hex_strings[index_msg_2]))
	#strxor2(list_byte_arrays[index_msg_1], list_byte_arrays[index_msg_2])