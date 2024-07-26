message = "i am learning infromation security"
newmsg=""
for m in message:
	if(m==" ") :
		newmsg+=" "
	else:
		i = ord(m) - ord("a");
		#print(i,end=" ");
		i = (i+20)%26;
		newmsg += chr(i + ord('a'))
	
print(newmsg)
	
