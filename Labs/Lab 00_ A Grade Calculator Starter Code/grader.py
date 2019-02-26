def assigngrade(score, grades =  ['A', 'B', 'C', 'D', 'F'], cutoffs = [90, 80, 70, 65, 0]):
    """if score >= 90: return 'A'
                if score < 90 and score >= 80: return 'B'
                if score < 80 and score >= 70: return 'C'
                if score < 70 and score >= 65: return 'D'
                if score < 65: return 'F'"""
    for i in range(0, len(cutoffs)):
      if score >= cutoffs[i] and i == 0: return grades[0]
      if i != 0 and score >= cutoffs[i] and score < cutoffs[i-1]: return grades[i]

def droplowest(L):
    if L:
    	L.remove(min(L))

def average(L):
    if L:
    	return sum(L)/len(L)


