'''
Author: Carlos Fernando Castaneda
Class : CS 2302 
Date Modified: November 26, 2019 
Instructor: Diego Aguirre 
Assingment: Lab 7 Edit Distance (1 0f 2)
TA: Gerardo Barraza
Purpose: To practice using dynamic porgramming
to implement te edit distance method.
'''
#Used to calculate the time for each option on the lab
import time
#Imports the edit_distance program needed to implement the graphs
import edit_distance as ed

def main():
    print("Welcome to the Edit Distance Program!") 
    print("")
    print("This program will perform three different tests. Let's get started!") 
    print("")
    print("Test 1: ")
    #Test case 1
    string_1 = "brand"
    string_2 = "random"
    print("The two words being compared are '",string_1,"' and '",string_2,"'.")
    start1 = time.time()
    print(ed.edit_distance(string_1, string_2, len(string_1), len(string_2)))
    end1 = time.time()
    print('Running time for test 1 was: ', end1 - start1, 'seconds.')
    print("")
    print("Test 2: ")
    #Test case 2
    string_1 = "any"
    string_2 = "any"
    print("The two words being compared are '",string_1,"' and '",string_2,"'.")
    start2 = time.time()
    print(ed.edit_distance(string_1, string_2, len(string_1), len(string_2)))
    end2 = time.time()
    print('Running time for test 1 was: ', end2 - start2, 'seconds.')
    print("")
    print("Test 3: ")
    #Test case 3
    string_1 = "magnificus"
    string_2 = ""
    print("The two words being compared are '",string_1,"' and '",string_2,"'.")
    start3 = time.time()
    print(ed.edit_distance(string_1, string_2, len(string_1), len(string_2)))
    end3 = time.time()
    print('Running time for test 1 was: ', end3 - start3, 'seconds.')
    print("")
    print("Tests completed!")
    print("")
    print("Would you like to try two words for yourself? Yes or No")
    user_selection = input()
    if(user_selection == 'yes' or user_selection == 'Yes' or user_selection == 'YES'):
        print("Excellent! Now, which two words would you like to try?")
        print("Word 1: ")
        string_1 = input()
        print("Word 2: ")
        string_2 = input()
        print("The two words being compared are '",string_1,"' and '",string_2,"'.")
        start4 = time.time()
        print(ed.edit_distance(string_1, string_2, len(string_1), len(string_2)))
        end4 = time.time()
        print('Running time for test 1 was: ', end4 - start4, 'seconds.')
        print("")
        print("Program complete! See you again soon!")
    elif(user_selection == 'no' or user_selection == 'No' or user_selection == 'NO'):
        print("Very well.")
        print("Program complete! See you again soon!")
    else:
        print("ERROR! Input invalid!")
        print("Goodbye!")
    
main()