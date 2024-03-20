from tkinter import *
from tkinter import messagebox
import os
import random

game_number = 0
user_score = 0
comp_score = 0

choices = ["rock", "paper", "scissor"]
ch = random.choice(choices)
print(ch)


class Rock_paper_scissor():

    def __init__(self, root):
        global game_number
        global user_score
        global comp_score

        def rock():
            global choices
            comp_choice = random.choice(choices)
            if comp_choice == "rock":
                game(1, 0, 0, 1, 0, 0)
            elif comp_choice == "paper":
                game(1, 0, 0, 0, 1, 0)
            elif comp_choice == "scissor":
                game(1, 0, 0, 0, 0, 1)

        def paper():
            global choices
            comp_choice = random.choice(choices)
            if comp_choice == "rock":
                game(0, 1, 0, 1, 0, 0)
            elif comp_choice == "paper":
                game(0, 1, 0, 0, 1, 0)
            elif comp_choice == "scissor":
                game(0, 1, 0, 0, 0, 1)

        def scissor():
            global choices
            comp_choice = random.choice(choices)
            if comp_choice == "rock":
                game(0, 0, 1, 1, 0, 0)
            elif comp_choice == "paper":
                game(0, 0, 1, 0, 1, 0)
            elif comp_choice == "scissor":
                game(0, 0, 1, 0, 0, 1)

        def win():
            global game_number
            global user_score
            user_score += 1
            self.user_score_lbl.config(text="    User   : " + str(user_score))
            game_number += 1
            self.game_number_lbl.config(text="Game number: " + str(game_number))
            if user_score >= 10:
                messagebox.showinfo("Winner", "Congratulations!! You have won the game...")
                exit(1)

        def lose():
            global game_number
            global comp_score
            comp_score += 1
            self.comp_score_lbl.config(text="Computer: " + str(comp_score))
            game_number += 1
            self.game_number_lbl.config(text="Game number: " + str(game_number))
            if comp_score >= 10:
                messagebox.showinfo("Losser", "Computer wins!! Better luck next time...")
                exit(1)

        def game(u_r, u_p, u_s, c_r, c_p, c_s):
            if u_r == 1:
                self.user_label.config(height=250, width=250, image=self.userrock)
                self.user_label.place(x=75, y=25)
                if c_r == 1:
                    self.comp_label.config(height=250, width=250, image=self.comprock, bg="#6657FF")
                    self.comp_label.place(x=450, y=25)
                    self.user_label.config(bg="#6657FF")
                elif c_p == 1:
                    self.comp_label.config(height=250, width=250, image=self.comppaper, bg="#57FF66")
                    self.comp_label.place(x=450, y=25)
                    self.user_label.config(bg="#FF6657")
                    lose()
                elif c_s == 1:
                    self.comp_label.config(height=250, width=250, image=self.compscissor, bg="#FF6657")
                    self.comp_label.place(x=450, y=25)
                    self.user_label.config(bg="#57FF66")
                    win()
            elif u_p == 1:
                self.user_label.config(height=250, width=250, image=self.userpaper)
                self.user_label.place(x=75, y=25)
                if c_p == 1:
                    self.comp_label.config(height=250, width=250, image=self.comppaper, bg="#6657FF")
                    self.comp_label.place(x=450, y=25)
                    self.user_label.config(bg="#6657FF")
                elif c_s == 1:
                    self.comp_label.config(height=250, width=250, image=self.compscissor, bg="#57FF66")
                    self.comp_label.place(x=450, y=25)
                    self.user_label.config(bg="#FF6657")
                    lose()
                elif c_r == 1:
                    self.comp_label.config(height=250, width=250, image=self.comprock, bg="#FF6657")
                    self.comp_label.place(x=450, y=25)
                    self.user_label.config(bg="#57FF66")
                    win()
            elif u_s == 1:
                self.user_label.config(height=250, width=250, image=self.userscissor)
                self.user_label.place(x=75, y=25)
                if c_s == 1:
                    self.comp_label.config(height=250, width=250, image=self.compscissor, bg="#6657FF")
                    self.comp_label.place(x=450, y=25)
                    self.user_label.config(bg="#6657FF")
                elif c_r == 1:
                    self.comp_label.config(height=250, width=250, image=self.comprock, bg="#57FF66")
                    self.comp_label.place(x=450, y=25)
                    self.user_label.config(bg="#FF6657")
                    lose()
                elif c_p == 1:
                    self.comp_label.config(height=250, width=250, image=self.comppaper, bg="#FF6657")
                    self.comp_label.place(x=450, y=25)
                    self.user_label.config(bg="#57FF66")
                    win()

        self.userrock = PhotoImage(file="rock_player.png")
        self.userpaper = PhotoImage(file="paper_player.png")
        self.userscissor = PhotoImage(file="scissor_player.png")

        self.comprock = PhotoImage(file="rock_computer.png")
        self.comppaper = PhotoImage(file="paper_computer.png")
        self.compscissor = PhotoImage(file="scissor_computer.png")

        self.root = root
        self.root.title("Rock-Paper-Scissor")
        self.root.geometry("800x600+400+120")
        self.icon = PhotoImage(file="rockpaperscissor.png")
        self.root.iconphoto(True, self.icon)
        self.root.resizable(width=0, height=0)
        self.root.config(bg="#FDFFE6")

        # user label
        self.user_label = Label(self.root, font=("Century", 20, "bold"), text="User", bg="#FDFFE6", fg="#003F1B")
        self.user_label.place(x=200, y=125)

        # vs label
        self.vs_label = Label(self.root, font=("Century", 35, "bold"), text="VS", bg="#FDFFE6", fg="#3F1B00")
        self.vs_label.place(x=350, y=115)

        # Computer Label
        self.comp_label = Label(self.root, font=("Century", 20, "bold"), text="Computer", bg="#FDFFE6", fg="#1B003F")
        self.comp_label.place(x=500, y=125)

        # game detail labels

        self.game_number_lbl = Label(self.root, font=("Century", 15, "bold"), text="Game number: " + str(game_number),
                                     bg="#FDFFE6", fg="#2A5B35")
        self.game_number_lbl.place(x=0, y=565)

        # score

        self.score_fr = Frame(self.root, bg="#FDFFE6")
        self.score_fr.place(x=650, y=535)

        self.user_score_lbl = Label(self.score_fr, font=("Century", 15, "bold"), text="    User   : " + str(user_score),
                                    bg="#FDFFE6", fg="#352A5B")
        self.user_score_lbl.grid(row=0, column=0, sticky="w")

        self.comp_score_lbl = Label(self.score_fr, font=("Century", 15, "bold"), text="Computer: " + str(comp_score),
                                    bg="#FDFFE6", fg="#C74338")
        self.comp_score_lbl.grid(row=1, column=0, sticky="w")

        # Buttons

        self.rock_btn = Button(self.root, text="ROCK", height=2, width=10, font=("Century", 10, "bold"),
                               bg="#F1B7F8", activebackground="#F8F1B7", fg="#210324", activeforeground="#242103",
                               command=rock)
        self.rock_btn.place(x=190, y=375)

        self.paper_btn = Button(self.root, text="PAPER", height=2, width=10, font=("Century", 10, "bold"),
                                bg="#F1B7F8", activebackground="#F8F1B7", fg="#210324", activeforeground="#242103",
                                command=paper)
        self.paper_btn.place(x=340, y=375)

        self.scissor_btn = Button(self.root, text="SCISSOR", height=2, width=10, font=("Century", 10, "bold"),
                                  bg="#F1B7F8", activebackground="#F8F1B7", fg="#210324", activeforeground="#242103",
                                  command=scissor)
        self.scissor_btn.place(x=490, y=375)


if __name__ == "__main__":
    root = Tk()
    g = Rock_paper_scissor(root)
    root.mainloop()
