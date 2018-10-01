'''
Created on 01 Oct 2018

@author: colinoriordan

Application that will ask the user to enter the number of packages purchased. The
program will display the amount of the discount (if any) and the total amount of the
purchase after the discount. If a user indicates a negative quantity then they
should be told that the quantity value should be greater than zero.
'''

#Global Variables 
packageCost=99
minQuantity=1

#main function of the application
def main():
    
    quantity=getNumPackages()
    calculateCostOfOrder(quantity, calculateDiscountPc(quantity))

"""
getNumPackages function - gets user input of how many orders they would like to purchase
(int)return numPackages - no. of packages the buyer would like to purchase.
"""
def getNumPackages():

    #no. of packages variable
    numPackages=0
    
    #Prompts user for an input until the input is valid i.e. >0.
    while numPackages<1:
        numPackages=int(input("How many packages would you like to order? "))
        
        #User is told the quantity of packages should be greater than the minimum quantity to proceed.
        if numPackages<minQuantity:
            print("\nQuantity of packages should be at least ", minQuantity, "\n")
    
    quantity=numPackages
    return numPackages 


"""
calculateDiscountPc function - calculates the % discount the buyer is eligible for
arg quantity - the quantity of packages in the order
return discountPc - the % discount the buyer is eligible for
"""
def calculateDiscountPc(quantity):

    #discount percentage variable - default at 0% for quantity of 1-9
    pcDiscount=0
    
    #if the quanity is 10-19, percentage discount is 20%
    if quantity>9 and quantity<20:
        pcDiscount=20
    
    #if the quanity is 20-49, percentage discount is 30%
    elif quantity>19 and quantity<50:
        pcDiscount=30
    
    #if the quanity is 20-49, percentage discount is 40%
    elif quantity>49 and quantity<100:
        pcDiscount=40
    
    #if the quanity is 100 or >, percentage discount is 250%
    elif quantity>99:
        pcDiscount=50
        
    return pcDiscount

def calculateCostOfOrder(quantity, pcDiscount):
    
    totalCost=packageCost*quantity
    discount=(totalCost/100)*pcDiscount
    discountedCost=totalCost-discount
    
    
    print("Total cost before discount: ", totalCost)
    print("Discount                  : ", discount)
    print("Discounted cost           : ", discountedCost)

main()

