from tkinter import *
from tkinter import messagebox
import pyperclip
import string
import random
# pyperclip.copy("Hello")


final_pass=''
class Password_generator:

    def __init__(self,root):

        def generate_p():
            n=self.size_entry.get()
            if not n.isnumeric():
                self.size_entry.delete(0,END)
                messagebox.showerror(title="Invalid Input!!",message="Please Enter only number!!")
                self.password_lbl.delete("1.0", END)
            elif int(n)<6 or int(n)>26:
                self.size_entry.delete(0, END)
                messagebox.showwarning(title="Limit exceed", message="Password size allowed: 6 to 25")
                self.password_lbl.delete("1.0", END)
            else:
                n=int(n)

                upper = string.ascii_uppercase
                lower =string.ascii_lowercase
                digits = string.digits
                symbols="@#$%&*^!_-+*/|?"

                total=upper+lower+digits+symbols
                password= random.sample(total,n)
                global final_pass
                final_pass = "".join(password)
                self.password_lbl.delete("1.0",END)
                self.password_lbl.insert("1.0",final_pass)
                self.password_lbl.config(width=int(n*1.3))
                self.password_lbl.tag_configure("center", justify="center")
                self.size_entry.delete(0, END)

        def copy_p():
            global final_pass
            if final_pass == '':
                messagebox.showwarning(title="Password not generated", message="Generate the password first!!")
            else:
                pyperclip.copy(final_pass)
                messagebox.showinfo(title="Copied",message="Password copied successfully :)")


        def rearrange():
            global final_pass
            if final_pass == '':
                messagebox.showwarning(title="Password not generated", message="Generate the password first!!")
            else:
                password = random.sample(final_pass, len(final_pass))
                final_pass = "".join(password)
                self.password_lbl.delete("1.0", END)
                self.password_lbl.insert("1.0", final_pass)
                self.password_lbl.config(width=len(final_pass)+2)
                self.password_lbl.tag_configure("center", justify="center")
                self.size_entry.delete(0, END)

        def on_key_press(event):
            return "break"


        self.root = root
        self.root.title("Pass Word Generator")
        self.root.geometry("700x363+400+120")
        self.icon=PhotoImage(file="security.png")
        self.root.iconphoto(True,self.icon)
        self.root.resizable(width=0, height=0)
        self.root.config(bg="#f1d4ff")

        #title
        title_lbl = Label(root,text="Password Generator", font = ("Rockwell",35,"bold"),bg="#E2FFD4" ,fg="#48006C")
        title_lbl.pack(fill= X,side=TOP,pady=10,padx=10)

        #function frame
        self.func_fr = Frame(root,bg="#B0F0FF",width=650)
        self.func_fr.pack(side=TOP,fill=BOTH,padx=5)
        #size entry label
        self.size_lbl = Label(self.func_fr,text="Enter the size: ",font = ("Lucida Sans Typewriter",20,"bold"),bg="#B0F0FF")
        self.size_lbl.grid(row=0,column=0,sticky='w',padx=5,pady=5)
        #size entry
        self.size_entry = Entry(self.func_fr,width=20,font=("Lucida Sans Typewriter",20,"bold"))
        self.size_entry.grid(row=0, column=1, sticky='w',pady=5)
        #generate button
        self.gen_btn = Button(self.func_fr,width=10,text = "Generate",command=generate_p,font=("Lucida Sans Typewriter",16,"bold"),relief=RAISED,bg="#85feb6",activebackground="#FE85CD",fg="#003415",activeforeground="#34001F")
        self.gen_btn.grid(row=1, column=0,columnspan=2, sticky='w',padx=250,pady=5)
        #frame to show password in a text
        self.text_fr = Frame(self.func_fr)
        self.text_fr.grid(row=2, column=0,columnspan=2,pady=30)
        #password text
        self.password_lbl= Text(self.text_fr,bg="#a5bcff",height=1,wrap="word", state="normal",
                                font=("Times New Roman",30,"bold"),
                                fg="#00103f",relief=SUNKEN,selectforeground="#3F2F00",selectbackground="#FFE8A5")
        self.password_lbl.tag_configure("center", justify="center")
        password="Password"
        self.password_lbl.insert("1.0",password)
        self.password_lbl.config(width=len(password)+1)
        self.password_lbl.pack(side=TOP,fill=BOTH)
        #self.password_lbl.grid(row=2, column=0,columnspan=2,pady=15)
        self.password_lbl.tag_add("center", "1.0", "end")
        self.password_lbl.bind("<Key>", on_key_press)

        #button for copy

        self.cpy_btn = Button(self.func_fr,text = "Copy",
                              font=("Lucida Sans Typewriter",16,"bold"),
                              relief=RAISED,bg="#FFD6AD",width=10,
                              activebackground="#ADD6FF",fg="#2C1600",
                              activeforeground="#00162C",command=copy_p)
        self.cpy_btn.grid(row=3, column=0,pady=15)
        #button for rearranging
        self.cpy_btn = Button(self.func_fr, text="Rearrange",
                              font=("Lucida Sans Typewriter", 16, "bold"), bg="#ACB6D9",width=10,
                              activebackground="#D9CFAC", fg="#14192C",relief=RAISED,
                              activeforeground="#2C2714",command=rearrange)
        self.cpy_btn.grid(row=3, column=1, pady=15)



if __name__ == "__main__":
    root =Tk()
    k= Password_generator(root)
    root.mainloop()