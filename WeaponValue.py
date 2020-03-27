def battleFunc(t1,t2):
    for i in range(len(t1)):
        if(t1[i]=="1" and t2[i]=="1"):
            s1=list(t1)
            s1[i]="0"
            t1="".join(s1)
            s2=list(t2)
            s2[i]="0"
            t2="".join(s2)
    if(t1.count("1")>t2.count('1')):
        temp1=list(t1)
        for i in range(len(t2)):
            if(t2[i]=='1'):
                temp1[i]='1'
        t1="".join(temp1)
        return t1
    else:
        temp2=list(t2)
        for i in range(len(t1)):
            if(t1[i]=='1'):
                temp2[i]='1'
        t2="".join(temp2)
        return t2
for _ in range(int(input())):
    n=int(input())
    s=[]
    battle=[]
    for i in range(n):
        s.append(input()) 
    battle.append(s[0])
    battle.append(s[1])
    for j in range(2,len(s)): 
        tempwin=battleFunc(battle[0] , battle[1])
        battle.clear()
        battle.append(tempwin)
        battle.append(s[j])
    final=battleFunc(battle[0],battle[1])
    print(final.count("1"))
        
