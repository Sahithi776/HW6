import shelve 
import time

def time_taken(func):
    start = time.time()
    func()
    end = time.time()
    print(end - start)

def retrieve_shelve_data():
    return shelvefile['clues']
    
def retrieve_dict_data():
    return dictionary['clues']
  
  
clues =['I use echo-location', 'I can eat nicely', 'I can have nice sleep'] 
   
shelvefile = shelve.open("shelf_file") 
   
shelvefile['clues']= clues

dictionary = { 'clues': clues }

print("Time taken by shelve")
time_taken(retrieve_shelve_data)

print("Time taken by dictionary")
time_taken(retrieve_dict_data)
  
shelvefile.close()
