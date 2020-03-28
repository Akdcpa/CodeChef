def replace_str(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])
for i in range(int(input())):
    N=int(input())
    string=input()
    for j in range(int(input())):
        case=list(input().split())
        if(int(case[0])==1):
            L=int(case[1])
            R=int(case[2])
            C=case[3]
            for k in range(L-1,R):
                string=replace_str(string,k,C)
        else:
            L=int(case[1])
            R=int(case[2])
            P=int(case[3])
            Q=int(case[4])
            MOD=10**9+7
            for l in range(L-1 , R):
                if(string[l]=="A"):
                    P1=(P-Q+MOD)%MOD
                    Q1=(P+Q)%MOD
                    P=P1
                    Q=Q1
                elif(string[l]=="B"):
                    P2=(P+Q)%MOD
                    Q2=(Q-P+MOD)%MOD
                    P=P2
                    Q=Q2
            print(P,Q)
