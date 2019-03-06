M=[[1,2]];N=[[3],[4]];l=range;m=len;r=[([sum([M[i][k]*N[k][j]for k in l(m(N))])for j in l(m(N[0]))])for i in l(m(M))];print(r)
