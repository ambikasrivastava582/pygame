# Import necessary libraries
import tkinter as tk
from datetime import date

# Create Window
root = tk.Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')

# Add widgets

# Main Label
lbl = tk.Label(
    root,
    text="Hey There!",
    fg="white",
    bg="#072F5F",
    height=1,
    width=30
)

# Label for name input
name_lbl = tk.Label(
    root,
    text="Full Name",
    bg="#3895D3"
)

# Entry box
name_entry = tk.Entry(root)

# Function to display message
def display():
    # Clear old text
    text_box.delete("1.0", tk.END)

    # Read user input
    name = name_entry.get()

    greet = "Hello " + name + "\n"
    message = "Welcome to the Application!\n"
    today = "Today's date is: " + str(date.today())

    # Insert text into text box
    text_box.insert(tk.END, greet)
    text_box.insert(tk.END, message)
    text_box.insert(tk.END, today)

# Text box
text_box = tk.Text(root, height=5, width=35)

# Button
btn = tk.Button(
    root,
    text="Begin",
    command=display,
    height=1,
    bg="#1261A0",
    fg='white'
)

# Organize widgets
lbl.pack(pady=10)
name_lbl.pack()
name_entry.pack(pady=5)
btn.pack(pady=10)
text_box.pack()

# Start GUI loop
root.mainloop()