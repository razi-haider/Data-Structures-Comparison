
class Node:
    def __init__(self, value = None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
  
  #Binary Search
    def find(self, value):
        node=self
        while node:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return node.value
    def min(self):
        node=self
        while node and node.left:
            node = node.left
        return node
    def max(self):
        node=self
        while node and node.right:
            node = node.right
        return node

    def inorder_traversal(self):
        self.__listOfNodes = []
        self.__inorderTraversal(self)
        print(self.__listOfNodes)

    def __inorderTraversal(self, node):
        if node!=None:
            self.__inorderTraversal(node.left)
            self.__listOfNodes.append(node.value)
            self.__inorderTraversal(node.right)  
    def insert(self, value, node=None, root=True):
        
        if root:
            node = self
        if node is None:
            return Node(value)
        if self.value is None:
            self.value = value
            return self
        
        if value < node.value:
            node.left = self.insert(value, node.left, False)

        elif value > node.value:
            node.right = self.insert(value, node.right, False)
        else:
            #Duplicate value, ignore it
            return node
        return node
    
    
    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left

        return current 
    
    def delete(self, value, node=None, root=True):
        if root:
            node=self
        #best Case
        if node is None:
            return None

        if value < node.value:
            node.left = self.delete(value, node.left, False)
        elif value > node.value:
            node.right = self.delete(value, node.right, False)

        else:
            # Node with only one child or no child
            if node.left is None:
                temp = node.right
                node = None
                return temp
    
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            
            # Node with two children:
            # Get the inorder successor
            # (smallest in the right subtree)
            temp = self.minValueNode(node.right)

            # Copy the inorder successor's
            # content to this node
            node.value = temp.value

             # Delete the inorder successor
            node.right = self.delete(temp.value,node.right, False)
        return node   

               
        