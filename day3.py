# File Handling in python 
# Python File Open
# Before perfoming file operation on file like rading and writing first 



# f  = open(file_name ,mode)

# r:Open an existinf file for read operation 
# w:open an existing file for a write operation,if the file alredy contains some data,then it will overridden but if the file not present then its create  file as well 
# a:open an existing file to opppend operation it wont overridden
# r+:to read and write  data in file the previous data will be overriden  
#  w+:to write and read data it will be overridden existing data 
# a+:to append and read data from the file it wont overriden existinfg data 

# Working With Read Mode 
#file read test.txt will be opened with reading mode 
file = open('test.txt','r')
for item in file:
    print(item)

    
