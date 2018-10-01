'''
Created on 01 Oct 2018

@author: colinoriordan

Application that will create a list and will populate it with the first 40 Fibonacci numbers.
The program will then ask the user to enter an integer value between 1 and 40 to indicate
which number in the Fibonacci series they would like to see
'''

#main function of the application
def main():
    
    #create list of fibonacci numbers & pass it to selectFibonacciNum, 
    #where user can select which number they'd like to see
    fibonacciList=generateFibonacciList()
    selectFibonacciNum(fibonacciList)
    
"""
function - generateFibonacciList - creates a list of the first 40 fibonacci numbers 
return - fibonacciList - list of the first 40 numbers in the fibonacci sequence
"""
def generateFibonacciList():
    
    #assign the first two numbers of the fibonacci list
    fibonacciList=[]
    fibonacciList.append(0)
    fibonacciList.append(1)
    
    #loop to assing next fibonacci number to sum of previous two
    for x in range (2, 40):
        fibonacciList.append(fibonacciList[x-1]+fibonacciList[x-2])
    
    return fibonacciList

""""
function - selectFibonacciNum - Gets user input of which fibonacci number they'd like to see and prints it.
arg - fibonacciList - list of the first 40 fibonacci numbers

"""
def selectFibonacciNum(fibonacciList):
    
    num=100
    
    #get num input 
    while num not in range(1, 41):
        num=int(input("Enter the n'th fibonacci number you'd like to see (1-40): "))
    
    #print the num'th number of the fibonacci sequence
    print("The ", num, " fibonacci number is ", fibonacciList[num-1])

main()