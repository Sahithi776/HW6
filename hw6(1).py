#write a program that will take a command line argument of full path and prints 
#True if the file/directory at the provided location is present

#Change program such that it runs indefinitely, monitoring a file/directory at a certain location 


import sys
import os
        
file_path=input("enter the file_path:")
does_file_exist=os.path.exists(file_path)
print(does_file_exist)
if does_file_exist == False:
        print('Alert')
        sys.exit(0)
    
        
