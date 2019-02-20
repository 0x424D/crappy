def split(L:list) -> list:
	ret = []
	for i in L:
		ret.append([i])
	while len(ret) > 1:
		ret[0] = merge(ret[0], ret[1])
		del ret[1]
	return ret[0]
	
def merge(L1:list, L2:list) -> list:
	for i in L2:
		for n, j in enumerate(L1):
			if i <= j:
				L1.insert(n, i)
				break
		else:
			L1.append(i)
	return L1
	
def main():
	from random import randint
	L = [randint(0, 999) for i in range(20)]
	
	print(f"L (unsorted): {L}")
	print(f"L (sorted): {split(L)}")
	
if __name__ == "__main__":
	main()
