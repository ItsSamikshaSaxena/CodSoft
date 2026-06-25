import tkinter as tk
from tkinter import messagebox
import random
 
root = tk.Tk()
root.title("RPS Battle Arena")
root.geometry("900x650")
root.config(bg="#071330")
root.resizable(False, False)

 
player_score = 0
computer_score = 0
round_num = 0
max_rounds = 5

 
def play(user_choice):
    global player_score, computer_score, round_num

    if round_num >= max_rounds:
        messagebox.showinfo("Game Over", "Click Reset to play again!")
        return

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    player_choice_label.config(text=f" {user_choice}")
    computer_choice_label.config(text=f"{computer_choice}")

    if user_choice == computer_choice:
        result = "🤝 Draw!"
    elif ((user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")):
        player_score += 1
        result = "🏆 You Win!"
    else:
        computer_score += 1
        result = "💻 Computer Wins!"

    round_num += 1

    player_score_label.config(text=f" You: {player_score}")
    computer_score_label.config(text=f"Computer: {computer_score}")
    result_label.config(text=result)

    progress["text"] = "■" * round_num + "□" * (max_rounds - round_num)
    round_label.config(text=f"Round {round_num}/{max_rounds}")

    if round_num == max_rounds:
        if player_score > computer_score:
            final = "🎉 YOU WON THE MATCH!"
        elif computer_score > player_score:
            final = "😔 COMPUTER WON THE MATCH!"
        else:
            final = "🤝 MATCH DRAW!"

        messagebox.showinfo("Tournament Finished", final)


def reset_game():
    global player_score, computer_score, round_num

    player_score = 0
    computer_score = 0
    round_num = 0

    player_score_label.config(text=" You: 0")
    computer_score_label.config(text="Computer: 0")

    player_choice_label.config(text=" ?")
    computer_choice_label.config(text=" ?")

    result_label.config(text="🎮 READY TO PLAY!")
    round_label.config(text="Round 0/5")
    progress.config(text="□□□□□")


def exit_game():
    if messagebox.askyesno("Exit", "Do you want to exit?"):
        root.destroy()

 
header = tk.Label(root,text="ROCK PAPER SCISSORS",bg="#1A2747",fg="#FFD700",font=("Segoe UI", 28, "bold"),pady=15)
header.pack(fill="x", padx=20, pady=20)

score_frame = tk.Frame(root, bg="#071330")
score_frame.pack()

player_score_label = tk.Label(score_frame,text=" You: 0",bg="#071330",fg="white",font=("Segoe UI", 18, "bold"))
player_score_label.grid(row=0, column=0, padx=60)

computer_score_label = tk.Label(score_frame,text="Computer: 0",bg="#071330",fg="white",font=("Segoe UI", 18, "bold"))
computer_score_label.grid(row=0, column=1, padx=60)

 
arena = tk.Frame(root,bg="#1A2747",bd=3,relief="ridge")
arena.pack(pady=30, ipadx=80, ipady=30)

player_choice_label = tk.Label(arena,text=" ?",bg="#1A2747",fg="white",font=("Segoe UI", 22, "bold"))
player_choice_label.pack()

vs_label = tk.Label(arena,text="VS",bg="#1A2747",fg="#FFD700",font=("Segoe UI", 18, "bold"))
vs_label.pack(pady=10)

computer_choice_label = tk.Label(arena,text=" ?",bg="#1A2747",fg="white",font=("Segoe UI", 22, "bold"))
computer_choice_label.pack()

result_label = tk.Label(arena,text="🎮 READY TO PLAY!",bg="#1A2747",fg="#00E5FF",font=("Segoe UI", 20, "bold"))
result_label.pack(pady=20)

# ---------------- CHOICE BUTTONS ---------------- #
btn_frame = tk.Frame(root, bg="#071330")
btn_frame.pack(pady=20)

button_style = {"font": ("Segoe UI", 16, "bold"),"width": 12,"height": 2,"bg": "#344563",
    "fg": "white","activebackground": "#4F46E5","cursor": "hand2"}

tk.Button(btn_frame,text="🪨 Rock",command=lambda: play("Rock"),**button_style).grid(row=0, column=0, padx=15)

tk.Button( btn_frame, text="📄 Paper", command=lambda: play("Paper"), **button_style).grid(row=0, column=1, padx=15)

tk.Button( btn_frame, text="✂️ Scissors", command=lambda: play("Scissors"), **button_style).grid(row=0, column=2, padx=15)

round_label = tk.Label(root,text="Round 0/5",bg="#071330",fg="#FFD700",font=("Segoe UI", 16, "bold"))
round_label.pack(pady=10)

progress = tk.Label( root, text="□□□□□", bg="#071330",fg="#00E5FF",font=("Segoe UI", 20))
progress.pack()


control = tk.Frame(root, bg="#071330")
control.pack(pady=25)

tk.Button(control,text="🔄 Reset",command=reset_game,bg="#28A745",fg="white",font=("Segoe UI", 14, "bold"),width=12
).grid(row=0, column=0, padx=20)

tk.Button(control,text="❌ Exit",command=exit_game,bg="#DC3545",fg="white",font=("Segoe UI", 14, "bold"),width=12
).grid(row=0, column=1, padx=20)

root.mainloop()