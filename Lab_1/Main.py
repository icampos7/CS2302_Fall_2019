'''
Author: Carlos Fernando Castaneda
Class : CS 2302 
Date Modified: September 9, 2019 
Instructor: Diego Aguirre 
Assingment: Lab 1 Recursion
TA: Gerardo Barraza
Purpose: To practice using recursion and to practice using this technique
to find new passwords using strings
'''

#Imports the hash library needed to be used in this program
import hashlib
#Imports time to be used in calculating the big o notation
import time

#Creates the new password related to its respective user.
def new_password(salt_name, len_string, hashed_string):
	#Sent to method int_converter, which converts the minimum integer into a the max it can be.
    new_int = int(int_converter(len_string))
    if (len_string >= 8):
        print("ERROR: Password not possible! Not within 3 to 7 characters!")
        return "Password does not exist!"
    #This loop is used to create a new string to be compared to our hashed password.
    for x in range (0, new_int): # For i in range of the new integer
        index = str(x)
        amount_string = len(index)
        #Creates a new index and digit to construct a hashed password
        new_index = zero_generator(len_string, index, amount_string)
        new_digit = hash_with_sha256(new_index + salt_name)
        #If the new digit equals the hashed string, then it will return the new index
        if (new_digit == hashed_string):
            return new_index
    #Calls itself again until it returns the new index
    return new_password(salt_name, len_string + 1, hashed_string) 
 
#Method that adds the zeros at beginning of a certain string 
def zero_generator(int, index, amount_string): 
    #If the integer quals the amount_string, then it returns the number struing
	if (int == amount_string): 
		return index 
	return '0' + zero_generator(int, index, amount_string +1)

#This method is used to get a certain maximum value of an integer by using just its min
def int_converter(int): 
	if (int == 0): 
		return ''
	return '9' + int_converter(int - 1)	

#Method given with the program,
def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

#Main method, will initiate the calls needed to execute the program; the brains of the program.	
def main():
    #Starts a timer that will calculate the total running time for the program
    start = time.time() 
    #Message that welcom
    print("Welcome. Password hack beginning.")
    txt = 'password_file.txt'
    print("Reading....")
    #Sets the lowest length of the password to be 3 as instructed in the lab
    min = 3
    #Reads the txt file as a textfile line by line 
    with open(txt) as textFile: 
        textFile_lines = [line.split(',') for line in textFile]
    #This loop is used to generate the new password using the new_password method using the information from the textfile. 
    for x in range (len(textFile_lines)):  #For i in range of the amount of lines in the textfile
        #Reads the hasged_string to be used in creating a new password
        hashed_string = textFile_lines[x][2]
        #Sends the new imported number as well as the new minimum to the method new_password that will create the new password
        new_pass = new_password(textFile_lines[x][1], min, hashed_string.rstrip('\n'))
        #Prints out the new password associated with its current user
        print(textFile_lines[x][0] + ' password is: ' + new_pass) 
    #Ends the timer used to calculate the running time
    end = time.time()
    #Prints out the running time needed for this program
    print('Running time was: ', end - start, 'seconds.')

#Calls the main method, it is the beginning of the program
main()
