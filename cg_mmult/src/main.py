M=[[1,2]];N=[[3],[4]];print([[sum(i[k]*N[k][j]for k in range(len(N)))for j in range(len(N[0]))]for i in M])
