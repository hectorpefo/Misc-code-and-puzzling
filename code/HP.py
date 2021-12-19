
# Fetch and write a list from and to text file, 
# with newlines separating items
def listFromFile(filename, dataDir = "../data/"):
	try:
		f = open(dataDir + filename)
		try:
			text = f.read().splitlines()
		except:
			print("Could not {} {}{}".format("read from",dataDir,filename))
		finally:
			f.close()
		return text
	except:
		print("Could not {} {}{}".format("open",dataDir,filename))

def listToFile(outList, filename,dataDir = "../data/"):
	try:
		f = open(dataDir + filename,"w")
		try:
			f.write("\n".join(outList))
		except:
			print("Could not {} {}{}".format("write to",dataDir,filename))
		finally:
			f.close()
	except:
		print("Could not {} {}{}".format("open",dataDir,filename))

def binaryToLetter(binStr,aVal=1):
    # 5-bit binary encoding of a letter
    # unicode for A is 65
    if not aVal in (0,1):
        return None
    charNum = int(binStr,2)
    if not charNum - aVal in range(26):
        return None
    return chr(65 + charNum - aVal) 

def  hamming_encode(x3,x5,x6,x7):
        x1= (x3+x5+x7) % 2
        x2= (x3+x6+x7) % 2
        x4= (x5+x6+x7) % 2
        return (x1 ,x2,x3 ,x4,x5,x6 ,x7)
def  hamming_decode(y1,y2,y3,y4,y5,y6,y7):
    # Hamming  decoding  of the 7 bit signal, parity bits y1 y2 y4
    # Return triple: 4tuple with (corrected) data bits, error bit 1 to 7 
    # or 0 if none, and correct value of erroneous bit. 
    y=[y1,y2 ,y3,y4,y5 ,y6,y7]
    b1= (y1+y3+y5+y7) % 2
    b2= (y2+y3+y6+y7) % 2
    b3= (y4+y5+y6+y7) % 2
    b=4*b3+2*b2+b1       # the integer value of b3b2b1
    if b1+b2+b3 == 1:    # incorrect parity bit is bit b
        return((y3,y5,y6 ,y7),b,1-y[b-1])
    elif b==0:           # no error
        return ((y3,y5,y6 ,y7),0,0)
    else:                # error in data bit b
        y[b-1]=1-y[b -1] 
        return ((y[2],y[4],y[5],y[6]),b,y[b-1])