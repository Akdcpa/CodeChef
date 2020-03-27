def findPlace(string):
    l = [string[0]]
    x = 0
    y = 0
    for j in range(1, len(string)):
        prev = l[-1]
        curr = string[j]
        if prev == "R" and curr != "R" and curr != "L":
            l += curr
        elif prev == "L" and curr != "R" and curr != "L":
            l += curr
        elif prev == "U" and curr != "D" and curr != "U":
            l += curr
        elif prev == "D" and curr != "D" and curr != "U":
            l += curr
    for i in l:
        if(i=='L'):
            x=x-1
        elif(i=='R'):
            x=x+1
        elif(i=='U'):
            y=y+1
        elif(i=='D'):
            y=y-1
    print(x,y)
    return 0
try:
    for i in range(int(input())):
        n=int(input())
        string=input()
        findPlace(string)
except:
    pass
