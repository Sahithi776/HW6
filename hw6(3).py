#Prompt user to enter a start path and file name, search recursively for the given
#file name starting at the given path, when file is found, 
#display the full path to the file. 
import os
path=input("enter the path:")
filename=input("enter Filename:")
full_path=[]
for r,d,f in os.walk(path):
    if filename in f:
        full_path.append(os.path.join(r,filename))
        if full_path==[]:
            print("File Not Found")
        else:
            print("Fullpath of File is "+str(full_path[0]))