import random
import time
import math

#Drzewa
class node(object):
    def __init__(self, number = None, parent = None):
        self.number = number
        self.left = None
        self.right = None
        self.parent = parent

   
class tree(object):
    def __init__(self):
        self.dummy = node() #drzewo w prawej nozce dummy
   
    def Add(self, num, nd = "u"):
        if(nd == "u"):
            nd = self.dummy.right
        if(nd == None):    # jeśli drzewo było puste
            self.dummy.right  = node(num, self.dummy)
            return
        if(nd.number>num):
            if(nd.left == None):
                nd.left = node(num, nd)
                return
            else:
                self.Add( num, nd.left)
                return
        elif(nd.number==num):
            return
        else:
            if(nd.right == None):
                nd.right = node(num, nd)
                return
            else:
                self.Add(num, nd.right)
                return
    
    def PrintIO(self, nd = "u"):
        # jeżeli nie podano, skąd zacząć, to zaczynam od góry
        if(nd == "u"):
            nd = self.dummy.right
        if (nd == None):
            return
        self.PrintIO(nd.left)
        print(nd.number, end = ",")
        self.PrintIO(nd.right)
           
    def sum(self, nd = "u"):
        if nd == "u":
            nd = self.dummy.right
        if nd == None:
            return 0
        return nd.number + self.sum(nd.left) + self.sum(nd.right)
    
    def height(self, nd = "u"):
        if nd == "u":
            nd = self.dummy.right
        if nd == None:
            return 0
        return 1 + max(self.height(nd.left),self.height(nd.right))
    
    def leaves(self, nd = "u"):
        if nd == "u":
            nd = self.dummy.right
        if nd == None:
            return 0
        if nd.left is None and nd.right is None:
            return 1
        return self.leaves(nd.left) + self.leaves(nd.right)
    
    def minimum(self, nd = "u"):
        if nd == "u":
            nd = self.dummy.right
        if nd == None:
            return None
        while nd.left is not None:
            nd=nd.left
        return nd
    
    def Myk(self, nd= "u", depth = 0):
        if nd == "u":
            nd = self.dummy.right
        if nd == None:
            return None
        self.Myk(nd.right,depth+1)
        for _ in range(depth):
            print(" ",end="")
        print(nd.number,' (',nd.parent.number,')')
        self.Myk(nd.left, depth+1)
            
    def Successor(self, nd):
        if nd.right is not None:
            return self.minimum(nd.right)
        
        while nd.parent is not None and nd == nd.parent.right:
            nd = nd.parent

        return nd.parent
    
    def PrintTree(self):
        x = self.minimum(self.dummy.right)
        while x is not None:
            print(x.number,end=' ')
            x=self.Successor(x)
    
    def Find(self,num,nd='u'):
        if nd == 'u':
            nd = self.dummy.right
        if nd == None:
            return None
        if (nd.number == num):
            return nd
        if (nd.number < num):
            return self.Find(num,nd.right)
        return self.Find(num,nd.left)
    
    def DeleteNode(self,nd):
        if nd == None:
            return
        
        if nd.left is None and nd.right is None:
            if nd.parent.left is nd:
                nd.parent.left = None
            else:
                nd.parent.right = None
            return
        
        if nd.left is None or nd.right is None:
            TOC = nd.left
            if TOC is None:
                TOC = nd.right
            
            if nd.parent.left is nd:
                nd.parent.left = TOC
            else:
                nd.parent.right = TOC
            TOC.parent = nd.parent
            return
        
        x = self.Successor(nd)
        x.number,nd.number = nd.number,x.number
        self.DeleteNode(x)
        
    def DeleteKey(self,key):
        x = self.Find(key)
        self.DeleteNode(x)
        
    def Rotate(self,B):
        if(B is None or B is self.dummy or B.parent is self.dummy):
            return
        A = B.parent
        p = A.parent
        if B is A.left: #rotacja w prawo
            beta = B.right
            B.right = A
            A.parent = B
            if A is p.left:
                p.left = B
            else: #rotacja w lewo
                p.right = B
            B.parent = p
            A.left = beta
            if beta is not None:
                beta.parent = A
        else:
            beta = B.left
            B.left = A
            A.parent = B
            if A is p.right:
                p.right = B
            else: #rotacja w lewo
                p.left = B
            A.right = beta
            B.parent = p
            if beta is not None:
                beta.parent = A
    
    def DSW(self):
        walker = self.dummy
        n = 0
        while walker.right is not None:
            if walker.right.left is not None:
                self.Rotate(walker.right.left)
            else:
                walker = walker.right
                n+=1
        m = 2 **(int(math.log2(n+1))) - 1
        walker = self.dummy
        for _ in range(n-m):
            walker = walker.right.right
            self.Rotate(walker)
        while m > 1:
            m = m//2
            walker = self.dummy
            for _ in range(m):
                walker = walker.right.right
                self.Rotate(walker)