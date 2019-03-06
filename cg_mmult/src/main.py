M = [[1, 4],
	[1, 3]]

N = [[4, 3],
	[0, -1]]

l=range;m=len;r=[([sum([M[i][k]*N[k][j]for k in l(m(N))])for j in l(m(N[0]))])for i in l(m(M))];print(r)
