'''
Created on 29 Sep 2018

@author: colinoriordan

Application which purpose is to stream job applicants into eligible or non eligible and tell
the applicant that they were non eligible and why (at least in version1.0).
If they applicant satisfies all three requirements then they are given the job.

Version1.0 Using nested if statements - Tells user why non eligible

Version2.0 Using if statement and logical operator AND - Doesn't tell user why non eligible

Version3.0 Using if statement and logical operator AND - Tells user why non eligible

'''

# Questions 3 nested if statements
import sys 

"""Version 1.0

#Main function of the application 
def main():

#Verifies the program is being run with python version 3.0 or later
 if sys.version_info[0] < 3:
        raise Exception("Python 3 or a more recent version is required.")
 
 #The answer to the question is converted to an int and assigned to variable yearsExp
 yearsExp = int(input("How many years of commercial software development experience do you have: "))
    
  #If yearsExp is less than 4, candidate is not eligible. Else, he satisfies the requirement.
 if yearsExp < 4:
     print("You are not eligible. You must have at least 4 years of commercial software development experience.")
     exit()
     
 else:
 
      #Setup vars
      certified = ""
      eligible = {'y', 'Y'}
      nonEligible = {'n', 'N'}
      valid = {'Y', 'y', 'N', 'n'}

      #while the assigned character to certified is not in the set valid, ask user to input until it is in set valid.  
      while certified not in valid:
        certified = str(input("Do you hold a Microsoft certification y/n: "))
      
      #If assigned value to certified is in the set nonEligible the candidate is not eligible. Else, the candidate satisfies the requirement.
      if certified in nonEligible:
        print("You are not eligible. You must hold a Microsoft certification.")
        exit()
    
      else:
        
        #Setup vars
        response = ""
        eligible = {'Y', 'y'}
        nonEligible = {'N', 'n'}
        valid = {'Y', 'y', 'N', 'n'}
        
        #while the assigned character to response is not in the set valid, ask user to input until it is in set valid.  
        while response not in valid:
            response = str(input("Do you hold a first class honours undergraduate computing degree y/n: "))
        
        #If assigned value to response is in the set nonEligible the candidate is not eligible. Else, the candidate satisfies the last requirement and has got the job.
        if response in nonEligible:
            print("You are not eligible. You must have a first class honours computing degree.")
            exit()
        else:
            print("Congratulations! You got the job.")


#Main is called to start the application       
main()
"""

#PART TWO 

"""Main function of the program"""
def main():
    
    #Verifies the program is being run with python version 3.0 or later.
    if sys.version_info[0] < 3:
       raise Exception("Python 3 or a more recent version is required.")
    
    
    #Version 2.0 Candidates response is passed to isEligble function. If isEligible returns True, applicant has got the job. 
    if isEligible(yearsExperience(), microsoftCertification(), computingDegree()):
        gotTheJob()
    else:
        print("You are not eligible for this position")
    
    """    
    #Version 3.0 If the candidate has 4 years experience, Microsoft certification & 1.1 computing degree, he gets the job.
    yearsExperience()
    microsoftCertification()
    computingDegree()
     
    """
        
"""
Version 2.0 yearsExperience
yearsExperience function - Get's user input of years experience in commercial software 
development environment and returns the value.


Version 3.0 yearsExperience
yearsExperience function - returns True if the candidate has at least 4 years of commercial
software development experience, notifies the candidate if not eligible and exits the program."""
def yearsExperience():
    
    #The answer to the question is converted to an int and assigned to variable yearsExp
    yearsExp=int(input("How many years of commercial software development experience do you have: "))
    
    return yearsExp

    """ Version 3.0
    #If yearsExp is less than 4, candidate is not eligible. Else, he satisfies the requirement.
    if yearsExp<4:
        print("You are not eligible. You must have at least 4 years of commercial software development experience.")
        exit()
    else:
        return True
    """

""" microsoftCertification function - returns True if the candidate has a certificate from Microsoft.
Notifies the candidate if non eligible and exits the program."""
def microsoftCertification():
    
    #Setup vars
    certified=""
    valid={'Y', 'y', 'N', 'n'}
    
    """ Version 3.0
    eligible={'y', 'Y'}
    nonEligible={'n', 'N'}
    """
    
    #while the assigned character to certified is not in the set valid, ask user to input until it is in set valid.
    while certified not in valid:
        certified=str(input("Do you hold a Microsoft certification y/n: "))
        
    return certified;

    """Version 3.0
    #If assigned value to certified is in the set nonEligible the candidate is not eligible. Else, the candidate satisfies the requirement.
    if certified in nonEligible:
        print("You are not eligible. You must hold a Microsoft certification.")
        exit()
    else:
        return True
    """
      
"""
computingDegree function - returns True if the candidate has a 1.1 computing degree. 
Notifies the candidate if they are non eligible and exits the program"""
def computingDegree():
    
    #Setup vars
    response=""
    valid={'Y', 'y', 'N', 'n'}
    
    """Version 3.0
    eligible = {'Y', 'y'}
    nonEligible={'N', 'n'} 
    """
    #while the assigned character to certified is not in the set valid, ask user to input until it is in set valid.
    while response not in valid:
        response=str(input("Do you hold a first class honours undergraduate computing degree y/n: "))
    
    return response
    
    """Version 3.0
    #If assigned value to certified is in the set nonEligible the candidate is not eligible. Else, the candidate satisfies the requirement.
    if response in nonEligible:
        print("You are not eligible. You must have a first class honours computing degree.")
        exit()
    else:
        return True
    """

"""Version 2.0 
   isEligble function, using the input values of the three requirements, determine sif the applicant is
   eligible for the role
   
   (int) yearsExp - No. of years experience the user has in a commercial software development environment
   (char)certified - Y/N response to if the user is certified by microsoft
   (char)response - Y/N repsonse to if the user has a 1.1 degree in computing
   
   Returns boolean value True if they are eligible, False if non eligible. 
"""
def isEligible(yearsExp, certified, response):
    
    #setup vars
    eligible = {'Y', 'y'}
    nonEligible={'N', 'n'} 
    
    #if candidate has >=4 years experience, has a microsoft certificate and a 1.1 honours degree return True. Else False.
    if (yearsExp>=4 and certified in eligible and response in eligible):
       return True
    else:
        return False

"""gotTheJob function - Notifies the candidate that they have gotten the job."""
def gotTheJob():
    
    print("Congratulations! You got the job.")
    
#Main is called to start the application   
main()
