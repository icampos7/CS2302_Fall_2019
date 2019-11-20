'''
Author: Carlos Fernando Castaneda
Class : CS 2302 
Date Modified: November 14, 2019 
Instructor: Diego Aguirre 
Assingment: Lab 5 LRU (2 0f 3)
TA: Gerardo Barraza
Purpose: To practice using queues and
hash tables to create a LRU cache.
'''
#Creates the node values necessary 
class Node(object): 
    def __init__(self, key, val, prev = None, next = None, empty = False): #Constructor for the node (doubly linked list node).
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        self.empty = empty
  
#Creates the LRU_Cache class necessary to perform the operations for problem 1      
class LRU(object): 
    def __init__(self, max_capacity, size = 0, head = None, tail = None, table = {}): #Constructor for LRU. Set up like a doubly linked list with a hash table.
        self.size = size
        self.head = head 
        self.tail = tail
        self.table = table
        self.max_capacity = max_capacity
    
    #Method that creates the nodes, the necessary linked list, and populates a new hash table to traverse through the cache. 
    def put(self, key, val):
        #If list is empty, it will create a new node and make it its head. 
        if (self.head is None):  
            self.head = Node(key, val)
            self.tail = self.head
            self.table[key] = self.head
            self.size += 1
            return
        #If  the key is already in the table, then it overrides the key values.    
        if (key in self.table): 
            if(key == self.head.key): 
                self.head.val = val
            node = self.table.get(key)
            node.val = val 
            return
        #If the size is at its maximum capacity or greater.    
        if (self.size >= self.max_capacity): 
            #If the tail node is none, it then overrides the head. 
            if (self.tail.next is None): 
                self.head.key = key 
                self.head.val = val 
                node = Node(key, val) 
                self.table[key] = node
                self.tail = self.head
                return
            #Otherwise, it overrides the next node that needs to be overridden.   
            else: 
                node = self.tail.next 
                node.key = key
                node.val = val
                self.tail = node
                self.table[key] = node
                return
        #If the list is not at its full capacity, it adds the nodes to the dictionary.        
        node = Node(key, val) 
        self.tail.next = node
        node.prev = self.tail
        self.tail = node 
        self.table[key] = node
        self.size = self.size + 1
        return
    
    #Uses a dictionary to get a value of the key if it currently exists in the cache.
    def get(self, key): 
        #If the current head is none, it will return -1, indicating that its empty.
        if (self.head is None):
            return -1 
        #Sets the current node to the current key
        curr_node = self.table.get(key) 
        #If the node is None, it will return -1, indicating there is nothing
        if curr_node == None: 
            return -1 
        #Returns the value of the current node
        return curr_node.value
    
    #Prints the list in order of the LRU cache until it reaches the end of the list. 
    def print_inorder(self): 
        #If the head is None, it will return an error message.
        if self.head is None: 
            print("ERROR! The current head is None. Farewell.") 
            return 
        #Sets an iterative value for the current head
        iter = self.head 
        #While the ieration is not none, it will print the iterative key and its value for each key.
        while(iter != None): 
            print("Current Key:", iter.key, "|","Key Value:", iter.val) 
            iter = iter.next 
        print("")
        print("Current size of Keys:", self.size)
        print("Maximum capacity of Cache:", self.max_capacity)
        
    #Returns the number of key/value pairs that are currently stored in the cache.
    def size(self):  
        return self.size

    #Returns the maximum capacity that is currently applied in the cache. 
    def max_capacity(self): 
        return self.max_capacity
            
    
        
    