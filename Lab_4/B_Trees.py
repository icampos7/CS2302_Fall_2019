'''
Author: Carlos Fernando Castaneda
Class : CS 2302 
Date Modified: October 29, 2019 
Instructor: Diego Aguirre 
Assingment: Lab 4 B Trees (Part 4 of 4)
TA: Gerardo Barraza
Purpose: To practice using B Trees to 
solve the problem faced from Lab 3.
'''
# This class in the program is used to create objects of BTrees, or binary trees
class BTreeNode:
    # Constructor
    def __init__(self, item=[], child=[], is_leaf=True, max_items=5):
        self.keys = item
        self.child = child
        self.is_leaf = is_leaf
        #If the max item will equal 3 if it is less than 3
        if max_items < 3:  
            max_items = 3
            #If the max items is not odd or greater than 3, it will change it so that it must be odd and greater or equal to 3
        if max_items % 2 == 0: 
            max_items += 1
        self.max_items = max_items
    
    #Will return if the leaves are full or not
    def is_full(self):
        return len(self.keys) >= self.max_items

#Method that acts as the operator of the B Tree operations
class BTree:
    #Creates the Constructor
    def __init__(self, max_items=5):
        self.max_items = max_items
        self.root = BTreeNode(max_items=max_items)

    # Method that is used to find the correct index position of child
    def FindChild(self, k, node=None):  
        if node is None:
            node = self.root
        key_num = 0
        for i in range(len(node.keys)):
            key = node.keys[i]
            key_num = k[1] 
            if key_num < key[1]:
                return i
        return len(node.keys)
    
    #Method that is used to insert items into the binary tree into non-leaf nodes
    def InsertInternal(self, i, node=None):
        if node is None:
            node = self.root
        if node.is_leaf:
            self.InsertLeaf(i, node)
        else:
            k = self.FindChild(i, node)
            if node.child[k].is_full():
                m, l, r = self.split(node.child[k])
                node.keys.insert(k, m)
                node.child[k] = l
                node.child.insert(k + 1, r)
                k = self.FindChild(i, node)
            self.InsertInternal(i, node.child[k])
    
    # Method is used to split full nodes to be used throughout the tree
    def split(self, node=None):
        if node is None:
            node = self.root
        mid = node.max_items // 2
        if node.is_leaf:
            leftChild = BTreeNode(node.keys[:mid], max_items=node.max_items)
            rightChild = BTreeNode(node.keys[mid + 1:], max_items=node.max_items)
        else:
            leftChild = BTreeNode(node.keys[:mid], node.child[:mid + 1], node.is_leaf, max_items=node.max_items)
            rightChild = BTreeNode(node.keys[mid + 1:], node.child[mid + 1:], node.is_leaf, max_items=node.max_items)
        return node.keys[mid], leftChild, rightChild
    
    # Method that is used to get number of leaves that are full in the tree
    def InsertLeaf(self, i, node=None):
        if node is None:
            node = self.root
        node.keys.append(i)
        node.keys.sort(key = lambda r:r[1])
    
    # Method that is used to get number of leaves that are full in the tree
    def leaves(self, node=None):
        if node is None:
            node = self.root
        if node.is_leaf:
            return [node.keys]
        s = []
        for c in node.child:
            s = s + self.leaves(c)
        return s
    
    # Method is used to insert items into the nodes of the tree
    def Insert(self, i, node=None):
        if node is None:
            node = self.root
        if not node.is_full():
            self.InsertInternal(i, node)
        else:
            m, l, r = self.split(node)
            node.keys = [m]
            node.child = [l, r]
            node.is_leaf = False
            k = self.FindChild(i, node)
            self.InsertInternal(i, node.child[k])
    
    # Method that is used to find height of tree
    def height(self, node=None):
        if node is None:
            node = self.root
        if node.is_leaf:
            return 0
        return 1 + self.height(node.child[0])
    
    # Method is used to search item in a B Tree
    def Search(self, k, node=None):
        if node is None:
            node = self.root
        for i in range(len(node.keys)): 
            key = node.keys[i]
            if (k[1] == key[1]):
                return node
        if node.is_leaf:
            return None
        return self.Search(k, node.child[self.FindChild(k, node)])