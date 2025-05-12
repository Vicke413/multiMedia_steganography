from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b'mysecretpassword'
iv = b'1234567890123456'
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = b'hello '

ciphertext= cipher.encrypt(pad(plaintext, AES.block_size))

# print(ciphertext)
# print(cipher.iv)

with open('cipher_file', 'wb') as c_file:
    c_file.write(cipher.iv)
    c_file.write(ciphertext)