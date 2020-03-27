def findPass(n,k):
    arr=[]
    for i in range(n-k , n+1):
        arr.append(i)
    for j in range(1,n-k):
        arr.append(j)
    for u in arr:
        print(u , end=" ")

for _ in range(int(input())):
    n,k=input().split()
    findPass(int(n),int(k))
