'''
Created on 01 Oct 2018

@author: colinoriordan

Application that will print out the ‘times’ table for a number up to a specific
limit. 
'''

#main function of the application
def main():
    
    num= int(input("Enter a number: "))
    limit= int(input("Enter a limit: "))
    
    timesTable(num, limit)
    
    printNumTriangle()
    
"""
timesTable function - creates a multiplication table of users input num and limit
arg num (int)   - the number being multiplied
arg limit (int) - the limit of the multiplication table
"""
def timesTable(num, limit):
    
    #counter variable
    counter=0
    
    #loops while counter is less than or equal to num
    while counter<=limit:
     
     #print one line of multiplication table
     print(num, "*", counter, "=", (counter*num))
     counter=counter+1

"""
printNumTriangle function - prints a triangle from one to numbered entered.
"""
def printNumTriangle():
    
    #counter variable and num input 
    counter=0
    num=int(input("\nEnter a number: "))
    
    #while loop as long as counter is less than or equal to num
    while counter<=num:
        
        #loop that prints x many times in range 0-counter
        for x in range(0, counter):
            print(counter, end='')
        
        #increment counter
        counter=counter+1
        print()
        
main()