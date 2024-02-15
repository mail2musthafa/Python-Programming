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
#------------------------------
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
 
# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
 
# taking two inputs at a time
a, b = input("Enter two values: ").split()
print("First number is {} and second number is {}".format(a, b))
 
# taking multiple inputs at a time 
# and type casting using list() function
x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", x)
#------------------------------------------------------
#using the list comprehension 
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
 
# taking three input at a time
x, y, z = [int(x) for x in input("Enter three values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print("Third Number is: ", z)
 
# taking two inputs at a time
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First number is {} and second number is {}".format(x, y))
 
# taking multiple inputs at a time 
x = [int(x) for x in input("Enter multiple values: ").split()]
print("Number of list is: ", x) 
#----------------------------------------------
x,y  = [int(x) for x in input("enter the value").split()]
print(x,y,z)
x,y,z  = [int(x) for x in input("enter the number").split()]

#-------------------------------
x,y =[int(x)  for x in input("enter the value \n").split()]
a = [1,2,3,4]
for i in range(5):
    print(a[i])

#--------------------------    
for i in range(4):
    print(x[i])

for i in range(4):
    print(a[i], end =" ")     



