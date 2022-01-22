import random 
from cryptography.fernet import Fernet

minus = "abcdefghijklmnopqrstuvwxyz"
mayus = minus.upper()
numbers = "0123456789"
symbols = "@()[]{}*,;?.!$<#>&+~="

sample_base = minus + mayus + numbers + symbols
pass_lenght = 24

for _ in range (5):
    print("Password "+str(_))
    pass_sample = random.sample(sample_base, pass_lenght)
    password = "".join(pass_sample)
    print(password) 
    #Generate a key in a sequence of bytes
    key = Fernet.generate_key()
    object_encode = Fernet(key)
    encrypt_pass = object_encode.encrypt(str.encode(password))
    print(encrypt_pass)
    decrypt_pass_bytes = object_encode.decrypt(encrypt_pass)
    print(decrypt_pass_bytes)
    decrypt_pass = decrypt_pass_bytes.decode()
    print(decrypt_pass)
    print("")
