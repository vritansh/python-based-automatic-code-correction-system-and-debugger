#GUI FOR TAKING USER INPUT FOR THE STRINGS AND CORRECTING THE SPELLINGS
import sqlite3
import time
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from CHECK_SPELLINGS import finder

from comparison import check_here

from semicoloning import replace_me



spell_errors = 0
comp_errors = 0
semi_errors = 0
database = sqlite3.connect('clang.db')
user = database.cursor()
user.execute('CREATE TABLE IF NOT EXISTS keys(keyword TEXT, ending TEXT)')
#declaring the functions before hand to be implemented in the file 

global fname
root= Tk()
def page() :
    root.title("AVIGNA")
    frame1 = Frame(root, cursor = 'dot')
    frame1.grid(sticky=N+S+E+W)
     
    frame1.rowconfigure(0,weight = 1)
    frame1.columnconfigure(0,weight =1)
    frame1.config(bg = 'LemonChiffon3')
    #LABEL WIDGET 
    label_select = Label(frame1, text = "File Name Here:")
    label_select.grid(row = 0 , column = 0 , padx =4 , pady = 4  )
    label_select.config(font=('helvetica', 12, 'bold'),fg='red') 
    global entry_file
    #ENTRY FILE WIDGET
    entry_file= Entry(frame1)
    entry_file.grid(row =1, column = 0)
    entry_file.config(font=('helvetica', 12, 'bold'),fg='gray4', relief =  RAISED, bd = 5)
    fname = entry_file.get() 
    #GO BUTTON WIDGET
    button_submit = Button(frame1 , text = " GO :",command =lambda : show_file(fname),padx = 10, pady = 10)
    button_submit.grid(row = 1, column= 1, padx = 4, pady = 4,sticky=N+S+E+W)
    button_submit.config(font=('helvetica', 10, 'bold'),bg='red2', fg='white', relief = RAISED)
    
    #BROWSE FILES WIDGET
    button_browse = Button(frame1, text = "Browse Files!",command = get_file)
    button_browse.grid(row = 2 , column = 0 )
    button_browse.config(font=('helvetica', 10, 'bold'),bg='red1', fg='white', relief = RAISED)

    #ANALYSE FILES WIDGET
    button_analyse = Button(frame1 , text = "ANALYSE",command =  check_all)
    button_analyse.grid(row = 3, column= 1, padx = 4, pady = 4)
    button_analyse.config(font=('helvetica', 10, 'bold'),bg='red2', fg='white', relief = RAISED)

   

    #LEVEL 2 WIDGET
    button_analyse2 = Button(frame1 , text = "SAVE FILE",command =  save_file)
    button_analyse2.grid(row = 1, column=2 , padx = 4, pady = 4)
    button_analyse2.config(font=('helvetica', 10, 'bold'),bg='red2', fg='white', relief = RAISED)

    
    global text_show
    #TEXT FIELD WIDGET
    text_show = Text(frame1,undo =True, highlightcolor = 'gray')
     
    text_show.grid( row =3, column = 0, padx = 10, pady = 10)
    text_show.rowconfigure(0,weight = 1)
    text_show.columnconfigure(0,weight =1)
    text_show.config(font=('helvetica', 10, 'bold'),bg='azure', fg='black', relief = SUNKEN)
    #BUTTON FOR SAVING REPORT
    button_analyse3 = Button(frame1 , text = "SAVE REPORT",command =  save_report)
    button_analyse3.grid(row = 0, column=2, padx = 4, pady = 4)
    button_analyse3.config(font=('helvetica', 10, 'bold'),bg='red', fg='white', relief = RAISED)
    
    
    
    button_analyse4 = Button(frame1 , text = "CLEAR ALL >>",command = clear_function)
    button_analyse4.grid(row = 2, column=2, padx = 4, pady = 4)
    button_analyse4.config(font=('helvetica', 10, 'bold'),bg='red', fg='white', relief = RAISED)

    #TEXT FIELD FOR OUTPUT
    global text_show2
    text_show2 = Text(frame1,undo =True)
     
    text_show2.grid( row =3, column = 2, padx = 10, pady = 10)
    text_show2.rowconfigure(0,weight = 1)
    text_show2.columnconfigure(0,weight =1)
    text_show2.config(font=('helvetica', 10, 'bold'),bg='red', fg='white', relief = SUNKEN)
    
    root.mainloop()
