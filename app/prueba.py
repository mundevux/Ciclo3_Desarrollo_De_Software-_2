import hashlib

m = hashlib.sha256("mensaje")
print(m.digest())