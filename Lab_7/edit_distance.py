'''
Author: Carlos Fernando Castaneda
Class : CS 2302 
Date Modified: November 26, 2019 
Instructor: Diego Aguirre 
Assingment: Lab 7 Edit Distance (2 0f 2)
TA: Gerardo Barraza
Purpose: To practice using dynamic porgramming
to implement te edit distance method.
'''
#Method that alters two given strings based on the rules of edit distance
def edit_distance(string_1, string_2, len1 , len2): 
    # Will check if the length of the first string is none. If so, it will return the length of the second string 
    if len1 == 0: 
         return len2
    # Will check if the length of the second string is none. If so, it will return the length of the first string
    if len2 == 0: 
        return len1
    #Will check if the last characters of both strings are the same; if so, it will return the count of the remaining characters and will ignore the duplicated ones
    if string_1[len1-1] == string_2[len2-1]: 
        return edit_distance(string_1,string_2,len1-1,len2-1) 
    #Returns one for the counter indicating that the last elements of the string are not the same. The program will then proceed to perform the three operations, insert, remove, and replace to find the best solution
    return 1 + min(edit_distance(string_1, string_2, len1, len2-1),    # Insert 
                   edit_distance(string_1, string_2, len1-1, len2),    # Remove 
                   edit_distance(string_1, string_2, len1-1, len2-1)    # Replace 
                   ) 