from itertools import permutations
import time
import sqlite3
database = sqlite3.connect('clang.db')
user = database.cursor()
error = 0
def finder(toReplace):
    
    user.execute("SELECT keyword from keys")
    
    data = user.fetchall()
    
    flag = 0
    q = 0
    for row in data:
            print("ANALYSING REQUESTS NO : -> "+str(q))
            q+=1
            fromReplace= row[0]
            
            fromReplaceData = [''.join(p) for p in permutations(fromReplace) ]
            
            for string in range(0,len(fromReplaceData)):
                x =  toReplace.find(fromReplaceData[string])
                
                global error
                if x !=-1 :
                            #print(fromReplaceData[string]) 
                            corrected_value = toReplace.replace(fromReplaceData[string], fromReplace)
                            error +=1
                            flag = 1
                            
                            break
            if flag ==1 :
                break
    
    if flag == 1:
            #print(corrected_value)
            return(corrected_value)
    
    elif flag ==0 :
       
        return(toReplace)

def error_count() :
     
    return error

 

