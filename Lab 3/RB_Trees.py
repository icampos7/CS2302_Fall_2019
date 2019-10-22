'''
Author: Carlos Fernando Castaneda
Class : CS 2302 
Date Modified: October 21, 2019 
Instructor: Diego Aguirre 
Assingment: Lab 3 Binary Trees (Part 3 of 3)
TA: Gerardo Barraza
Purpose: To practice using multiple methods
of creating Binary Trees, includong AVL and
Red-Black.
'''
class RBNode(object): 
	def __init__(self, word = "", key = 0, left = None, parent = None, right = None, color = -1): 
		self.word = word 
		self.key = 0
		self.left = None
		self.parent = None
		self.right = None
		self.color = -1 

class RedBlack(object):
    def __init__(self, root = None):
        self.root = None
        
    def RBTreeSetChild(self, parent, which_child, child):
        if (which_child != "left" and which_child != "right"):
            return False
        if (which_child == "left"):
            parent.left = child
        else:
            parent.right = child
        if (child != None):
            child.parent = parent
        return True
    
    def RBTreeReplaceChild(self, parent, current_child, new_child):
        if (parent.left == current_child):
            return self.RBTreeSetChild(parent, "left", new_child)
        elif (parent.right == current_child):
            return self.RBTreeSetChild(parent, "right", new_child)
        return False  
    
    def RBTreeRotateLeft(self, node):
        right_left_child = node.right.left
        if (node.parent != None):
            self.RBTreeReplaceChild(node.parent, node, node.right)
        else:
            self.root = node.right
            self.root.parent = None
        self.RBTreeSetChild(node.right, "left", node)
        self.RBTreeSetChild(node, "right", right_left_child)
       
    def RBTreeRotateRight(self, node):
        left_right_child = node.left.right
        if (node.parent != None):
            self.RBTreeReplaceChild(node.parent, node, node.left)
        else:
            self.root = node.left
            self.root.parent = None
        self.RBTreeSetChild(node.left, "right", node)
        self.RBTreeSetChild(node, "left", left_right_child)
    
    def RBTreeInsert(self, words, key):
        node = RBNode(words, key)
        node.key = key
        self.BSTinsert(node)
        node.color = 1
        self.RBTreeBalance(node)
        
    def RBTreeGetGrandparent(self, node):
        if (node.parent == None):
            return None 
        return node.parent.parent
    
    def RBTreeGetUncle(self, node):
        grandparent = None
        if (node.parent != None):
            grandparent = node.parent.parent
        if (grandparent == None):
            return None
        if (grandparent.left == node.parent):
            return grandparent.right
        else:
            return grandparent.left
    def RBTreeBalance(self, node):
        if (node.parent == None):
            node.color = 0
            return
        if (node.parent.color == 0):
            return
        parent = node.parent
        grandparent = self.RBTreeGetGrandparent(node)
        uncle = self.RBTreeGetUncle(node)
        if (uncle != None and uncle.color == 1):
            parent.color = uncle.color = 0
            grandparent.color = 1
            self.RBTreeBalance(grandparent)
            return
        if (node == parent.right and parent == grandparent.left):
            self.RBTreeRotateLeft(parent)
            node = parent
            parent = node.parent
        elif (node == parent.left and parent == grandparent.right):
            self.RBTreeRotateRight(parent)
            node = parent
            parent = node.parent
        parent.color = 0
        grandparent.color = 1
        if (node == parent.left):
            self.RBTreeRotateRight(grandparent)
        else:
            self.RBTreeRotateLeft(grandparent)
            
    def BSTinsert(self, node):
        if (self.root == None):
            self.root = node
            node.left = None
            node.right = None
        else:
            cur = self.root
            while (cur != None):
                if (node.key < cur.key):
                    if (cur.left == None):
                        cur.left = node
                        cur = None
                    else:
                        cur = cur.left
                else:
                    if (cur.right == None):
                        cur.right = node
                        cur = None
                    else:
                        cur = cur.right            
            node.left = None
            node.right = None