### In this assignment, we use binary expression trees to solve the card game 24
### Read the code and add code to construct the missing trees. There are 5 different
### trees one need to consider. Tree #1 is given, following the example, and
### construct the other 4 trees.
### Also, you need to fill in the code for method evaluate and display.
### Method evaluate evalutes a binary expression tree, while method display
### displays a binary expression tree.
### Read the slides on trees on how to evalute and display (print) a binary
### expression tree.

from fractions import Fraction
import itertools
import sys
ops = ['+', '-', '*', '/']
d = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6' : 6, '7': 7, '8': 8, '9': 9, '0': 10, 'J': 11, 'Q': 12, 'K': 13}

class BNode:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None

    def addleft(self, leftnode):
        self.left = leftnode

    def addright(self, rightnode):
        self.right = rightnode

    def evaluate(self):
        ## Add your code here
        if self.left is None and self.right is None: 
            return d[self.element]
        elif self.left is None:
            y = self.right.evaluate()
        elif self.right is None:
            x = self.left.evaluate()
        else:
            #Evaluate left tree
            x = self.left.evaluate()
            #Evaluate right tree
            y = self.right.evaluate()
            operator = self.element
            if operator == '+': return x + y
            if operator == '-': return x - y
            if operator == '*': return x * y
            if operator == '/':
                if y == 0: return x
                return x / y

    def recursive_inorder(self):
        if self.left is None or self.right is None:
            return []
        return self.left.recursive_inorder() + [self.element] + self.right.recursive_inorder(self)

    def display(self):
        ## Add your code here
        if self.left:
            print("(")
            self.left.display()
        print(self.element)
        if self.right:
            self.right.display()
            print(")")
    
    def display(self):
      sVal = ""
      if self.left:
          sVal = '(' + self.left.display()
      sVal = sVal + str(d.get(self.element,self.element))
      if self.right:
          sVal = sVal + self.right.display() +')'
      return sVal

def evaluatefive(ops, cards):

    s = set()
    # Tree #1        
    node1 = BNode(ops[0])
    node2 = BNode(ops[1])
    node3 = BNode(ops[2])
    node1.addleft(node2)
    node1.addright(node3)

    node4 = BNode(cards[0])
    node5 = BNode(cards[1])

    node6 = BNode(cards[2])
    node7 = BNode(cards[3])

    node2.addleft(node4)
    node2.addright(node5)

    node3.addleft(node6)
    node3.addright(node7)

    if node1.evaluate() == 24:
        s.add(node1.display())

    # Tree #2
    ## Add your code here   
    node1 = BNode(ops[0])
    node2 = BNode(ops[1])
    node3 = BNode(ops[2])

    node4 = BNode(cards[0])
    node5 = BNode(cards[1])
    node6 = BNode(cards[2])
    node7 = BNode(cards[3])

    node1.addleft(node2)
    node2.addleft(node3)

    node3.addleft(node4)
    node3.addright(node5)
    node2.addright(node6)
    node1.addright(node7)

    if node1.evaluate() == 24:
        s.add(node1.display())  

    #tree #3
    ## Add your code here
    node1 = BNode(ops[0])
    node2 = BNode(ops[1])
    node3 = BNode(ops[2])

    node4 = BNode(cards[0])
    node5 = BNode(cards[1])
    node6 = BNode(cards[2])
    node7 = BNode(cards[3])

    node1.addright(node2)
    node2.addright(node3)

    node3.addright(node4)
    node3.addleft(node5)
    node2.addleft(node6)
    node1.addleft(node7)

    if node1.evaluate() == 24:
        s.add(node1.display())  

    #tree #4
    ## Add your code here  
    node1 = BNode(ops[0])
    node2 = BNode(ops[1])
    node3 = BNode(ops[2])

    node4 = BNode(cards[0])
    node5 = BNode(cards[1])
    node6 = BNode(cards[2])
    node7 = BNode(cards[3])

    node1.addleft(node2)
    node1.addright(node7)

    node2.addleft(node4)
    node2.addright(node3)
    
    node3.addleft(node5)
    node3.addright(node6)
    
    if node1.evaluate() == 24:
        s.add(node1.display())  

    #tree #5
    ## Add your code here
    node1 = BNode(ops[0])
    node2 = BNode(ops[1])
    node3 = BNode(ops[2])

    node4 = BNode(cards[0])
    node5 = BNode(cards[1])
    node6 = BNode(cards[2])
    node7 = BNode(cards[3])

    node1.addleft(node4)
    node1.addright(node2)
    node2.addleft(node3)
    node2.addright(node7)

    node3.addleft(node5)
    node3.addright(node6)

    #print([i.element for i in [node1,node2,node3,node4,node5,node6,node7]])
    if node1.evaluate() == 24:
        s.add(node1.display())  
    return s

"""s = list(input("Input your hand:"))
 if len(s) != 4:
     sys.exit()
 for i in range(len(s)):
     if s[i] not in d.keys():
         sys.exit()
 results = set()
 s1 = [0, 1, 2, 3]
 for L in list(itertools.permutations([0, 1, 2, 3], 4)):
     for i in range(4):
         s1[i] = s[L[i]]
 
     ops1 = [ops[0], ops[0], ops[0]]
     for i in range(len(ops)):
         for j in range(len(ops)):
             for k in range(len(ops)):
                 ops1[0] = ops[i]
                 ops1[1] = ops[j]
                 ops1[2] = ops[k]
                 results = results | evaluatefive(ops1, s1)
 for result in results:
     print(result)
 print(str(len(results)) + " solutions.")   """ 

