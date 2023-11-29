# RSADigitalSignature
Realization of RSA digital signature algorithm on python.

You need to install pycryptodome lib, try it using command: pip install pycryptodome
The realization is divided into three parts. For first is "create_key.py", which is used to generate and save our private and public keys. Second, is a "signing.py", which is a signing algorithm of the RSA. And third, "verifying.py", to verify our output sign.
This repository includes file-examples with keys (public.key\private.key), message (message.txt), and sign (signature.pem).
You can try it by running files in the next sequence: 1 - run "create_key.py", 2- run "signing.py", 3- run "verifying.py". If all is correct- you will probably see the message "The signature is valid.", and if not- "Invalid signature!"
