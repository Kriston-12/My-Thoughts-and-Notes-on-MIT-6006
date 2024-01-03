class BinaryNode:
  def __init__(A, x):   # (A, x)  == (self, x)
    A.parent = None       # parent is not specified in the pdf
    A.item = x
    A.left = None
    A.right = None

# All algorithm operations below must mantain BST property

# InOrder Traversal
def subtree_iter(A): # O(n)
  if A.left: yield from A.left.subtree_iter()
  yield A
  if A.right: yield from A.right.subtree_iter()

# Recursion to find the leftmost node   # O(h) where h is the height of the tree
def subtree_first(A): 
  if A.left: return A.left.subtree_first()
  else: return A
 
def subtree_last(A): # O(h)
  if A.right: return A.right.subtree_last()
  else: return A

# Find successor in a inOrderTraversal Binary Tree    # O(h)
def successor(A): 
  if A.right: return A.right.subtree_first()    # If has right subtree, find the leftmost node in the right subtree
  while A.parent and (A is A.parent.right):      # Here it means the tree has not right subtree. It has to find the place where A is in the left substree
    A = A.parent
    return A.parent

# Find predecessor in a inOrderTraversal Binary Tree   O(h)
def predecessor(A): 
  if A.left: return A.left.subtree_last()
  while A.parent and (A is A.parent.left):  
    A = A.parent
    return A.parent

# Insert node B before Node A
def sub_tree_insert_before(A, B): 
  if A.left: A.left.subtree_last.right = B, B.parent = A
  else A.left = B, B.parent = A

# Insert node B after Node A
def sub_tree_insert_after(A, B):
  if A.right: A.right.substree_first.left = B, B.parent = A
  else A.right = B, B.parent = A

def sub_tree_delete(A):
  if A.left or A.right:
    if A.left:         # A has left substree, it might also have right subtree
      B = A.predecessor()
    else:              # A only has right subtree
      B = A.successor()
    A.item, B.item = B.item, A.item
    return B.sub_tree_delete()
  else:                # A is a leaf node
    if (A is A.parent.left): A.parent.left = None
    else: A.parent.right = None
    
