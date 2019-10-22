class AVLNode(object): 
    def __init__(self, word, key, left = None, parent = None, right = None): 
        self.word = word #Added attribute 
        self.key = 0
        self.left = None
        self.parent = None
        self.right = None
        self.height = -1
        
class AVLTree(object): 

    def __init__(self, root = None): 
        self.root = None 
        
    def AVLTreeUpdateHeight(self, node): 
        left_height = -1
        if (node.left != None):
            left_height = node.left.height 
        right_height = -1
        if (node.right != None):
            right_height = node.right.height
        node.height = max(left_height, right_height) + 1    
        
    def AVLTreeSetChild(self, parent, which_child, child): 
        if (which_child != "left" and which_child != "right"):
            return False
        if (which_child == "left"):
            parent.left = child
        else:
            parent.right = child
        if (child != None):
            child.parent = parent
        self.AVLTreeUpdateHeight(parent)
        return True
    
    def AVLTreeReplaceChild(self, parent, curr_child, new_child): 
        if (parent.left == curr_child):
            return self.AVLTreeSetChild(parent, "left", new_child)
        elif (parent.right == curr_child):
            return self.AVLTreeSetChild(parent, "right", new_child)
        return False
    
    def AVLTreeGetBalance(self, node):
        left_height = -1
        if (node.left != None):
            left_height = node.left.height
        right_height = -1
        if (node.right != None):
            right_height = node.right.height
        return left_height - right_height
    
    def AVLTreeRotateRight(self, node): 
        left_right_child = node.left.right
        if (node.parent != None):
            self.AVLTreeReplaceChild(node.parent, node, node.left)
        else: # node is root
            self.root = node.left
            self.root.parent = None
    
        self.AVLTreeSetChild(node.left, "right", node)
        self.AVLTreeSetChild(node, "left", left_right_child)

    def AVLTreeRotateLeft(self, node): 
        right_left_child = node.right.left
        if (node.parent != None):
            self.AVLTreeReplaceChild(node.parent, node, node.right)
        else: 
            self.root = node.right
            self.root.parent = None
        self.AVLTreeSetChild(node.right, "left", node)
        self.AVLTreeSetChild(node, "right", right_left_child)
        
    def AVLTreeRebalance(self, node): 
        self.AVLTreeUpdateHeight(node)        
        if (self.AVLTreeGetBalance(node) == -2): 
            if (self.AVLTreeGetBalance(node.right) == 1): 
                self.AVLTreeRotateRight(node.right)
            return self.AVLTreeRotateLeft(node)
        elif (self.AVLTreeGetBalance(node) == 2): 
            if (self.AVLTreeGetBalance(node.left) == -1):  
                self.AVLTreeRotateLeft(node.left)
            return self.AVLTreeRotateRight(node)
        return node
    
    def AVLTreeInsert(self, words, key): 
        node = AVLNode(words, key)
        node.key = key
        if (self.root == None): 
            self.root = node
            node.parent = None 
            return 
        cur = self.root 
        while (cur != None): 
            if (node.key < cur.key): 
                if (cur.left == None): 
                    cur.left = node
                    node.parent = cur
                    cur = None
                else:
                    cur = cur.left
            else:
                if (cur.right == None): 
                    cur.right = node
                    node.parent = cur
                    cur = None
                else:
                    cur = cur.right
        node = node.parent
        while (node != None): 
            self.AVLTreeRebalance(node)
            node = node.parent