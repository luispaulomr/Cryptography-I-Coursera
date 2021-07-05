from Crypto.Cipher import AES
import base64

file_cbc_ct = "question_1_cbc_ciphertext"
file_cbc_key = "question_1_cbc_key"

file2_cbc_ct = "question_2_cbc_ciphertext"
file2_cbc_key = "question_2_cbc_key"

byte_array_ciphertext = bytearray()
byte_array_key = bytearray()

def pad(bs, s):
	return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

def unpad(s):
	return s[:-ord(s[len(s)-1:])]
	 
def decrypt(enc, key):
	#enc = base64.b64decode(_enc)
	iv = enc[:AES.block_size]
	cipher = AES.new(key, AES.MODE_CBC, iv)
	
	#return unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')
	return cipher.decrypt(enc[AES.block_size:])
	
def getByteArrayFromFile(input_file):
	fd = open(input_file, "r")
	hex_string = fd.read()
	byte_array = bytearray.fromhex(hex_string)
	
	return byte_array

byte_array_ciphertext = getByteArrayFromFile(file_cbc_ct)
byte_array_key = getByteArrayFromFile(file_cbc_key)

print("CT len: " + str(len(byte_array_ciphertext)))
print("Key len: " + str(len(byte_array_key)))
print("Block size: " + str(AES.block_size))

print(decrypt(bytes(byte_array_ciphertext), bytes(byte_array_key)))

byte_array_ciphertext = getByteArrayFromFile(file2_cbc_ct)
byte_array_key = getByteArrayFromFile(file2_cbc_key)

print("CT len: " + str(len(byte_array_ciphertext)))
print("Key len: " + str(len(byte_array_key)))
print("Block size: " + str(AES.block_size))

print(decrypt(bytes(byte_array_ciphertext), bytes(byte_array_key)))