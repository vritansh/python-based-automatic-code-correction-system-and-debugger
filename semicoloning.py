import re
import sqlite3
import time

database = sqlite3.connect('semicolons.db')
user = database.cursor()
errors  = 0
def replace_me(string):
    global errors
    if(string.find(';')==-1) and  string!='' and string !='\n' :
       
                raw_Expression = ["^(\w*)"]
                regular_Expression= ''.join(raw_Expression)

                check_String = re.findall('{0}'.format(regular_Expression) , string)
                    
                flag = fetch_Keyword(''.join(check_String))
                
                if flag==1:
                    
                  if string.find('\n')!=-1:
                    d = string.replace('\n','')
                    data = d+ ';'
                   
                    errors+=1
                   
                  else :
                      data = string +';'
                 # print(data) 
                  return(data) 
                else :
                    data = string.replace('\n','')
                    
                    return(data) 
                    
    else:
        return(string.replace('\n','') )

    



def fetch_Keyword(check_String) : #SUCCESS
     flag  = 0
     user.execute("select * from semicolons")
     data = user.fetchall()
     user.execute("select second from semicolons")
     data1 = user.fetchall()
     
     for row in data:
           
           if row[0] == check_String :
               
               if row[1] == ';' :
                flag =1 
                
                
     if flag == 1 :
            return 1 
     else :
          return 0 
def error_count2() :
    return(errors)



