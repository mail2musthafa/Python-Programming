print("welcome!!")
#--------------------------------------
def getInteger(): 
    result = int(input("Enter integer: ")) 
    return result 
  
def Main(): 
    print("Started") 
  
    # calling the getInteger function and  
    # storing its returned value in the output variable 
    output = getInteger()      
    print(output) 
  
# now we are required to tell Python  
# for 'Main' function existence 
if __name__=="__main__": 
    Main() 
  #------------------------------ 
    # for iteratig the (looping the) 
for i in range(10):
    print(i)
#-------------------------------------------
#  Pthon program to illustrate math module 
import math
def Main():
    num =-49 
    num = math.fabs(num)  
    print(num)     
if __name__ =="__main__":
    Main()       
#---------------------------------------------------
# Python Taking the inputs form user  
# input(prompt)
# raw_input(prompt)  
var = input("please enter value")
print(var)   
name = input("please enter your name!!?\n") 
print(name)        

 #--------------------------------------------------
name = input('What is your name?\n')     # \n ---> newline  ---> It causes a line break 
print(name)    
#-----------------------------------
#program to check input type in python 
num = input("please enter the value ")
print(num)
num1 = input('please enter value')
print(num1)
print("type of number is :",type(num1))
#--------------------------------------------------
g = raw_input("Enter your name : ") 
print g    
#--------------------------------
# accepting the inputs from user
#input
input1= input()
#output
print(input1)
#------------------------
# typcastig the input to intigear
num1 = int(input("please enter value \n"))
num1 = float(input("enter the value \n"))
num1 = str(input("please enter the string value"))
#----------------------------------
 
#taqking the mmultiple inputs  isimng ṭh
# e using split method 
#accept multi[ler multple inputys usingh the usomng the
#]
#sploit functions x,y



print(type(num1))

