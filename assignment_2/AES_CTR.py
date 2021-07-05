from Crypto.Cipher import AES
from Crypto.Util import Counter
import base64

file_ctr_ct = "question_3_ctr_ciphertext"
file_ctr_key = "question_3_ctr_key"

file2_ctr_ct = "question_4_ctr_ciphertext"
file2_ctr_key = "question_4_ctr_key"

byte_array_ciphertext = bytearray()
byte_array_key = bytearray()

def pad(bs, s):
	return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

def unpad(s):
	return s[:-ord(s[len(s)-1:])]
	 
def decrypt(enc, key):
	#enc = base64.b64decode(_enc)
	iv = enc[:AES.block_size]
	ctr = Counter.new(AES.block_size * 8, initial_value = int.from_bytes(iv, byteorder='big', signed=False))
	cipher = AES.new(key, AES.MODE_CTR, counter = ctr)
	
	return cipher.decrypt(enc[AES.block_size:])
	
	#return unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')
	
def getByteArrayFromFile(input_file):
	fd = open(input_file, "r")
	hex_string = fd.read()
	byte_array = bytearray.fromhex(hex_string)
	
	return byte_array

byte_array_ciphertext = getByteArrayFromFile(file_ctr_ct)
byte_array_key = getByteArrayFromFile(file_ctr_key)

print("CT len: " + str(len(byte_array_ciphertext)))
print("Key len: " + str(len(byte_array_key)))
print("Block size: " + str(AES.block_size))

print(decrypt(bytes(byte_array_ciphertext), bytes(byte_array_key)))

byte_array_ciphertext = getByteArrayFromFile(file2_ctr_ct)
byte_array_key = getByteArrayFromFile(file2_ctr_key)

print("CT len: " + str(len(byte_array_ciphertext)))
print("Key len: " + str(len(byte_array_key)))
print("Block size: " + str(AES.block_size))

print(decrypt(bytes(byte_array_ciphertext), bytes(byte_array_key)))