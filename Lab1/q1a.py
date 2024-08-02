message = "i am learning infromation security"
newmsg=""
dec=""
for m in message:
	if(m==" ") :
		newmsg+=" "
	else:
		i = ord(m) - ord("a");
		#print(i,end=" ");
		i = (i+20)%26;
		newmsg += chr(i + ord('a'))
	
print(newmsg)


for m in newmsg:
	if(m==" ") :
		dec+=" "
	else:
		i = ord(m) - ord("a");
		i = (i-20);
		if(i<0):
			i = -i;
			i = i%26
			dec += chr(26-i + ord('a'))
		else: 
			dec += chr(i + ord('a')) 
		
print(dec)
