from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

message = b'Hello World!'

#importing key and creating a hash of the message
key = RSA.import_key(open('private.key').read())
hash = SHA256.new(message)

#signing message
signer = PKCS1_v1_5.new(key)
signature = signer.sign(hash)

#saving to files
file_out = open('signature.pem', 'wb')
file_out.write(signature)
file_out.close()

file_out = open('message.txt', 'wb')
file_out.write(message)
file_out.close()