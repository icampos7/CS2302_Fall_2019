'''
Author: Carlos Fernando Castaneda
Class : CS 2302 
Date Modified: September 16, 2019 
Instructor: Diego Aguirre 
Assingment: Lab 2 Linked Lists
TA: Gerardo Barraza
Purpose: To practice using linked lists and to apply the
knowledge of running times to compare different sorting
methods.
'''

#Used to calculate the time for each method
import time

#Node Functions given to us by the lab report
class Node(object):
   item = -1
   next = None
   # Constructor
   def __init__(self, item = -1, next = None):
        self.item = item
        self.next = next
        
   def print_list(self):
        curr = self
        while curr is not None:
            print(curr.item)
            curr = curr.next
#List Functions
class List(object):   
    # Constructor
    head = None
    tail = None
    size = 0

    def __init__(self, node: Node = None):
        if node is None:
            self.head = None
            self.tail = None
            self.size = 0
            return

        if node.next is None:
            self.head = node
            self.tail = node
            self.size = 1
            
    def insert_head(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
            self.size += 1
            return
        curr_node = Node(data)
        curr_node.next = self.head
        self.head = curr_node
        self.size += 1   
        
    def print(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.item)
            curr_node = curr_node.next
    def append_list(self, list):
        # if added list is empty return
        if list.size is 0:
            return

        # if self is empty return
        if self.size is 0:
            return

        # combine both sizes
        self.size += list.size

        # add list to the tail of self
        self.tail.next = list.head
        self.tail = list.tail
        
    def find_max(self) -> int:
        if self.head is None:
            return -1

        #set pointer and max variable
        max_num = self.head.item
        curr_node = self.head

        # find max item on the list
        while curr_node is not None:
            if curr_node.item > max_num:
                max_num = curr_node.item
            curr_node = curr_node.next

        return max_num
#Makes a new empty list
def NewList(L):
    L.head = None
    L.tail = None
    L.Len = 0

    
def file_to_linked_list(file_name):
    # Open file to read
    file = open(file_name, 'r')

    # Linked List files
    linked_list = List()

    # add file ids to the linked lists
    for line in file:
        linked_list.insert_head(int(line))

    file.close()
    return linked_list

#Sorting Algorithm Functions

#Solution 1
def get_duplicate_ids(linked_list):
    # make two pointers to compare nodes
    pointer1 = linked_list.head
    pointer2 = pointer1.next
    duplicate_ids = []
    
    #traverse all pointer combinations and find the duplicates
    while pointer1.next is not None:
        while pointer2 is not None:
            if pointer1.item == pointer2.item:
                duplicate_ids.append(pointer1.item)
            pointer2 = pointer2.next
        pointer1 = pointer1.next
        pointer2 = pointer1.next

    # return duplicates
    return duplicate_ids
    
#Solution 2
def BubbleSort(L):
    if IsEmpty(L):
        return None
    else:
        Current = L.head
        Completed = False
        while Completed != True:
            Completed = True
            Current = L.head
            while Current.next is not None:
                if Current.item > Current.next.item:
                    nextItem = Current.next.item
                    Current.next.item = Current.item
                    Current.item = nextItem
                    Completed = False
                Current = Current.next

#Solution 3
def MergeSort(L):
    if L.Len > 1:
        L1 = List()
        L2 = List()
        NewLength = L.Len//2
        Current = L.head 
        
        for i in range(NewLength):
            Append(L1, Current.item)
            Current= Current.next
            
        while Current != None:
            Append(L2, Current.item)
            Current = Current.next
            
        MergeSort(L1)
        MergeSort(L2)
        NewList(L)
        MergeList(L, L1, L2)

# Inserts x at end of list L   
def Append(L,x): 
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
        L.Len = L.Len + 1
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        L.Len = L.Len + 1

#States if the current List is empty or not
def IsEmpty(L):
    return L.head == None
        
# Appends sorted Lists into L
def MergeList(L,L1,L2):
    #Grabs the two head of each respective list. Called the variables current as it is the current item the algorithm is analyzing
    Current1 = L1.head
    Current2 = L2.head
    while Current1 != None and Current2 != None:
        #Adds the lowest term first of either list
        if Current1.item < Current2.item:
            Append(L, Current1.item)
            Current1 = Current1.next
        else:
            Append(L, Current2.item)
            Current2 = Current2.next 
    #Clarifies that if either list contains any elements, if so, they will add any remaining items to the new list
    if Current1 is None:
        while Current2 != None:
            Append(L, Current2.item)
            Current2 = Current2.next
    if Current2 is None:
        while Current1 != None:
            Append(L, Current1.item)
            Current1 = Current1.next
            
#Solution 4
def find_duplicates(list):
    #make list to see if the number is duplicate
    is_id_listed = []
    for i in range(list.find_max() + 1):
        is_id_listed.append(False)

    #traverse the id and return numbers that are already on list
    duplicate_ids = []
    curr_node = list.head
    while curr_node is not None:
        # if id is listed already then add it to duplicate list
        if is_id_listed[curr_node.item]:
            duplicate_ids.append(curr_node.item)

        # check id as already visited
        is_id_listed[curr_node.item] = True
        curr_node = curr_node.next

    return duplicate_ids
          
L1 = 'activision.txt'
L2 = 'vivendi.txt'
print('Original list: ')
print('')
activision = file_to_linked_list(L1)
vivendi = file_to_linked_list(L2)

L3 = activision
L3.append_list(vivendi)

duplicated = get_duplicate_ids(L3)
print(len(duplicated))

duplicate_ids = find_duplicates(L3)
print(len(duplicate_ids))
print('')