import tkinter as tk

# Function to update the entry field when a button is clicked
def button_click(value):
    entry.insert(tk.END, value)

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())  # Evaluate the mathematical expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for the display
entry = tk.Entry(root, width=20, font=("Arial", 18), bd=5, insertwidth=4, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), bg="red", command=clear)
    elif text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), bg="green", command=calculate)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

# Run the application
root.mainloop()
