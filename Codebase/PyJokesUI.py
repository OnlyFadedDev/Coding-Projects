import pyjokes
import tkinter as tk
from tkinter import scrolledtext


user_input = input('How many jokes do you want to hear?: ')


def amount_of_jokes(user_input):
    jokes = []
    for i in range(int(user_input)):
        jokes.append(pyjokes.get_joke())
    return "\n\n".join(jokes)

# Create the main window
root = tk.Tk()

# Set the window size
root.geometry("800x600")

# Create a scrolled text widget with a specific size
scroll_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=30)
scroll_text.pack(padx=10, pady=10, expand=True, fill='both')

# Insert jokes into the scrolled text widget
scroll_text.insert(tk.INSERT, amount_of_jokes(user_input))

# Start the Tkinter event loop
root.mainloop()
