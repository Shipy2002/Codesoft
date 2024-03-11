from tkinter import *
from taskdb import *
class Todo:

    def __init__(self,root,db):

        #Button Functions
        def add_task():
            if self.task_etry.get()=="":
                return
            self.list_bx.insert(self.list_bx.size(),self.task_etry.get().capitalize())
            db.add_tsk(self.task_etry.get().capitalize())
            self.task_etry.delete(0,END)



        def delete_task():
            if self.list_bx.curselection()==():
                return
            self.db.delete_task(self.list_bx.get(self.list_bx.curselection()))
            self.list_bx.delete(self.list_bx.curselection())

        def clear_task():
            self.list_bx.delete(0,self.list_bx.size())
            self.db.clear_task()


        self.db=db
        self.root=root
        # self.icon=PhotoImage(file="task_icon.png")
        # self.root.iconphoto(True,self.icon)
        self.root.title("To-Do-List")
        self.root.geometry("640x410+300+150")
        #self.root.resizable(width=0, height=0)
        self.root.config(bg="#D6F6FA")

        self.todo_lbl= Label(self.root,text="TO-DO-LIST",font=("Bauhaus 93",40, "bold"),
                             fg="#41BEBD",bg="#E1F7FA")
        self.todo_lbl.pack(fill=X,side=TOP)

        #Buttons
        self.btn_fr= Frame(bg="#C1B2FA",width=100,padx=10,pady=10)
        self.btn_fr.pack(fill=Y,side=LEFT)

        self.task_etry = Entry(self.btn_fr,font=("Dubai",15),width=25,
                              bd=2,bg="#EDD8F7",fg="#37104A",relief=RIDGE)
        self.task_etry.grid(row=0,column=0,padx=10,pady=10,sticky='w')

        self.add_btn= Button(self.btn_fr,text="ADD",font=("Castellar",20, "bold"),
                             height=1,width=7,bg="#B2F3BF",fg="#0A4416",
                             activeforeground="#440A38",activebackground="#F3B2E6",command=add_task)
        self.add_btn.grid(row=1,column=0,padx=10,pady=5)

        self.dlt_btn = Button(self.btn_fr, text="DELETE", font=("Castellar", 20, "bold"),height=1,width=7,bg="#FDB8BB",fg="#430205",
                             activeforeground="#024340",activebackground="#B8FDFA",command=delete_task)
        self.dlt_btn.grid(row=2, column=0, padx=10, pady=25)

        self.clr_btn = Button(self.btn_fr, text="CLEAR", font=("Castellar", 20, "bold"), height=1, width=7,
                              bg="#FFE2A8", fg="#482F00",command=clear_task,
                              activeforeground="#001848", activebackground="#A8C6FF")
        self.clr_btn.grid(row=3, column=0, padx=10, pady=5)

        #list

        self.list_frm= Frame(self.root,width=100)
        self.list_frm.pack(fill=Y,side=RIGHT)

        self.list_bx=Listbox(self.list_frm,width=100,bg="#DEFFE7",fg="#00310D",font=("Comic Sans MS", 15),selectmode=SINGLE,selectbackground="#FFDEF6",
                             selectforeground="#310024")
        """adding existing tasks"""
        n=self.db.get_all()
        for i in range(self.db.task_count()):
            self.list_bx.insert(self.list_bx.size(),n[i][0])

        self.list_bx.pack(fill="both",side=LEFT)




def main():
    db=Database("Tasks.db")
    root=Tk()
    tdl=Todo(root,db)
    root.mainloop()

if __name__=="__main__":
    main()
