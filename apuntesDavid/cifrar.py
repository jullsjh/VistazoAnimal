import hashlib
# con esta forma solo necesitamos importar hashlib
# new retorna un nuevo obj de la clase hash


# 1
# ej cifrar con sha1 , la b son bytes
h = hashlib.new("sha1", b"password")
# retorna la cadena hasheada en hexadecimal
print(h.hexdigest())
# retorna la cadena hasheada en binario
# print(h.digest())

# 2
# haciendo lo mismo de diferente forma
passw = b"password"
otherHash = hashlib.sha1(passw)
print(otherHash.hexdigest())






# https://recursospython.com/guias-y-manuales/hashlib-md5-sha/

