import random
import tkinter as tk

window = tk.Tk()
window.geometry("250x250")
window.title("Rock Paper & Scissors")
window.resizable(height=0,width=0)

user_score = 0
comp_score = 0
user_choice = ""
comp_choice = ""

def choice_to_number(choice):
    rps = {"rock": 0, "paper": 1, "scissors": 2}
    return rps[choice]

def number_to_choice(number):
    rps = {0: "rock", 1: "paper", 2: "scissors"}
    return rps[number]

def random_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Score count
text_area = tk.Text(master=window, width=30, height=12, bg="yellow")
text_area.grid(row=3, column=1,columnspan=3)

def result(human_choice, comp_choice):
    global user_score
    global comp_score
    user = choice_to_number(human_choice)
    comp = choice_to_number(comp_choice)
    if user == comp:
        print("Tie")
    elif (user - comp) % 3 == 1:
        print("You win")
        user_score += 1
    else:
        print("Computer win")
        comp_score += 1
    text_area.delete(1.0, tk.END)  # Clear previous content
    answer = "Your choice: {uc}\nComputer Choice: {cc}\nYour score: {u}\nComp score: {c}".format(
        uc=user_choice, cc=comp_choice, u=user_score, c=comp_score
    )
    text_area.insert(tk.END, answer)

def rock():
    global user_choice
    global comp_choice
    user_choice = "rock"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)

def paper():
    global user_choice
    global comp_choice
    user_choice = "paper"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)

def scissors():
    global user_choice
    global comp_choice
    user_choice = "scissors"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)

btn1 = tk.Button(text="   Rock   ", width=8, height=2, bg="skyblue", command=rock)
btn1.grid(row=0, column=1, padx=3, pady=3)

btn2 = tk.Button(text="   Paper   ", width=8, height=2, bg="pink", command=paper)
btn2.grid(row=0, column=2, padx=3, pady=3)

btn3 = tk.Button(text="   Scissors   ", width=8, height=2, bg="green", command=scissors)
btn3.grid(row=0, column=3, padx=3, pady=3)

window.mainloop()