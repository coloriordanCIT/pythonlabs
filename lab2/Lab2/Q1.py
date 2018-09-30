'''
Created on 29 Sep 2018

@author: colinoriordan
'''


def main():
    
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
