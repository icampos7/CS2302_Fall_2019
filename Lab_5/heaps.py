'''
Author: Carlos Fernando Castaneda
Class : CS 2302 
Date Modified: November 14, 2019 
Instructor: Diego Aguirre 
Assingment: Lab 5 LRU (3 0f 3)
TA: Gerardo Barraza
Purpose: To practice using queues and
hash tables to create a LRU cache.
'''
#Used to return error messages to the user if the need arises
import math

# This class in the program is used to create objects of a max Heap
class MaxHeap(object):
    def __init__(self):
        self.tree = []
        
    #Will return if its empty or not
    def is_empty(self):
        return len(self.tree) == 0

    #Will return the index of the parent
    def parent(self, i):
        if i == 0:
            return -math.inf
        parent_list = self.tree[(i - 1) // 2]

        return parent_list[1]
    #Will return the index of the right child
    def right_child(self, i):
        c = 2 * i + 2
        if c >= len(self.tree):
            return -math.inf
        c_list = self.tree[c]
        return c_list[1]
    
    #Will return the index of the left child
    def left_child(self, i):  
        c = 2 * i + 1
        if c >= len(self.tree):
            return -math.inf
        c_list = self.tree[c] 
        return c_list[1]

    #Will insert the new item and percolate up so that it balances the heap
    def insert(self, item):
        self.tree.append(item)
        self.percolate_up(len(self.tree) - 1)
        
    #Method that helps balance of the heap correctly by swapping items until the correct order is met while also creating the correct placementy of each item.
    def percolate_up(self, i):
        if i == 0:
            return
        #Sets the parent index and the value of i to compare in the percolation
        indexParent = (i - 1) // 2
        parent_val = self.tree[indexParent]
        i_value = self.tree[i] 
        #Checks if the count equals the value
        if parent_val[1] == i_value[1]:   
            parent_word = list(parent_val[0])
            i_word = list(i_value[0])
            iteration = min(len(i_word), len(parent_word))
            #While iterating, it will check which words replaces uppercase letters with lowercase letters.
            for i in range(iteration):
                i_letter = self.caps(i_word[i])  
                parent_letter = self.caps(parent_word[i])
                #If the letter is greater than its parent, then it swaps
                if i_letter > parent_letter: 
                    i_value[0], parent_val[0] = parent_val[0], i_value[0]
                    i_value[1], parent_val[1] = parent_val[1], i_value[1]
                    self.percolate_up(indexParent)
                #Otherwise it will return blank
                elif i_letter < parent_letter:
                    return
        #Checks if the count is less than the value
        if parent_val[1] < i_value[1]:
            i_value[0], parent_val[0] = parent_val[0], i_value[0]
            i_value[1], parent_val[1] = parent_val[1], i_value[1]
            self.percolate_up(indexParent)
            
    #Method that helps balance of the heap correctly by swapping items until the correct order is met while also creating the correct placementy of each item.
    def percolate_down(self, i):
        #Sets the value of i to traverse the heap.
        i_value = self.tree[i]
        #If the i value is less than the max of the left and right child, return blank
        if i_value[1] >= max(self.left_child(i), self.right_child(i)):
            return
        #If the i value is greater than the right child, set the index to the left child, otherwise set the index to the right child
        if self.left_child(i) > self.right_child(i):
            max_child_index = 2 * i + 1 
        else:
            max_child_index = 2 * i + 2
        #Sets a list of max values through iterate again
        max_list = self.tree[max_child_index]
        i_value[0], max_list[0] = max_list[0], i_value[0]
        i_value[1], max_list[1] = max_list[1], i_value[1]
        self.percolate_down(max_child_index)
    
    #Method that finds the max value of a heap.
    def extractMax(self): 
        #If the length of the heap is less than 1, return none.
        if len(self.tree) < 1:
            return None
        #If the length of the heap is  1, pop the item on the tree.
        if len(self.tree) == 1:
            return self.tree.pop()
        #Sets the root of the tree, and later pops the number as well as percolating down the heap.
        root = self.tree[0]
        self.tree[0] = self.tree.pop()
        self.percolate_down(0)
        #Returns the root value
        return root
    
    #Takes the filename given by the user and inserts all of the words into a given heap
    def file(filename):
        #Creates a new heap and dictionary to place items inside.
        dict = {}
        heapWord = MaxHeap()
        #While the file is open, it adds each word into the dictionary.
        with open(filename, encoding='windows-1252') as textFile:  
            #For every line in the file, it will grab every word.
            for line in textFile:
                string = line.split()
                word = str(string)
                word_string = word[2:len(word) - 2]
                #If the word is in the dictionary, it will add to the count variable if duplicates of a word are found in the file. 
                if word_string in dict: 
                    count = dict.get(word_string) + 1
                    update_pair = {word_string : count}
                    dict.update(update_pair)

                else: 
                    dict[word_string] = 1 
        #Inserts the info from the dictionary into the heap 
        for key in dict: 
            heapWord.insert([key, dict[key]])
        #Returns the heap back to the user
        return heapWord, dict
    
    #Method activated by make key that will find the lower case letter by comparing it to its caps counterpart
    def caps(self, char):   
        cap_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        lower_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
        lower_char = '' 
        for i in range(len(cap_list)): 
            if (char == cap_list[i]): 
                lower_char = lower_list[i] 
                return lower_char
        return char
    
    #Method that returns the size of the heap
    def size(self): 
        return len(self.tree)
    
    #Prints the items of a heap in descending order
    def print_descending(self, num_of_times): 
        count = 0
        if (len(self.tree) < num_of_times): 
            print("Invalid number. Try again")
            count+=1
        if count == 3:
            print("ERROR: Too many incorrect statements!")
            print("Farewell.")
        #Sets the first word automatically in case there is no most common word
        most_common_word = self.tree[0]
        #Iterates through the whole heap to find the max
        for i in range(num_of_times):
            word = self.extractMax()
            print("Current Word:", word[0], "|", "Number of times:", word[1])
        print("")
        print("Result: ")
        print("The most seen word was :", most_common_word[0])
        print("This word appeared", most_common_word[1],"number of times.")
        print("")