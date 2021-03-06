# merge sort implemented in python 3.x
# copyright (C) 2019 0x424D (www.github.com/0x424D)

import random

def merge(L1, L2):
	ret = []
	
	# while both L1 and L2 are not empty lists, decide which list head is smaller, append it to ret, chop the head off and repeat
	while L1 and L2:
		if L1[0] <= L2[0]:
			ret.append(L1[0])
			L1 = L1[1:]
		else:
			ret.append(L2[0])
			L2 = L2[1:]
	
	# while there is a nonempty list, append each element of the list to ret
	# nonempty list is guaranteed to have two properties: list[0] >= ret[-1]; and for i in list, list[i] <= list[i+1]
	# therefore we can safely just append each element to ret
	while L1:
		ret.append(L1[0])
		L1 = L1[1:]
	while L2:
		ret.append(L2[0])
		L2 = L2[1:]
	
	return ret
	
def msort(L):	
	# splitting
	tmp = [[i] for i in L]
	
	# merging
	ret = [[]]
	while tmp:
		ret[0] = merge(ret[0], tmp[0])
		tmp = tmp[1:]
	
	# we end up with a list of one list, of the form [[a, b, c,...]] where a, b, c,... are integers
	# therefore, we return the first element of ret to avoid the structure being nested
	return ret[0]

def main():
	# let's run the sort on a list that consists of a random amount of random integers between -1000 and 1000 (inclusive)
	L = [random.randint(-1000, 1000) for i in range(random.randint(0, 100))]
	print(msort(L))
	
if __name__ == "__main__":
	main()
