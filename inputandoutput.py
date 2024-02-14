value  = input("pleae enter the input value")
print(value)
#----------------------------------------
name = input("Wht is  Your Name\n")
print(name)
#--------------------------------
# How input Funtions works in plython  
g = raw_input("pleae enter the input\n")
print(g)
#-------------------------
#for desire inputs 
num = int(input("please Enter The valid input\n"))
print(num, " ",type(num))
#----------------------------------
#flot devcimal 
num = float(input("pleae enter the valid input"))
print(num,+"  " ,type(num)+ " data type ")
#-------------------------------------
# #Taking the input from console in python 
# what is the console in python 
# console is called shell is bsically commond line interpreater 

input1  = input()
print(input1) 
#-------------------
num1= int(input())
num2 = int(input())
print(num1+num2)
#-------------------------------
#typcastng the input to string:
string = str(input())
print(string)
#-----------------------------
#taking the multiple inputs from user 
x, y  = input("please enter the numbers \n").split()
print(x,y)
x,y,z = input("enter the input value \n").split()
print(x,y,z)
print("first nuber is {} and second number s {},third number is {}".format(x,y,z))
