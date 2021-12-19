from Levenshtein import distance as LevDistance
import HP
words = HP.listFromFile("words_corncob.txt")
dist = 4
targets = ['suspense','fermion','purge']
covered = []
for t1 in targets:
	for t2 in targets:
		if t1 == t2:
			continue
		for t3 in targets:
			if t1 == t3 or t2 == t3:
				continue
			ts = [t1,t2,t3]
			ts.sort()
			if ts in covered:
				continue
			covered.append(ts)
			if LevDistance(t1,t2) > 2*dist or LevDistance(t1,t3)> 2*dist or LevDistance(t2,t3) > 2*dist: 
				continue
			for w in words:
				if LevDistance(t1,w)==dist and LevDistance(t2,w) ==dist and LevDistance(t3,w)==dist:
					print(t1,t2,t3,w)
