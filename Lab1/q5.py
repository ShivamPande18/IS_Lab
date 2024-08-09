msg = "XVIEWYWI"
key = 22
newmsg = ""
	
for m in msg:
	i = ord(m) - ord('A')
	i = (i + key)%26
	newmsg += chr(i + ord('a'))
print(newmsg)
