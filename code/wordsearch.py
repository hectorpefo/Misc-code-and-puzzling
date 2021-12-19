import HP
from copy import deepcopy

minLen = 4

##### in file in rows of lowercase letters, other chars okay
#inFile = "wordsearch.txt"
inFile = "GoKarts.txt"
outFile = "GoKartsDetails.txt"
foundFile = "GoKartsFound.txt"
upperedFile = "GoKartsUppered.csv"
#####

wordList = "spreadlist.txt"
# wordList = "words_corncob.txt"

rows = [r.lower() for r in HP.listFromFile(inFile)]
words = [w.lower() for w in HP.listFromFile(wordList)]
# words = [w.lower() for w in words]

numRows = len(rows)
numCols = len(rows[1])

# list-format grid to change found stuff to uppercase
outRowList = [list(r) for r in rows]
outStr = "DETAILS"
found = []

print("Horizontals")
outStr += "\nHORIZ LR:\n"
for r in range(len(rows)):
	for i in range(0,numCols-minLen+1):
		for j in range(i+minLen-1,numCols):
			maybeRowList = deepcopy(outRowList)
			s = rows[r][i:j+1]
			maybeRowList[r][i:j+1] = list(s.upper())
			if s in words and not s in found:
				outStr += "{} ({},{})\n".format(s,r+1,i+1)
				found.append(s)
				outRowList = maybeRowList

outStr += "\nHORIZ RL:\n"
for r in range(len(rows)):
	for i in range(minLen-1,numCols):
		for j in range(0,i-minLen+2):
			maybeRowList = deepcopy(outRowList)
			s = rows[r][i:j-1:-1]
			maybeRowList[r][i:j-1:-1] = list(s.upper())
			if s in words and not s in found:
				outStr += "{} ({},{})\n".format(s,r+1,i+1)
				found.append(s)
				outRowList = maybeRowList

print("Verticals")
outStr += "\nVERT UP:\n"
for r in range(minLen-1,numRows):
	for i in range(numCols):
		for j in range(0,r-minLen+2):
			maybeRowList = deepcopy(outRowList)
			s = ""
			for k in range(0,r-j+1):
				s += rows[r-k][i]
				maybeRowList[r-k][i] = maybeRowList[r-k][i].upper()
			if s in words and not s in found:
				outStr += "{} ({},{})\n".format(s,r+1,i+1)
				found.append(s)
				outRowList = maybeRowList

outStr += "\nVERT DOWN:\n"
for r in range(0,numRows-minLen+1):
	for i in range(numCols):
		for j in range(r+minLen-1,numRows):
			maybeRowList = deepcopy(outRowList)
			s = ""
			for k in range(0,j-r+1):
				s += rows[r+k][i]
				maybeRowList[r+k][i] = maybeRowList[r+k][i].upper()
			if s in words and not s in found:
				outStr += "{} ({},{})\n".format(s,r+1,i+1)
				found.append(s)
				outRowList = maybeRowList

print("Diagonals")

outStr += "\nDIAG UP LR:\n"
for r in range(minLen-1,numRows):
	for i in range(0,numCols-minLen+1):
		there = False
		for j in range(i+minLen-1,min(numCols-1,r+i)+1):
			maybeRowList = deepcopy(outRowList)
			s = ""
			for k in range(0,j-i+1):
				s += rows[r-k][i+k]
				maybeRowList[r-k][i+k] = maybeRowList[r-k][i+k].upper()
			if s in words and not s in found:
				outStr += "{} ({},{})\n".format(s,r+1,i+1)
				found.append(s)
				outRowList = maybeRowList

outStr += "\nDIAG UP RL:\n"
for r in range(minLen-1, numRows):
	for i in range(minLen-1, numCols):
		for j in range(max(0,i-r),(i-minLen+1)+1):
			maybeRowList = deepcopy(outRowList)
			s=""
			for k in range(0,i-j+1):
				s += rows[r-k][i-k]
				maybeRowList[r-k][i-k] = maybeRowList[r-k][i-k].upper()
			if s in words and not s in found:
				outStr += "{} ({},{})\n".format(s,r+1,i+1)
				found.append(s)
				outRowList = maybeRowList

outStr += "\nDIAG DOWN RL:\n"
for r in range(0,numRows-minLen+1):
	for i in range(minLen-1,numCols):
		for j in range(max(0,i-(numRows-1-r)),(i-minLen+1)+1):
			maybeRowList = deepcopy(outRowList)
			s = ""
			for k in range(0,i-j+1):
				s += rows[r+k][i-k]
				maybeRowList[r+k][i-k] = maybeRowList[r+k][i-k].upper()
			if s in words and not s in found:
				outStr += "{} ({},{})\n".format(s,r+1,i+1)
				found.append(s)
				outRowList = maybeRowList

outStr += "\nDIAG DOWN LR:\n"
for r in range(0,numRows-minLen+1):
	for i in range(0,numCols-minLen+1):
		for j in range(i+minLen-1,min(numCols-1,i+(numRows-1-r))+1):
			maybeRowList = deepcopy(outRowList)
			s = ""
			for k in range(0,j-i+1):
				s += rows[r+k][i+k]
				maybeRowList[r+k][i+k] = maybeRowList[r+k][i+k].upper()
			if s in words and not s in found:
				outStr += "{} ({},{})\n".format(s,r+1,i+1)
				found.append(s)
				outRowList = maybeRowList

with open("../data/" + outFile,"w") as f:
	f.write(outStr)
print("Detailed list of words in " + outFile)

print("Sorted list of found words in " + foundFile )

found.sort()
HP.listToFile(found,foundFile)

for i in range(len(outRowList)):
	outRowList[i] = ",".join(outRowList[i])
HP.listToFile(outRowList,upperedFile)
print("Modified grid with found words in uppercase in ",upperedFile)

print (found)