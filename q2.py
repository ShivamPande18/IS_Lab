message = "i am learning infromation security"
newmsg=""
for m in message:
	if(m==" ") :
		newmsg+=" "
	else:
		i = ord(m) - ord("a");
		#print(i,end=" ");
		i = (i*15)%26;
		newmsg += chr(i + ord('a'))
	
	
print(newmsg)

key = pow(15,-1,26)
dec = ""

for m in newmsg:
	if(m==" ") :
		dec+=" "
	else:
		i = ord(m) - ord("a");
		i = (i*key)%26;
		dec += chr(i + ord('a'))
		
print(dec)
	
