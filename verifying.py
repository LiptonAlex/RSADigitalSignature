from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

#reading the public key
key = RSA.import_key(open('public.key').read())

file_in = open('message.txt', 'rb')
message = file_in.read()
file_in.close()

file_in = open('signature.pem', 'rb')
signature = file_in.read()
file_in.close()

hash2 = SHA256.new(message)

try:
    PKCS1_v1_5.new(key).verify(hash2, signature)
    print("The signature is valid.")
except(ValueError, TypeError):
    print("Invalid signature!")