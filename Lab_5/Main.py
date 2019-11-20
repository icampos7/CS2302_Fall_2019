'''
Author: Carlos Fernando Castaneda
Class : CS 2302 
Date Modified: November 14, 2019 
Instructor: Diego Aguirre 
Assingment: Lab 5 LRU (1 0f 3)
TA: Gerardo Barraza
Purpose: To practice using queues and
hash tables to create a LRU cache.
'''
#Used to calculate the time for each option on the lab
import time
#Imports the LRU cache and the heap programs to test out the lab
import LRU_Cache as lru
import heaps as heap

#Method that 
def LRU_Test():
    int = 10
    print("Setting the value of the LRU to: ",int)
    print("")
    new_lru = lru.LRU(int)
    print("Inserting items now...")
    print("")
    new_lru.put(1, "Hi")
    new_lru.put(2, "Im")
    new_lru.put(3, "Mr")
    new_lru.put(4, "Meeseeks")
    new_lru.put(5, "look") 
    new_lru.put(6, "at")
    new_lru.put(8, "mee") 
    new_lru.put(9, "6712")
    new_lru.put(10, "Our")
    new_lru.put(11, "very") 
    new_lru.put(11, "existence") 
    new_lru.put(8, "is")
    new_lru.put(9, "pain")
    new_lru.put(6, "pain")
    new_lru.put(11, "pain")
    new_lru.put(6, "ooooooo")
    new_lru.put(12, "6494")
    print("Here are the results: ")
    print("")
    new_lru.print_inorder()
    

def main():
    print("Welcome to the Least Recently Used (LRU) program!") 
    print("")
    print("Do you want to use a LRU, or find the most found word in a list using Heaps? Select from below:")
    print("")
    print("A. LRU Testing")
    print("B. Most found word in a list using Heaps")
    user_selection = input()
    count = 0
    if (user_selection == "A" or user_selection == "a"):
        print("Beginning LRU Testing...")
        print("")
        start1 = time.time()
        LRU_Test()
        end1 = time.time()
        print('Running time was: ', end1 - start1, 'seconds.')
    elif (user_selection == "B" or user_selection == "b"):
        print("Beginning Heap Search...")
        start2 = time.time()
        print("")
        print("Please input the filename you want to input for the heap:")
        filename = input()
        heapWord, dict = heap.MaxHeap.file(filename)
        heapSize = heapWord.size()
        print("")
        print("There are currently", heapSize, "words in the heap. How many words of that heap do you want to see printed?")
        printed = int(input())
        heapWord.print_descending(printed)
        print("")
        end2 = time.time()
        print('Running time was: ', end2 - start2, 'seconds.')
    elif count == 3:
        print("ERROR: Too many incorrect statements!")
        print("Farewell.")
    else: 
        print("ERROR: Input not valid!") 
        count+=1
        main()
        
main()