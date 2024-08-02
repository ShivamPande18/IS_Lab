message = "the house is being sold tonight"
newmsg=""
dec=""
key = "dollars"
cur = 0;


for m in message:
	if(m==" ") :
		newmsg+=" "
	else:
		i = ord(m) - ord("a");
		#print(i,end=" ");
		i = ( i + (ord(key[cur]) - ord("a")) ) % 26;
		cur+=1
		if(cur>=len(key)): cur=0
		newmsg += chr(i + ord('a'))
	
print(newmsg)

cur=0

for m in newmsg:
	if(m==" ") :
		dec+=" "
	else:
		i = ord(m) - ord("a");
	
		#print(i,end=" ");
		i = (i- (ord(key[cur]) - ord("a")) )
		cur+=1
		if(cur>=len(key)): cur=0
		if(i<0):
			i = -i;
			i = i%26
			dec += chr(26-i + ord('a'))
		else: 
			dec += chr(i + ord('a')) 
		
print(dec)