def clear_function():
     text_show.delete(1.0,END)
     
     text_show2.delete(1.0,END)
     messagebox.showinfo("Excuse me","Cleared !You are now good to go !")

def get_file() :
    
        fname = askopenfilename(filetypes=(("TEXT files", "*.txt"),
                                           ("C files", "*.c;*.cpp"),
                                           ("All files", "*.*") ))
        show_file(fname)  
         
def show_file(fname):
        if fname == '' :
                 messagebox.showinfo("Excuse Me!","I Was Expecting a File Name!")
        else :
                browse_file = open(fname,'r')  
                
                data = browse_file.readlines()
                browse_file.close()
                text_show.insert(INSERT, data)

def spell_check():
                 global spell_errors
                 
                 print("ANALYSING MODULES")
                 new_data = [] 
                 data = text_show.get(1.0,END).strip().splitlines()
                 
                 
                 for i in range(0,len(data)):
                   print("REQUEST SENT ")
                   check_first = re.findall("^(\w*)",data[i])
                   passme = ''.join(check_first) 
                   replace_text = finder(passme)
                   if replace_text !=passme:
                       
                       spell_errors +=1
                   new_data.append(data[i].replace(passme,replace_text))
                   
                   
                 text_show.delete(1.0,END)
                 print("REQUEST RECIEVED") 
                 for d in new_data:
                       text = d
        
                       text_show.insert(INSERT, d +'\n') 
                 
                 
               

def check_comparison () :
                print("SECOND STEP STARTED")
                global comp_errors
                new_data = []
               
                data = text_show.get(1.0,END).strip().splitlines()
              
                 
                
                for i in range(0,len(data)):
                   
                   
                   passme = ''.join(data[i])
                   
                   replace_text = check_here(passme)
                   if replace_text !=passme: 
                       comp_errors +=1 
                    
                   new_data.append(data[i].replace(passme,replace_text))
                   
                   
                text_show.delete(1.0,END)
               
                for d in new_data:
                       text = d
                       
                       text_show.insert(INSERT, d +'\n')
                print("SECOND STEP IS COMPLETE")        
              
                
               
def check_semicolons () :
    
               global semi_errors
               new_data = []
               
               data = text_show.get(1.0,END).strip().splitlines(3) 
               
               for i in range(0,len(data)):
                  
                   
                   passme = ''.join(data[i])
                   
                   replace_text = replace_me(passme)
                   p=''.join(replace_text)
                   if p.find(';')!=-1: 
                       semi_errors +=1
                   
                   new_data.append(data[i].replace(passme,replace_text))
               print("LAST ANALYSIS OVER ") 
               text_show.delete(1.0,END)
               
               for d in new_data:
                       text = d
                       text_show.insert(INSERT, d+ '\n')
                    
def check_headers(data):
            #  new_data = []
              
             # data = text_show.get(1.0,END).splitlines()
              print(data[0]) 
              for i in range(0,len(data)):
                   x = re.findall(('\#'),data[i])
                   
                  
                   
                   passme = ''.join(x)
                    
                   replace_text = finder(passme)
                   #for i in range(0,len(replace_text)): 

                   #   new_data.append(data[i].replace(passme,replace_text))
def save_file():
     
     data = text_show.get(1.0,END).strip().splitlines()
     print(data) 
     f = open('file.txt','w')
     f.write(''.join(data))
     
     f.close()
     messagebox.showinfo("Excuse me","Saved with file name File!")

def save_report():
     
     data = text_show2.get(1.0,END).strip().splitlines()
     print(data) 
     f = open('report.txt','w')
     f.write(''.join(data))
     
     f.close()
     messagebox.showinfo("Excuse me","Saved with file name Report!")




    
                
def check_all():
    spell_check()
    
    check_comparison()
    
    check_semicolons()
    text_show2.delete(1.0,END) 
    text_show2.insert(INSERT,'SPELLINGS ERRORS ARE :' +str(spell_errors)+'\n') 
    text_show2.insert(INSERT,'COMPARISON ERRORS ARE :' +str(comp_errors)+'\n') 
    text_show2.insert(INSERT,'CORRECTED SEMICOLONS ARE :' +str(semi_errors)) 
                       

def main_function():
    page()

main_function()

    
    
    
