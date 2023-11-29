from Crypto.PublicKey import RSA

key = RSA.generate(2048)

private_key = key.exportKey()
file_out = open('private.key', 'wb')
file_out.write(private_key)
file_out.close()

public_key = key.publickey().exportKey()
file_out = open("public.key", "wb")
file_out.write(public_key)
file_out.close()




