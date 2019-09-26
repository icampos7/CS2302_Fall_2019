'''
Author: Carlos Fernando Castaneda
Class : CS 2302 
Date Modified: September 24, 2019 
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
    #Default constructors
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
            
    #Method that adds a new head to the linked list      
    def add_head(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
            self.size += 1
            return
        curr_node = Node(data)
        curr_node.next = self.head
        self.head = curr_node
        self.size += 1   
        
    #Method that prints all the contents of a list    
    def print(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.item)
            curr_node = curr_node.next
            
    #Method that combines one list to another, we will use this to combine activision and vivendi
    def combine_list(self, list):
        if list.size is 0:
            return
        if self.size is 0:
            return
        self.size += list.size
        self.tail.next = list.head
        self.tail = list.tail
        
    #Method that finds the maximum number in the list
    def find_max(self) -> int:
        if self.head is None:
            return -1
        max_num = self.head.item
        curr_node = self.head
        while curr_node is not None:
            if curr_node.item > max_num:
                max_num = curr_node.item
            curr_node = curr_node.next

        return max_num
    
    # This function counts number of nodes in the linked list. 
    def getCount(self): 
        temp = self.head
        count = 0  
        while (temp): 
            count += 1
            temp = temp.next
        return count 
    
    #Solution 1
    #Method that compares elements of a list from its neighbor, and determine if they are duplicate. At the end it will return the number of duplicates found in the list.
    def compare_num(self):
        duplicate = 0
        cur_node = self.head
        while cur_node is not None:
            next_node = cur_node.next
            while next_node is not None:
                if int(cur_node.item) == int(next_node.item):
                    duplicate += 1
                    break
                next_node = next_node.next
            cur_node = cur_node.next
        return duplicate

#Makes a new empty list
def NewList(L):
    L.head = None
    L.tail = None
    L.Len = 0

#Method that reads the content of a text file and turns into a brand new linked list
def Text_to_list(txt):
    file = open(txt, 'r')
    L = List()
    for line in file:
        L.add_head(int(line))
    file.close()
    return L

#Sorting Algorithm Functions
  
#Solution 2
    
#Method that arranges a given list using bubble sort.
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
                
#Method that arranges a given list using merge sort.
def MergeSort(L):
    L.Len = L.getCount()
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

# Method that inserts x at end of list L   
def Append(L,x):
    L.Len = L.getCount()
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
        L.Len = L.Len + 1
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        L.Len = L.Len + 1

#Method that states if the current List is empty or not
def IsEmpty(L):
    return L.head == None
        
#Method that appends sorted Lists into a new list L.
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
#Method that searches for duplicates 
def Search_duplicates(list):
    #Will use a list to see if the number is duplicate
    listedID = []
    for i in range(list.find_max() + 1):
        listedID.append(False)

    #Will create a list that will add Duplicated items
    Duplicate = []
    curr_node = list.head
    while curr_node is not None:
        # If the ID is listed, then it will be added it to the duplicate list
        if listedID[curr_node.item]:
            Duplicate.append(curr_node.item)
        listedID[curr_node.item] = True
        curr_node = curr_node.next
    return Duplicate

print('Welcome to the Activision ID generator! Before we begin, please state the following... ')
L1 = input("Name of the first text file : ") 
print(L1)
L2= input("Name of the second text file : ") 
print(L2)
print('Excellent, commencing program now:')
print('')
activision = Text_to_list(L1)
vivendi = Text_to_list(L2)

L3 = activision
L3.combine_list(vivendi)
L3_COPY_1 = L3
L3_COPY_2 = L3
#Solution 1
#Starts a timer that will calculate the total running time for the solution
start1 = time.time()
print('Beginning without sorting:')
print('Comparing if neighbor head is identical to another... ')
comparison1 =  L3.compare_num()
print('Result: ',comparison1)
print('Resulted List:')
L3.print()
print()
#Ends the timer used to calculate the running time
end1 = time.time()
print()

#Prints out the running time needed for this solution
print('Running time was: ', end1 - start1, 'seconds.')

#Solution 2
#Starts a timer that will calculate the total running time for the solution
start2 = time.time()
print('Sending list through bubble sort... ')
BubbleSort(L3_COPY_1)
print('Comparing if neighbor head is identical to another... ')
comparison2 =  L3_COPY_1.compare_num()
print('Result: ',comparison2)
print('Resulted List:')
L3.print()
print()
#Ends the timer used to calculate the running time
end2 = time.time()

#Prints out the running time needed for this solution
print('Running time was: ', end2 - start2, 'seconds.')
print()

#Solution 3
#Starts a timer that will calculate the total running time for the solution
start3 = time.time()
print('Sending list through merge sort... ')
MergeSort(L3_COPY_2)
print('Comparing if neighbor head is identical to another... ')
comparison3 =  L3_COPY_2.compare_num()
print('Result: ',comparison3)
print('Resulted List:')
L3.print()
print()
#Ends the timer used to calculate the running time
end3 = time.time()

#Prints out the running time needed for this solution
print('Running time was: ', end3 - start3, 'seconds.')
print()

#Solution 4
#Starts a timer that will calculate the total running time for the solution
start4 = time.time()
print('Finding the number of duplicates in the combined list... ')
duplicate_ids = Search_duplicates(L3)
print(len(duplicate_ids))
print('Resulted List:')
L3.print()
print('Resulted Duplicates: ')
print(duplicate_ids)
#Ends the timer used to calculate the running time
end4 = time.time()
print('')

#Prints out the running time needed for this solution
print('Running time was: ', end4 - start4, 'seconds.')
print()