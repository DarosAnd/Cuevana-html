import hashlib

p = 'hola1'
m=hashlib.sha256(p)
print(p)
print(m.hexdigest())