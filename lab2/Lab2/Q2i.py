'''
Created on 29 Sep 2018

@author: colinoriordan
'''

#Questions 3 nested if statements
import sys 

def main():
    
    print(sys.version)
    
    if sys.version_info[0] < 3:
        raise Exception("Python 3 or a more recent version is required.")
    
    yearsExperience()
    
    microsoftCertification()
    
    computingDegree()
    
    gotTheJob()
    
def yearsExperience():
    
    yearsExp=int(input("How many years of commercial software development experience do you have: "))
    
    if yearsExp<4:
        print("You are not eligible. You must have at least 4 years of commercial software development experience.")
        exit()

def microsoftCertification():
    
    eligible = "Y" or "y"
    nonEligible="N" or "n"
    valid=eligible or nonEligible
    certified=""
    
    while certified!=valid:
        certified=input("Do you hold a Microsoft certification y/n: ")

    if certified==nonEligible:
        print("You are not eligible. You must hold a Microsoft certification.")
        exit()
        
def computingDegree():
    
    eligible = "Y" or "y"
    nonEligible="N" or "n"
    valid=eligible or nonEligible
    certified=""
    
    while response!=valid:
        response=input("Do you hold a first class honours undergraduate computing degree y/n: ")
    
    if response==nonEligible:
        print("You are not eligible. You must have a first class honours computing degree.")
        exit()

def gotTheJob():
    
    print("Congratulations! You got the job.")
    

main()