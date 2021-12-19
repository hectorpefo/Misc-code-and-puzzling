import HP

words = HP.listFromFile("words_corncob.txt")
words = HP.listFromFile("spreadlist.txt")

tlw = [w for w in words if len(w) == 3 and w[0] != w[1] 
		and w[1] != w[2] and w[0] != w[2]]

for t in tlw:
	for w in words:
		if not len(w) == 11: continue
		if not (w[1] == t[2] and w[2]==t[0] and w[3]==t[1] and w[4]==t[2]):			
			continue
		if not w[0]==w[8]:
			continue
		ok = True
		chars = list(t) + [w[0],w[5],w[6],w[7],w[9],w[10]]
		hits = [(i,j) for i in range(len(chars)) for j in range(i+1,len(chars)) if chars[i] == chars[j]]
		if hits != []:
			continue
		print(t,w)
