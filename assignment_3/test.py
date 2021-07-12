import os
from Crypto.Hash import SHA256

#file_path = "C:\\Users\\IZZY\\Desktop\\Cryptography I Assignments\\assignment_3\\6.2.birthday.mp4_download"
file_path = "C:\\Users\\IZZY\\Desktop\\Cryptography I Assignments\\assignment_3\\6.1.intro.mp4_download"

size_block = 1024
size_file = os.path.getsize(file_path)
size_first_block = size_file % size_block
num_blocks = int(size_file / size_block)

print("FILESIZE: " + str(size_file))
print("BLOCK LENGTH: " + str(size_block))
print("BLOCK LENGTH FIRST: " + str(size_first_block))
print("NUMBER OF BLOCKS: " + str(num_blocks))

f = open(file_path, "rb")
size_acc = 0
size_block_read = size_first_block
size_file_acc = size_file
sha_block = b""

while size_file_acc > 0:
		
	f.seek(size_file_acc - size_block_read)
	array_bytes = f.read(size_block_read)
	size_file_acc -= size_block_read
	
	#if size_file_acc == 0:
		#print(array_bytes)
	#	print(sha_block)
	
	if sha_block != b"":
		
		array_bytes += sha_block
		
	#if size_file_acc == 0:
	#	print(array_bytes)
		#print(sha_block)
		
	h = SHA256.new(array_bytes)
	
	if size_file_acc == 0:
	
		print(h.hexdigest())
		
	else:
	
		sha_block = h.digest()
		#print(h.hexdigest())
		
	size_block_read = size_block