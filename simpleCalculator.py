from tkinter import *

root=Tk()
root.title("Simple Calculator ")
root.geometry("300x400")

entry= Entry(root,width=16, font=('Times', 24), borderwidth=2, relief='ridge')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def click(button_text):
    current= entry.get()
    entry.delete(0, END)
    entry.insert(0, current+ str(button_text))  #append new numbr 
    
def clear():
    entry.delete(0, END)

def calculate():
    try:
        result= eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
        
    except:                                     #invalid expression 
        entry.delete(0, END)
        entry.insert(0, 'Error') 
buttons= [
    '7','8','9','/',
    '4','5','6','*',  
    '1','2','3','-',  
    'C','0','=','+'
    
]

row=1
col=0

for b in buttons:
    action= lambda x=b: click(x)
    
    if b=='C':
        Button(root, text=b, width=5, height=2, command=clear).grid(row=row, column=col, padx=5, pady=5)
    elif b=='=':
        Button(root, text=b, width=5 , height=2, command=calculate).grid(row=row, column=col, padx=5, pady=5)
    else:
        Button(root, text=b, width=5, height=2, command=action).grid(row=row, column=col, padx=5, pady=5 )
    
    col+=1  #next column move
    
    if col> 3:  
        col=0   #reset to column 0
        row+=1  #move to next row
        
root.mainloop()  #run the main event loop