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
    
    certified=""
    eligible={'y', 'Y'}
    nonEligible={'n', 'N'}
    valid=eligible or nonEligible
    
    while certified not in valid:
        certified=str(input("Do you hold a Microsoft certification y/n: "))

    if certified in nonEligible:
        print("You are not eligible. You must hold a Microsoft certification.")
        exit()
        
def computingDegree():
    
    response=""
    eligible = {'Y', 'y'}
    nonEligible={'N', 'n'}
    valid=eligible or nonEligible

    while response not in valid:
        response=str(input("Do you hold a first class honours undergraduate computing degree y/n: "))
    
    if response in nonEligible:
        print("You are not eligible. You must have a first class honours computing degree.")
        exit()

def gotTheJob():
    
    print("Congratulations! You got the job.")
    

main()