'''
Author: Carlos Fernando Castaneda
Class : CS 2302 
Date Modified: October 21, 2019 
Instructor: Diego Aguirre 
Assingment: Lab 3 Binary Trees (Part 2 of 3)
TA: Gerardo Barraza
Purpose: To practice using multiple methods
of creating Binary Trees, includong AVL and
Red-Black.
'''
#Used to calculate the time for each tree
import time
#Imports the AVL_Trees and RB_Trees programs to build the binary trees
import AVL_Trees
import RB_Trees

#Method that creates and returns an AVL tree from the imported file.
def AVL(filename):  
    AVL = AVL_Trees.AVLTree()
    key = 0
    print("Preparing the AVL Tree now! Please wait...")
    print()
    with open(filename, encoding='windows-1252') as textFile: 
        for line in textFile:
            string = line.split()
            word = str(string) 
            stringedWord = word[2:len(word) - 2] 
            key = make_key(stringedWord) 
            AVL.AVLTreeInsert(stringedWord, key)
    return AVL

#Method that creates and returns an Red and Black tree from the imported file.   
def RB(filename): 
    RB = RB_Trees.RedBlack()
    key = 0 
    print("Preparing the Red and Black Tree now! Please wait...")
    print()
    with open(filename, encoding='windows-1252') as textFile: 
        for line in textFile:
            string = line.split()
            word = str(string) 
            stringedWord = word[2:len(word) - 2]
            key = make_key(stringedWord)   
            RB.RBTreeInsert(stringedWord, key)
    return RB

#Method that finds the necessary anagrams for both the maximum and count methods for the anagrams by using a binary search tree
def search_anagrams(tree, word, prefix=""): #
    if len(word) <= 1: 
        str = prefix + word
        key = make_key(str) 
        searched_word = BSTsearch(tree, key)
        if (searched_word != None): 
            return 1 
        return 0 
    else:
        count_anagrams = 0 
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] 
            after = word[i + 1:] 
            if cur not in before:
                count_anagrams += search_anagrams(tree, before + after, prefix + cur)
    return count_anagrams

#Method that acts a binary search tree that will find the necessary anagrams for the find
def BSTsearch(tree, key): 
    cur = tree.root   
    while cur != None:
        if key == cur.key:
            return cur 
        elif key < cur.key:
            cur = cur.left
        else:
            cur = cur.right
    return None

#This method generates keys for each word by stringing together character numbers of each letter of a word.   
def make_key(word):  
    key = "" 
    res = list(word) 
    if (len(res[0]) > 1):   
        str_word = str(res[0]) 
        return make_key(str_word)
    for i in range(len(res)): 
        char = caps(res[i])
        char_num = ord(char) 
        char_str = str(char_num)
        key += char_str 
    key_int = int(key) 
    return key_int 
  
#Method activated by make key that will find the lower case letter by comparing it to its caps counterpart.
def caps(char): 
    cap_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
    lower_char = '' 
    for i in range(len(cap_list)): 
        if (char == cap_list[i]): 
            lower_char = lower_list[i] 
            return lower_char     
    return char 
  
#Method that counts the number of anagrams a certain word has.
def count_anagrams(tree): 
    print("") 
    print("Please input a word for counting the number of anagrams:") 
    new_word = input() 
    count = search_anagrams(tree, new_word) 
    print("") 
    print("Findings complete! Total was:", count)  
    print()

#Method that finds the maximum number of anagrams from another text file, the user can choose to ignore this part however.
def maximum_anagrams(): 
    print("Want to load another file to find the word that has the most anagrams? Y/N") 
    print("A. Yes")
    print("B. No")
    user_selection = input() 
    count = 0
    if (user_selection == "A" or user_selection == "a"):
        print("")
        print("Input filename of the textfile:")
        filename = input() 
        tree = RB(filename) 
        anagrams = "" 
        anagrams_num = 0 
        with open(filename, encoding='windows-1252') as textFile:  
            for line in textFile:
                string = line.split()
                word = str(string)
                word_str = word[2:len(word) - 2]
                count = search_anagrams(tree, word_str)   
                if (anagrams_num < count): 
                    anagrams = word_str 
                    anagrams_num = count     
        print("The word with the most anagrams is '", anagrams, "' with the total of", anagrams_num, "anagrams.")
        print("Terminating program, Farewell!")
    elif (user_selection == "B" or user_selection == "b"): 
        print("User selected to exiting the program.")
        print("Farewell.")
    elif count == 3:
        print("ERROR: Too many incorrect statements!")
        print("Farewell.")
    else: 
        print("ERROR: Input not valid!") 
        count+=1
        maximum_anagrams() 

#Main method of the program, this method is used for the user to select the options for the rest of the program.       
def main(): 
    print("Welcome to the Anagram program! Please select the .txt file you want to implement:")
    file = input() 
    print("") 
    print("Do you want to use an AVL tree or a Black-Red tree? Select from below:") 
    print("A. AVL Tree")
    print("B. Red-Black Tree")
    user_selection = input()
    count = 0
    if (user_selection == 'A' or user_selection == 'a'):
        start1 = time.time()
        tree = AVL(file)
        end1 = time.time()
        print("Tree insertion complete!")
        print('Running time was: ', end1 - start1, 'seconds.')
        count_anagrams(tree) 
    elif (user_selection == 'B' or user_selection == 'b'): 
        start2 = time.time()
        tree = RB(file)
        end2 = time.time()
        print("Tree insertion complete!")
        print('Running time was: ', end2 - start2, 'seconds.')
        count_anagrams(tree) 
    elif count == 3:
        print("ERROR: Too many incorrect statements!")
        print("Farewell.")
    else: 
        print("ERROR: Input not valid!") 
        count+=1
        main() 
        
main() 
maximum_anagrams() 