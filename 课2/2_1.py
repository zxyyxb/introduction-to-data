def max_result(n):
    list=[0]*(n+1)
    sequence=[ [] for _ in range(n + 1) ]
    list[0]=0
    list[1]=1
    sequence[1]=[1]
    for i in range(2,n+1):
        list[i]=i
        for j in range(2,i):
            if j*list[i-j]>list[i]:
                list[i]=j*list[i-j]
                sequence[i]=[j]+sequence[i-j]
        
    return sequence[n]


n=2001
result=max_result(n)
print(result)