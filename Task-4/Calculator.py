from tkinter import *



class Calculator:

    def __init__(self, root):
        # constants
        self.btns = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '.']

        def key_press(event):
            return "break"

        def button_click(sym):
            current = self.Entry_box.get()
            self.Entry_box.delete(0, END)
            self.Entry_box.insert(0, current + sym)

        def evaluate():
            try:
                current = self.Entry_box.get()
                op = eval(current)
                self.Entry_box.delete(0, END)
                self.Entry_box.insert(0, op)
            except:
                # messagebox.showerror("Error","Give valid Expression")
                self.Entry_box.delete(0, END)
                self.Entry_box.insert(0, "Error")

        def delete():
            cur = len(self.Entry_box.get())
            self.Entry_box.delete(cur - 1)

        def all_clear():
            self.Entry_box.delete(0, END)

        def plus_minus():

            current = self.Entry_box.get()
            self.Entry_box.delete(0, END)
            if current.isnumeric() or int(current) < 0:
                if int(current) > 0:
                    insert_val = "-" + current
                    self.Entry_box.insert(0, insert_val)
                else:
                    adder = str(int(current) * -1)
                    self.Entry_box.insert(0, adder)

            else:
                self.Entry_box.insert(END, current + "-")

        self.root = root
        self.root.geometry("410x350+630+200")
        self.root.title("Calculator")
        self.root.resizable(width=0, height=0)
        self.root.config(bg="#D9DED9")
        self.icon = PhotoImage(file="calculator_icon.png")
        self.root.iconphoto(True, self.icon)
        # textarea
        self.Entry_box = Entry(self.root, relief=SUNKEN, bg="#DED9DE", fg="#121412", justify=RIGHT,
                               bd=2, font=("Times New Roman", 40))
        self.Entry_box.pack(side=TOP, fill=X, padx=5, pady=2)
        self.Entry_box.bind("<Key>", key_press)

        # frame for buttons
        self.btn_fr = Frame(self.root, pady=10, bg="#D9DED9", padx=5)
        self.btn_fr.pack(fill=BOTH)

        # button-row1
        self.btn_7 = Button(self.btn_fr, command=lambda t=self.btns[7]: button_click(self.btns[7]), text=self.btns[7],
                            height=2, width=5, font=("Times New Roman", 15, "bold"), padx=5,
                            bg="#BEC3DA", activebackground="#DAD6BE", fg="#1A1D2E", activeforeground="#2E2A1A")
        self.btn_7.grid(row=0, column=0, padx=1, pady=1)

        self.btn_8 = Button(self.btn_fr, command=lambda t=self.btns[8]: button_click(self.btns[8]), text=self.btns[8],
                            height=2, width=5, font=("Times New Roman", 15, "bold"), padx=5,
                            bg="#BEC3DA", activebackground="#DAD6BE", fg="#1A1D2E", activeforeground="#2E2A1A")
        self.btn_8.grid(row=0, column=1, padx=1, pady=1)

        self.btn_9 = Button(self.btn_fr, command=lambda t=self.btns[9]: button_click(self.btns[9]), text=self.btns[9],
                            height=2, width=5, font=("Times New Roman", 15, "bold"), padx=5,
                            bg="#BEC3DA", activebackground="#DAD6BE", fg="#1A1D2E", activeforeground="#2E2A1A")
        self.btn_9.grid(row=0, column=2, padx=1, pady=1)

        self.btn_del = Button(self.btn_fr, text="DEL", height=2, width=5, font=("Times New Roman", 15, "bold"), padx=5,
                              bg="#ffbf78", activebackground="#78B8FF", fg="#361C00", activeforeground="#001A36",
                              command=delete)
        self.btn_del.grid(row=0, column=3, padx=1, pady=1)

        self.btn_ac = Button(self.btn_fr, text="AC", height=2, width=5, font=("Times New Roman", 15, "bold"), padx=5,
                             bg="#FF7F71", activebackground="#71F0FF", fg="#370600", activeforeground="#003137",
                             command=all_clear)
        self.btn_ac.grid(row=0, column=4, padx=1, pady=1)
        # button-row2

        self.btn_4 = Button(self.btn_fr, command=lambda t=self.btns[4]: button_click(self.btns[4]), text=self.btns[4],
                            height=2, width=5, font=("Times New Roman", 15, "bold"), padx=5,
                            bg="#BEC3DA", activebackground="#DAD6BE", fg="#1A1D2E", activeforeground="#2E2A1A")
        self.btn_4.grid(row=1, column=0, padx=1, pady=1)

        self.btn_5 = Button(self.btn_fr, command=lambda t=self.btns[5]: button_click(self.btns[5]), text=self.btns[5],
                            height=2, width=5, font=("Times New Roman", 15, "bold"), padx=5,
                            bg="#BEC3DA", activebackground="#DAD6BE", fg="#1A1D2E", activeforeground="#2E2A1A")
        self.btn_5.grid(row=1, column=1, padx=1, pady=1)

        self.btn_6 = Button(self.btn_fr, command=lambda t=self.btns[6]: button_click(self.btns[6]), text=self.btns[6],
                            height=2, width=5, font=("Times New Roman", 15, "bold"), padx=5,
                            bg="#BEC3DA", activebackground="#DAD6BE", fg="#1A1D2E", activeforeground="#2E2A1A")
        self.btn_6.grid(row=1, column=2, padx=1, pady=1)

        self.btn_mul = Button(self.btn_fr, command=lambda t=self.btns[12]: button_click(self.btns[12]),
                              text=self.btns[12], height=2, width=5, font=("Times New Roman", 15, "bold"), padx=5,
                              bg="#CFE279", activebackground="#8C79E2", fg="#2F370C", activeforeground="#140C37")
        self.btn_mul.grid(row=1, column=3, padx=1, pady=1)

        self.btn_div = Button(self.btn_fr, command=lambda t=self.btns[13]: button_click(self.btns[13]),
                              text=self.btns[13], height=2, width=5, font=("Times New Roman", 15, "bold"), padx=5,
                              bg="#CFE279", activebackground="#8C79E2", fg="#2F370C", activeforeground="#140C37")
        self.btn_div.grid(row=1, column=4, padx=1, pady=1)

        # butto row_3

        self.btn_1 = Button(self.btn_fr, command=lambda t=self.btns[1]: button_click(self.btns[1]), text=self.btns[1],
                            height=2, width=5, font=("Times New Roman", 15, "bold"), padx=5,
                            bg="#BEC3DA", activebackground="#DAD6BE", fg="#1A1D2E", activeforeground="#2E2A1A")
        self.btn_1.grid(row=2, column=0, padx=1, pady=1)

        self.btn_2 = Button(self.btn_fr, command=lambda t=self.btns[2]: button_click(self.btns[2]), text=self.btns[2],
                            height=2, width=5, font=("Times New Roman", 15, "bold"), padx=5,
                            bg="#BEC3DA", activebackground="#DAD6BE", fg="#1A1D2E", activeforeground="#2E2A1A")
        self.btn_2.grid(row=2, column=1, padx=1, pady=1)

        self.btn_3 = Button(self.btn_fr, command=lambda t=self.btns[3]: button_click(self.btns[3]), text=self.btns[3],
                            height=2, width=5, font=("Times New Roman", 15, "bold"), padx=5,
                            bg="#BEC3DA", activebackground="#DAD6BE", fg="#1A1D2E", activeforeground="#2E2A1A")
        self.btn_3.grid(row=2, column=2, padx=1, pady=1)

        self.btn_add = Button(self.btn_fr, command=lambda t=self.btns[10]: button_click(self.btns[10]),
                              text=self.btns[10], height=2, width=5, font=("Times New Roman", 15, "bold"), padx=5,
                              bg="#CFE279", activebackground="#8C79E2", fg="#2F370C", activeforeground="#140C37")
        self.btn_add.grid(row=2, column=3, padx=1, pady=1)

        self.btn_sub = Button(self.btn_fr, command=lambda t=self.btns[11]: button_click(self.btns[11]),
                              text=self.btns[11], height=2, width=5, font=("Times New Roman", 15, "bold"), padx=5,
                              bg="#CFE279", activebackground="#8C79E2", fg="#2F370C", activeforeground="#140C37")
        self.btn_sub.grid(row=2, column=4, padx=1, pady=1)

        # final row

        self.btn_0 = Button(self.btn_fr, command=lambda t=self.btns[0]: button_click(self.btns[0]), text=self.btns[0],
                            height=2, width=5, font=("Times New Roman", 15, "bold"), padx=5,
                            bg="#918ACA", activebackground="#C3CA8A", fg="#18152F", activeforeground="#2C2F15")
        self.btn_0.grid(row=3, column=0, padx=1, pady=1)

        self.btn_dot = Button(self.btn_fr, command=lambda t=self.btns[14]: button_click(self.btns[14]),
                              text=self.btns[14], height=2, width=5, font=("Times New Roman", 15, "bold"), padx=5,
                              bg="#42BDBB", activebackground="#BD4244", fg="#112F2F", activeforeground="#2F1111")
        self.btn_dot.grid(row=3, column=1, padx=1, pady=1)

        self.btn_plusminus = Button(self.btn_fr, text="±", height=2, width=5, font=("Times New Roman", 15, "bold"),
                                    padx=5,
                                    bg="#42BDBB", activebackground="#BD4244", fg="#112F2F", activeforeground="#2F1111",
                                    command=plus_minus)
        self.btn_plusminus.grid(row=3, column=2, padx=1, pady=1)

        self.btn_equal = Button(self.btn_fr, text="=", height=2, width=10, command=evaluate,
                                font=("Times New Roman", 15, "bold"), padx=14,
                                bg="#8AFFAE", activebackground="#FF8ADB", fg="#002C0E", activeforeground="#2C001F")
        self.btn_equal.grid(row=3, column=3, columnspan=2, padx=1, pady=1)


if __name__ == "__main__":
    root = Tk()
    g = Calculator(root)
    root.mainloop()
