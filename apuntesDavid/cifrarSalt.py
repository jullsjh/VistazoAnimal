import os
import hashlib


salt = os.urandom(32)

# 1
plaintext = 'hellow0rld'.encode()
# sha256, password, salt, longitud de la passw
digest = hashlib.pbkdf2_hmac('sha1', plaintext, salt, 10000)



hex_hash = digest.hex()
print(hex_hash)
byte_hash = digest.fromhex(digest.hex())
# print(byte_hash)

# 2 haciendo lo mismo de diferente forma
pass2 = 'hellow0rld'.encode()
digest2 = hashlib.pbkdf2_hmac('sha1', pass2, salt, 10000)
hex_hash2 = digest2.hex()
print(digest2)

# 3 no entiendo bien esta manera xq da algo diferente
# dk = hashlib.pbkdf2_hmac('sha1', b'hellow0rld', b'salt', 10000)
dk = hashlib.pbkdf2_hmac('sha1', 'hellow0rld'.encode(), os.urandom(32), 10000)
print(dk.hex())



# DEFINITIVO
# https://levelup.gitconnected.com/python-salting-your-password-hashes-3eb8ccb707f9
# ejemplos cifrar
# https://docs.python.org/3/library/hashlib.html

# salt
# https://stackoverflow.com/questions/9594125/salt-and-hash-a-password-in-python
# https://levelup.gitconnected.com/python-salting-your-password-hashes-3eb8ccb707f9
# base64
# https://www.geeksforgeeks.org/encoding-and-decoding-base64-strings-in-python/#:~:text=In%20Python%20the%20base64%20module,import%20base64
# uuid
# https://www.geeksforgeeks.org/generating-random-ids-using-uuid-python/#:~:text=UUID%2C%20Universal%20Unique%20Identifier%2C%20is,hardware%20(MAC%20etc.).

