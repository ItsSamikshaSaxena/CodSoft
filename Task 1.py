import tkinter as tk
from tkinter import messagebox


def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def update_task():
    try:
        selected = task_listbox.curselection()[0]
        new_task = task_entry.get().strip()

        if new_task:
            task_listbox.delete(selected)
            task_listbox.insert(selected, new_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter updated task!")
    except:
        messagebox.showwarning("Warning", "Select a task to update!")

def clear_tasks():
    task_listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List Application")
root.geometry("850x550")
root.resizable(False, False)
bg_color = "#f0f0f0"
root.configure(bg=bg_color)


title_label = tk.Label(
    root,
    text="TO-DO LIST",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=10)


task_entry = tk.Entry(root, width=50, font=("Arial", 12))
task_entry.pack(pady=10)


button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_btn = tk.Button(button_frame,bg="lightgreen", text="Add Task", width=12, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

update_btn = tk.Button(button_frame, bg="lightblue", text="Update Task", width=12, command=update_task)
update_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(button_frame, bg="lightcoral", text="Delete Task", width=12, command=delete_task)
delete_btn.grid(row=0, column=2, padx=5)


task_listbox = tk.Listbox(
    root,
    width=50,
    height=12,
    font=("Arial", 12),
    selectbackground="lightblue"
)
task_listbox.pack(pady=15)

clear_btn = tk.Button(root, bg="lightgray", text="Clear All Tasks", width=20, command=clear_tasks)
clear_btn.pack(pady=10)


root.mainloop()
