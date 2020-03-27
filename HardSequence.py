def findIndex(li , i):
    indexPosList = []
    indexPos = 0
    while True:
        try:
            indexPos = li.index(i, indexPos)
            indexPosList.append(indexPos)
            indexPos += 1
        except ValueError as e:
            break
    return indexPosList

def findSequence(n):
    li=[0]
    for j in range(n-1):
        i=li[-1]
        if(i not in li[0:len(li)-1]):
            li.append(0)
        else:
            indexes=findIndex(li[:len(li)-1] , i)
            li.append((len(li)-1)-max(indexes))
    return li
            
for i in range(int(input())):
    n=int(input())
    c=findSequence(n)
    print(c.count(c[n-1]))


            
