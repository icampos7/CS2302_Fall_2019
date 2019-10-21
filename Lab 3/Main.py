'''
Author: Carlos Fernando Castaneda
Class : CS 2302 
Date Modified: October 14, 2019 
Instructor: Diego Aguirre 
Assingment: Lab 3 Binary Trees
TA: Gerardo Barraza
Purpose: To practice using multiple methods
of creating Binary Trees, includong AVL and
Red-Black.
'''
#AVL Constructor
class Node1:
    def __init__(self, item=None, left=None, right=None, parent=None):
        self.item = item
        self.left = left
        self.right = right
        self.parent = parent
        self.height = 0
        self.embedding = []


    def AVLTreeSetChild(self, whichChild: str, child):
        if whichChild is not "left" and whichChild is not "right":
            return False
        if whichChild is "left":
            self.left = child
        else:
            self.right = child
        if child is not None:
            child.parent = self
        self.update_height()
        return True

    def AVLTreeReplaceChild(self, currentChild, newChild):
        if self.left is currentChild:
            return self.set_child("left", newChild)
        elif self.right is currentChild:
            return self.set_child("right", newChild)
        return False

    def AVLTreeUpdateHeight(self):
        left_height = -1
        if self.left is not None:
            left_height = self.left.height
        right_height = -1
        if self.right is not None:
            right_height = self.right.height

        self.height = max(left_height, right_height) + 1

    def AVLTreeGetBalance(self):
        left_height = -1
        if self.left is not None:
            left_height = self.left.height

        right_height = -1
        if self.right is not None:
            right_height = self.right.height

        return left_height - right_height

    def separate_word_and_embedding(self):
        words = self.item.split()
        self.item = words.pop(0)
        self.embedding = words
        
#AVL Operations
class AVL_Tree:
    def __init__(self, item=None):
        self.root = Node1(item)

    def rotate_left(self, node):
        right_left_child = node.right.left
        if node.parent is not None:
            node.parent.replace_child(node, node.right)

        else:
            self.root = node.right
            self.root.parent = None

        node.right.set_child("left", node)
        node.set_child("right", right_left_child)

    def rotate_right(self, node):
        left_right_child = node.left.right
        if node.parent is not None:
            node.parent.replace_child(node, node.left)
        else:
            self.root = node.left
            self.root.parent = None
        node.left.set_child("right", node)
        node.set_child("left", left_right_child)

    def rebalance(self, node):
        node.update_height()
        if node.get_balance() == -2:
            if node.right.get_balance() == 1:
                self.rotate_right(node.right)
            return self.rotate_left(node)

        elif node.get_balance() == 2:
            if node.left.get_balance() == -1:
                self.rotate_left(node.left)
            return self.rotate_right(node)

        return node

    def bts_search(self, item):
        cur = self.root
        while cur is not None:
            if item == cur.item:
                return cur
            elif item < cur.item:
                cur = cur.left
            else:
                cur = cur.right
        return None

    def insert(self, item):
        if self.root is None or self.root.item is None:      # Root is None
            self.root = Node1(item)
            return

        cur = self.root
        node = Node1(item)
        while cur is not None:
            if item < cur.item:
                if cur.left is None:
                    cur.left = node
                    node.parent = cur
                    cur = None
                else:
                    cur = cur.left

            else:
                if cur.right is None:
                    cur.right = node
                    node.parent = cur
                    cur = None
                else:
                    cur = cur.right

        node = node.parent
        while node is not None:
            self.rebalance(node)
            node = node.parent

    def num_nodes(self, node):
        if node is None:
            return 0
        return self.num_nodes(node.left) + self.num_nodes(node.right) + 1

    def height(self, node):
        if node is None:
            return -1

        return max(self.height(node.left), self.height(node.right)) + 1


    def print(self, node):
        if node is None:
            return


        self.print(node.left)
        print(node.item)
        self.print(node.right)

    def AVLSeparateEmbeddings(self, node: Node1):
        if node is None:
            return

        node.separate_word_and_embedding()
        self.separate_all_embeddings(node.left)
        self.separate_all_embeddings(node.right)

#RB Constructor       
class Node2(object):
    def __init__(self, item=None, left=None, right=None, parent=None):
        self.item = item
        self.left = left
        self.right = right
        self.parent = parent
        self.color = ""
        self.embedding = []

    def RBTreeSetChild(self, whichChild: str, child):
        if whichChild is not "left" and whichChild is not "right":
            return False
        if whichChild is "left":
            self.left = child
        else:
            self.right = child
        if child is not None:
            child.parent = self
        return True

    def RBTreeReplaceChild(self, currentChild, newChild):
        if self.left is currentChild:
            return self.set_child("left", newChild)
        elif self.right is currentChild:
            return self.set_child("right", newChild)
        return False

    def RBTreeGetGrandparent(self):
        if self.parent is None:
            return None
        return self.parent.parent

    def RBTreeGetUncle(self):
        grandparent = None
        if self.parent is not None:
            grandparent = self.parent.parent
        if grandparent is None:
            return None
        if grandparent.left is self.parent:
            return grandparent.right
        else:
            return grandparent.left

    def get_sibling(self):
        if self.parent is not None:
            if self is self.parent.left:
                return self.parent.right
            return self.parent.left
        return None

    def get_predecessor(self):
        cur = self.left
        while cur.right is not None:
            cur = cur.right
        return cur

    def are_both_children_black(self) -> bool:
        if self.left is not None and self.left.color is "red":
            return False
        if self.right is not None and self.right.color is "red":
            return True

    def separate_word_and_embedding(self):
        words = self.item.split()
        self.item = words[0]
        self.embedding = words.pop(0)
        
