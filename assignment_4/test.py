import urllib.request
import string

TARGET = 'http://crypto-class.appspot.com/po?er='
CT_hex= "f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4"

def query(q):
	
	target = TARGET + urllib.parse.quote(q)
	
	#print(target)
	#print(len(q))
	
	req = urllib.request.Request(target)
	try: urllib.request.urlopen(req)
	except urllib.error.URLError as e:
		#print(e.code)
		return e.code == 404
		
	return True

CT_bytearray = bytearray.fromhex(CT_hex)
payload_bytearray = CT_bytearray[16:]
result_string = ['@'] * len(payload_bytearray)
IV_bytearray = CT_bytearray[:16]

# 1 for IV and 3 for payload
num_blocks_to_send = 4
block_to_modify = 2

# for all bytes in a block
for byte in reversed(range(0, 16)):
	
	index_string = block_to_modify * 16 + byte
		
	print(index_string)
		
	char_bytearray = bytearray(len(CT_bytearray))
	padding_bytearray = bytearray(len(CT_bytearray))
		
	outer_range = (block_to_modify + 1) * 16
	padding_bytes = outer_range - index_string
		
	for i in range(index_string, outer_range):
			
		char_bytearray[i] = ord(result_string[i])
		padding_bytearray[i] = padding_bytes
			
	print(padding_bytearray.hex())

	#for char in range(48, 126):
	for char in range(9, 255):
		
		#print(char)
		
		if result_string[index_string] != '@':
			
			break

#print("LEN CT: " + str(len(CT_bytearray)))
#print("LEN IV: " + str(len(IV_bytearray)))
#print("LEN PAYLOAD: " + str(len(payload_bytearray)))
				
		char_bytearray[index_string] = char
		CT_send_bytearray = bytearray.fromhex(CT_hex)

		for i in range(len(CT_bytearray)):

			CT_send_bytearray[i] ^= padding_bytearray[i] ^ char_bytearray[i]

		CT_send_bytearray = CT_send_bytearray[ : num_blocks_to_send * 16]
		CT_send_hex = CT_send_bytearray.hex()
			
		#print(char_bytearray.hex())
		#print(padding_bytearray.hex())
		#print(CT_send_hex)
		#print(len(CT_send_bytearray))
			
		if query(CT_send_hex):

			print(str(chr(char)) + ", " + str(char) + ": Correct padding!")
			result_string[index_string] = chr(char)
			print(*result_string)
			break