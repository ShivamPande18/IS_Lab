initialPerm = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]
                
expandPbox = [ 32, 1, 2, 3, 4, 5, 4, 5,
         	6, 7, 8, 9, 8, 9, 10, 11,
         	12, 13, 12, 13, 14, 15, 16, 17,
         	16, 17, 18, 19, 20, 21, 20, 21,
         	22, 23, 24, 25, 24, 25, 26, 27,
         	28, 29, 28, 29, 30, 31, 32, 1]
         	
shiftTable = [1, 1, 2, 2,
               2, 2, 2, 2,
               1, 2, 2, 2,
               2, 2, 2, 1]



def hex2bin(s):
    mp = {'0': "0000",
          '1': "0001",
          '2': "0010",
          '3': "0011",
          '4': "0100",
          '5': "0101",
          '6': "0110",
          '7': "0111",
          '8': "1000",
          '9': "1001",
          'A': "1010",
          'B': "1011",
          'C': "1100",
          'D': "1101",
          'E': "1110",
          'F': "1111"}
    bin = ""
    for i in range(len(s)):
        bin = bin + mp[s[i]]
    return bin

def shortenTo56(key):
	nkey = ""
	for i in range(len(key)):
		if(i%8==0 and i>0): continue
		nkey+=key[i]
		
	return nkey
	
	
def perm(pt, arr, size):
	npt = ""
	for i in range(size):
		npt += pt[arr[i] - 1]
	return npt
	
def shift_left(k, nth_shifts):
    s = ""
    for i in range(nth_shifts):
        for j in range(1, len(k)):
            s = s + k[j]
        s = s + k[0]
        k = s
        s = ""
    return k 
	


pt = "123456ABCD132536"
key = "AABB09182736CCDD"

#step 0
key = hex2bin(key)
pt = hex2bin(pt)


#step 1
print(key)
key = shortenTo56(key)
print(key)


#step 2
print(pt)
pt = perm(pt, initialPerm, 64)
print(pt)



#step 3
left = pt[0:32]
right = pt[32:64]



#step 5
rndKey = []
lkey = key[0:28]
rkey = key[28:52]

for i in 16:
	left = 
	combine = left + right
	r



#step 4
for i in range(16):
	#step 4.1
	rightExpand = permute(right, expandPbox, 48)
	
	#step 4.2
	xorX = xor(rightExpand,)
	














