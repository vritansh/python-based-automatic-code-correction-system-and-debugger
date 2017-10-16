import re

errors = 0

def check_here(input_String):
        listing = ['if','else','for','do','while']
        global errors
        flag = 1 
        raw_Expression = ["^(\w*)"]
        regularExpression= ''.join(raw_Expression)
        
        obtain_String = re.findall('{0}'.format(regularExpression) ,input_String)
        check_String = ''.join(obtain_String)
                
        for i in range(0,5):
                check_String = ''.join(obtain_String)
                if listing[i] == check_String :
                        flag = 1
                        break
        
        if flag ==1:
            replacable_String = "=="
            replacing_String= ['==','<=','>=','!=']
            x=0     
            for i in range(0,4):
                    
                    if input_String.find(replacing_String[i]) !=-1:
                            x = 1 
                    
            if x != 1 :
                            input_String = input_String.replace("=", replacable_String)
                            errors +=1
                            return(input_String)
                    
            else :
                 return(input_String) 

def error_count1():
        #print(errors)
        return(errors)

error_count1()
