'''
Created on 01 Oct 2018

@author: colinoriordan

Application that that asks the user to enter the rainfall for the first X months of the year into a
list, where X is an int value between 1 and 12. (Obtaining the rainfall input from the user
should be done using a loop).
The program will calculate and display:
• The average monthly rainfall
• The highest rainfall value received
• The lowest rainfall value received
'''

#import module 
import sys

#main function of the application
def main():
    
    #call the rainfallData function
    rainfallData()
    
"""
rainfallData function - gets user input for rainfall of x amount of months a user wishes to enter
stores users input in a list and records the highest and lowest of the rainfall
displays the highest, lowest and average rainfall to user
"""
def rainfallData():
    
    highestRainfall=0
    lowestRainfall=sys.maxsize
    rainfall=[]
    
    numMonths=int(input("Enter how many months of data you wish to enter: "))
    
    for x in range(0, numMonths):
        
        rainfall.append(int(input("Enter rainfall for month {}:".format((x+1)))))
        
        if rainfall[x]>highestRainfall:
            highestRainfall=rainfall[x]
            
        if rainfall[x]<lowestRainfall:
            lowestRainfall=rainfall[x]

    averageRainfall=getAverageRainfall(numMonths, rainfall)
    
    print("Highest rainfall value: ", highestRainfall)
    print("Lowest rainfall value ", lowestRainfall)
    print("Average rainfall value: ", averageRainfall)
        
"""
getAverageRainfall function -  calculates the average rainfall from a list of rainfall data
arg numMonths - number of months of rainfall in the list 
arg rainfall - list of rainfall data by month
return averageRainfall - the average rainfall of the list of rainfalls
"""
def getAverageRainfall(numMonths, rainfall):
    
    totalRainfall=0
    
    for x in range (0, numMonths):
        totalRainfall=totalRainfall+rainfall[x]
    
    averageRainfall=(totalRainfall/numMonths)
    
    return averageRainfall

main()