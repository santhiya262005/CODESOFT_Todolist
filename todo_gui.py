import tkinter as tk
from tkinter import messagebox
import json
import os

FILENAME = "tasks.json"

# Load existing tasks
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

# Save tasks
def save_tasks():
    with open(FILENAME, "w") as file:
        json.dump(tasks, file)

# Add a new task
def add_task():
    task = entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        update_listbox()
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Update listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for i, t in enumerate(tasks):
        status = "✅" if t["completed"] else "❌"
        listbox.insert(tk.END, f"{i+1}. {t['task']} [{status}]")

# Mark selected task complete
def mark_completed():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["completed"] = True
        update_listbox()
        save_tasks()
    else:
        messagebox.showwarning("Select Task", "Please select a task to mark completed.")

# Delete selected task
def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = tasks.pop(index)
        update_listbox()
        save_tasks()
        messagebox.showinfo("Deleted", f"Deleted task: {task['task']}")
    else:
        messagebox.showwarning("Select Task", "Please select a task to delete.")

# --- GUI Setup ---
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
root.resizable(False, False)

tasks = load_tasks()

entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=10)

btn_add = tk.Button(root, text="Add Task", command=add_task, bg="lightgreen")
btn_add.pack()

listbox = tk.Listbox(root, width=50, height=12, font=("Arial", 10))
listbox.pack(pady=10)
update_listbox()

btn_done = tk.Button(root, text="Mark Completed", command=mark_completed, bg="lightblue")
btn_done.pack(pady=5)

btn_delete = tk.Button(root, text="Delete Task", command=delete_task, bg="tomato")
btn_delete.pack(pady=5)

root.mainloop()
