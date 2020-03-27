def conc(items):
    count=0
    cind=[]
    ind=[]
    i=0
    for i in range(len(items)):
        while(items[i+1]==items[i]+1):
            count=count+1
            cind.append(items[i])
            i=i+1
            items.remove(items[i])
        cind.append(items[i])
    return cind
for _ in range(int(input())):
    items=list(map(int , input().split()))
    result=[]
    print(conc(items))
