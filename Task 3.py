import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("380x550")
root.resizable(False, False)
root.configure(bg="#1E1E1E")

expression = ""

display = tk.Entry(root,font=("Segoe UI", 24),bd=0,bg="#2D2D2D",fg="white",justify="right")
display.pack(fill="both", padx=15, pady=15, ipady=20)
 
def press(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)

def calculate():
    global expression
    try:
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expression = result
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""

frame = tk.Frame(root, bg="#1E1E1E")
frame.pack(expand=True, fill="both", padx=10, pady=10)

buttons = [
    ['C', '(', ')', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=', '%']
]

# Colors
number_bg = "#3A3A3A"
operator_bg = "#FF9500"
equal_bg = "#00B894"

def on_enter(e):
    e.widget["bg"] = "#5A5A5A"

def on_leave(e):
    if e.widget["text"] == "=":
        e.widget["bg"] = equal_bg
    elif e.widget["text"] in ['+', '-', '*', '/', '%']:
        e.widget["bg"] = operator_bg
    else:
        e.widget["bg"] = number_bg

for r, row in enumerate(buttons):
    frame.rowconfigure(r, weight=1)

    for c, text in enumerate(row):
        frame.columnconfigure(c, weight=1)

        if text == "=":
            bg = equal_bg
            cmd = calculate
        elif text == "C":
            bg = "#E74C3C"
            cmd = clear
        elif text in ['+', '-', '*', '/', '%']:
            bg = operator_bg
            cmd = lambda t=text: press(t)
        else:
            bg = number_bg
            cmd = lambda t=text: press(t)

        btn = tk.Button(frame,text=text,command=cmd,font=("Segoe UI", 18, "bold"),bg=bg,fg="white",bd=0,
            activebackground=bg, activeforeground="white", relief="flat", cursor="hand2")

        btn.grid(row=r,column=c,padx=6,pady=6,sticky="nsew")

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

root.mainloop()