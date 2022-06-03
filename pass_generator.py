from sqlite3 import Cursor
from tkinter import *
from tkinter import ttk
#from PIL import Image,ImageTk
from tkinter import messagebox
import string
import random

class password_generator:
    def __init__(self,root):
        self.root=root
        self.root.title("Password Generartor")
        self.root.geometry("650x445+370+140")
        
        main_frame=Frame(self.root,bd=5,relief=RIDGE)
        main_frame.place(x=0,y=0,width=650,height=445)
        
        title_lbl=Label(main_frame,text="PASSWORD GENERATOR SOFTWAARE",font=("times new roman",20,"bold"),fg="red",bg="white")
        title_lbl.place(x=0,y=0,width=650)
        
       # img1=Image.open(r"D:\python2\P.jpg")
        #img1=img1.resize((650,90),Image.ANTIALIAS)
        #self.photoimage1=ImageTk.PhotoImage(img1)
        #lblimg=Label(main_frame,image=self.photoimage1,font=("times new roman",20,"bold"),fg="red",bg="white")
        #lblimg.place(x=0,y=0,width=650)
        
        lenthlbl=Label(main_frame,text="Enter Password Length",font=("times new roman",20,"bold"),fg="blue")
        lenthlbl.place(x=40,y=150) 
        
        self.var_entry=StringVar()
        entry_fill=ttk.Entry(main_frame,textvariable=self.var_entry,width=55,font=("times new roman",15,"bold"))
        entry_fill.place(x=40,y=185)
        
        btn=Button(main_frame,text="GENERATE PASSWORD",font=("times new roman",15,"bold"),fg="white",bg="red",bd=4,relief=SUNKEN,cursor="hand2")
        btn.place(x=40,y=235,width=555,height=35)
        
        passlbl=Label(main_frame,text="Random Password Generator",font=("times new roman",20,"bold"),fg="blue")
        passlbl.place(x=40,y=290) 
        
    def pass_generator(self):
        if self.var_entry.get()=="":
            messagebox.showerror("Error","Please Enter some input")
        else:
            num=int(self.var_entry.get())        
            s1=string.ascii_lowercase
            s2=string.ascii_uppercase
            s3=string.digits
            s4=string.punctuation
            
            s=[]
            s.extend(list(s1))
            s.extend(list(s2))
            s.extend(list(s3))
            s.extend(list(s4))  
            
            random.shuffle(s)
            password=s[0:num]
            
            showdata=Label(self.root,text=password,font=("times new roman",20,"bold"),fg="blue",bd=5)
            showdata.place(x=40,y=290)
            
        
            
        
if __name__== "__main__":
    root=Tk() 
    app=password_generator(root)
    root.mainloop()        
        