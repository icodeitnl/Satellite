class Node:
   def __init__(self, value): 
       self.right = None  #from self get the 'right' attribute and set it to None
       self.left = None #from self get the 'left' attribute and set it to None
       self.value = value 
def PreOrder(stack):
   if stack: #if true is the statement that the class Node is called with a value
       print (stack.value) # print the value passed to the class Node as a stack parameter
       PreOrder(stack.left)
       PreOrder(stack.right)

def inOrder(stack):
   if stack:    
       inOrder(stack.left)
       print (stack.value) 
       inOrder(stack.right)
       
stack = Node("a") # root node, sets stack to an instance of the class Node
stack.left = Node("i") 
stack.right = Node("x") 
stack.right.left = Node("f") 
stack.right.right = Node("r")

print (PreOrder(stack))#call PreOrder function with parameter stack and print the returned value
#a i x f r
print (inOrder(stack))
#i a f x r