#Red_Black Operations        
class RB_Tree:
    def __init__(self, item=None):
        self.root = Node2(item)

    def RBTreeRotateLeft(self, node):
        right_left_child = node.right.left
        if node.parent is not None:
            node.parent.replace_child(node, node.right)
        else:
            self.root = node.right
            self.root.parent = None
        node.right.RBTreeSetChild("left", node)
        node.RBTreeSetChild("right", right_left_child)

    def RBTreeRotateRight(self, node):
        left_right_child = node.left.right
        if node.parent is not None:
            node.parent.replace_child(node, node.left)
        else:
            self.root = node.left
            self.root.parent = None
        node.left.RBTreeSetChild("right", node)
        node.RBTreeSetChild("left", left_right_child)

    def bst_search(self, item):
        cur = self.root
        while cur is not None:
            if item == cur.item:
                return cur
            elif item < cur.item:
                cur = cur.left
            else:
                cur = cur.right
        return None

    def bst_insert(self, node: Node2) -> Node2:
        if self.root is None or self.root.item is None:
            self.root = node
        else:
            cur = self.root
            while cur is not None:
                if node.item < cur.item:
                    if cur.left is None:
                        cur.left = node
                        node.parent = cur
                        cur = None
                    else:
                        cur = cur.left
                else:
                    if cur.right is None:
                        cur.right = node
                        node.parent = cur
                        cur = None
                    else:
                        cur = cur.right
        return node

    def bst_remove(self, item):
        par = None
        cur = self.root
        while cur is not None:
            if cur.item == item:
                if cur.left is None and cur.right is None:  # Remove Leaf
                    if par is None:
                        self.root = None
                    elif par.left is cur:
                        par.left = None
                    else:
                        par.right = None

                elif cur.left is not None and cur.right is None: # Remove node with only left child
                    if par is None:
                        self.root = cur.left
                    elif par.left is cur:
                        par.left = cur.left
                    else:
                        par.right = cur.left

                elif cur.left is None and cur.right is not None:
                    if par is None:
                        self.root = cur.right
                    elif par.left is cur:
                        par.left = cur.right
                    else:
                        par.right = cur.right

                else:
                    suc = cur.right
                    while suc.left is not None:
                        suc = suc.left
                    suc_item = suc.item
                    self.bst_remove(suc.item)
                    cur.item = suc_item
                return

            elif cur.item < item:
                par = cur
                cur = cur.right

            else:
                par = cur
                cur = cur.left

        return

    def balance(self, node):
        if node.parent is None:  # Parent is None
            node.color = "black"
            return

        if node.parent.color is "black":  # Parent color is Black
            return

        parent = node.parent
        grandparent = node.get_grandparent()
        uncle = node.get_uncle()

        if uncle is not None and uncle.color is "red":
            parent.color = uncle.color = "black"
            grandparent.color = "red"
            self.balance(grandparent)
            return

        if node is parent.right and parent is grandparent.left:
            self.rotate_left(parent)
            node = parent
            parent = node.parent

        elif node is parent.left and parent is grandparent.right:
            self.rotate_right(parent)
            node = parent
            parent = node.parent

        parent.color = "black"
        grandparent.color = "red"

        if node is parent.left:
            self.rotate_right(grandparent)
        else:
            self.rotate_left(grandparent)

    def insert(self, item):
        node = Node2(item)
        self.bst_insert(node)
        node.color = "red"
        self.balance(node)


    def print(self, node):
        if node is None:
            return

        print(node.item)
        self.print(node.left)
        self.print(node.right)

    def separate_all_embeddings(self, node: Node2):
        if node is None:
            return

        node.separate_word_and_embedding()
        self.separated_all_embeddings(node.left)
        self.separated_all_embeddings(node.right)        

#Print anagram
def print_anagrams(english_words, word, prefix=""):
    if len(word) <= 1:
        str = prefix + word

        if str in english_words:
            print(prefix + word)
        else:
            print(prefix + word)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]  # letters before cur
            after = word[i + 1:]  # letters after cur

            if cur not in before:  # Check if permutations of cur have not been generated.
                print_anagrams(english_words, before + after, prefix + cur)

#Count anagram
def CountAnagrams(english_words):
    print("Count anagrams of: ")
    word = input()
    word = word.replace("\n", "")
    print('Total anagrams of ', word, ': ', _count_anagrams(english_words, word, []))
    
def _count_anagrams(english_words, word, li, prefix=""):
    if len(word) <= 1:
        str = prefix + word
        if english_words.contains(str):
            li.append(prefix + word)
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i]  # letters before cur
            after = word[i + 1:]  # letters after cur

            if cur not in before:  # Check if permutations of cur have not been generated.
                _count_anagrams(english_words, before + after, li, prefix + cur)
    return len(li)

#count_greatest anagram
def count_greatest(english_words):
    anagram_gr = []
    for word in english_words:
        if not anagram_gr:
            anagram_gr.append(word)
            anagram_gr.append(_count_anagrams(english_words, word, []))
        else:
            count = _count_anagrams(english_words, word, [])
            if count > anagram_gr[1]:
                anagram_gr[0] = word
                anagram_gr[1] = count
    print('This word:', anagram_gr[1])       
    print(' has the greatest number of anagrams with a number of', anagram_gr[1])
    
#Main method
'''
print("Welcome to the Anagram program! Please select the method of organizing the word.txt file:")
print("1. AVL Tree")
print("2. Red-Black Tree")
print("")
L1 = input("Choice:")
errorCount=0
if L1!=1 or L1!=2:
    print("Not a valid input, try again!")
    errorCount+=1
    L1 = input("Choice:")
if errorcount == 3:
    print("Error amount exceeded. Goodbye!")
if L1 == 1:
    print("Excellent! Arranging tree via AVL method:")
if L1 == 2:
    print("Excellent! Arranging tree via Red-Black method:")
'''