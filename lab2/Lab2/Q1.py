'''
Created on 29 Sep 2018

@author: colinoriordan

Application which get the user input of two rectangles and 
calculates the area of each rectangle, and compares them to see which is larger.
Tells the user which rectangle has a larger area.
'''

import sys

'''Main function of application'''
def main():
    
    print(sys.version)
    
    if sys.version_info[0] < 3:
        raise Exception("Python 3 or a more recent version is required.")
    
    #Setup variables
    results=[]
    i=1;
    
    #loop
    while i<3:
            results.append(getRectangleArea(i))
            i=i+1
        
    getLargerArea(results[0], results[1])

        

def getRectangleArea(num):
    width = input("\nEnter the width of rectangle {}:".format(num))
    length = input("\nEnter the length of rectangle {}:".format(num))
    return width*length

def getLargerArea(rec1, rec2):
   
    if rec1>rec2:
        print("\nRectangle 1 has a larger area.")
    if rec2>rec1:
        print("\nRectangle 2 has a larger area.")
    if rec2==rec1:
        print("\nBoth rectangles have the same area.")
    


main()
