import tkinter as tk
from tkinter import messagebox

# Function to calculate interest and total amount
def calculate_interest():
    try:
        # Get inputs from the user
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())

        # Determine which type of interest to calculate
        interest_type = interest_var.get()

        if interest_type == "Simple Interest":
            interest = (principal * rate * time) / 100
            total_amount = principal + interest
        elif interest_type == "Compound Interest":
            total_amount = principal * ((1 + (rate / 100)) ** time)
            interest = total_amount - principal
        else:
            messagebox.showerror("Error", "Please select an interest type.")
            return

        # Display the results
        result_label.config(
            text=f"Interest: {interest:.2f}\nTotal Amount: {total_amount:.2f}"
        )
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

# Create the main Tkinter window
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("350x400")
root.configure(bg="#FFA07A")  # Dark background color

# Labels and Entry Widgets
tk.Label(root, text="Principal (P):", bg="#2E4053", fg="white").grid(row=0, column=0, padx=10, pady=5)
entry_principal = tk.Entry(root, bg="#34495E", fg="white")
entry_principal.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Rate of Interest (R):", bg="#2E4053", fg="white").grid(row=1, column=0, padx=10, pady=5)
entry_rate = tk.Entry(root, bg="#34495E", fg="white")
entry_rate.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Time (T) in years:", bg="#2E4053", fg="white").grid(row=2, column=0, padx=10, pady=5)
entry_time = tk.Entry(root, bg="#34495E", fg="white")
entry_time.grid(row=2, column=1, padx=10, pady=5)

# Interest type selection
interest_var = tk.StringVar(value="Simple Interest")
tk.Label(root, text="Interest Type:", bg="#2E4053", fg="white").grid(row=3, column=0, padx=10, pady=5)
tk.Radiobutton(root, text="Simple Interest", variable=interest_var, value="Simple Interest", bg="#2E4053", fg="white").grid(row=3, column=1, sticky='w')
tk.Radiobutton(root, text="Compound Interest", variable=interest_var, value="Compound Interest", bg="#2E4053", fg="white").grid(row=4, column=1, sticky='w')

# Calculate Button
calculate_button = tk.Button(root, text="Calculate", command=calculate_interest, bg="#E74C3C", fg="white")
calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(root, text="Interest: \nTotal Amount: ", font=("Arial", 12), bg="#2E4053", fg="white")
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
