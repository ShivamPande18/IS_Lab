from des import DesKey

key0 = DesKey(b"some key")                  
key1 = DesKey(b"a key for TRIPLE")          
key2 = DesKey(b"a 24-byte key for TRIPLE")  
key3 = DesKey(b"1234567812345678REAL_KEY")  

print(key0.encrypt(b"abc", padding=True))  

print(key0.decrypt(b"%\xd1KU\x8b_A\xa6", padding=True))
