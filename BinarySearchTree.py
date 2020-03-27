class Node:
    def __init__(self,data,pos):
        self.right=None
        self.left=None
        self.val=data
        self.pos=pos
def insertAlg(node,value,pos):
    if(node is None):
        print(pos)
        return(Node(value,pos))
    if(value<node.val):
        insertAlg(node.left,val,2*pos)
    else:
        insertAlg(node.right,val,2*pos+1)
    return(node)
def min(val):
    current=val
    if(current.left!=None):
        current=current.left
    return current
def deleteAlg(node,value):
    if node is None:
        return node
    elif(value<node.val):
        deleteAlg(node.left,val)
    elif(value>node.val):
        deleteAlg(node.right,val)
    else:
        print(node.pos)
        if(node.left==None):
            temp=node.right
            node=None
            return temp
        elif(node.right==None):
            temp=node.right
            node=None
            return temp
        temp=min(node.right)
        node.val=temp.val
        node.right=deleteAlg(node.right,temp.val)
        return node
root=None
for i in range(int(input())):
    inp = input().split()
    mode=str(inp[0])
    val=int(inp[1])
    if(mode=="i"):
        root=insertAlg(root,val,1)
    elif(mode=="d"):
        root=deleteAlg(root,val)
        
