import random

def merge(L:"list of lists", origLen:int) -> list:
	if len(L[0]) == origLen:
		return L[0]
	
	L[0].append(L[1])
	L[0].sort()
	del L[1]
	
	return merge(L, origLen)
	
	
def main():
	L = [random.randint(0, 999) for i in range(997)]
	L[0] = [L[0]]
	
	print(merge(L, len(L)))
	
if __name__ == "__main__":
	main()
