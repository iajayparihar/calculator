import tkinter as tk

# Function to update the input field when buttons are clicked
def click_button(value):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Function to evaluate the expression in the input field
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("600x700")
root.configure(bg="#f0f0f0")

# Entry field for input and output
entry = tk.Entry(root, width=20, font=("Arial", 36), borderwidth=2, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20, ipadx=10, ipady=10)

# Define buttons for the calculator with colors
buttons = [
    ('7', '#4caf50'), ('8', '#4caf50'), ('9', '#4caf50'), ('/', '#ff9800'),
    ('4', '#4caf50'), ('5', '#4caf50'), ('6', '#4caf50'), ('*', '#ff9800'),
    ('1', '#4caf50'), ('2', '#4caf50'), ('3', '#4caf50'), ('-', '#ff9800'),
    ('0', '#4caf50'), ('.', '#4caf50'), ('=', '#ff9800'), ('+', '#ff9800')
]

# Add buttons to the grid
tk.Button(root, text='C', width=5, height=2, font=("Arial", 24), bg='#f44336', command=clear).grid(row=1, column=3, columnspan=1, padx=10, pady=10)

row_val = 2
col_val = 0

for (button, color) in buttons:
    action = lambda x=button: click_button(x)
    tk.Button(root, text=button, width=5, height=2, font=("Arial", 24), bg=color, command=action).grid(row=row_val, column=col_val, padx=10, pady=10)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Special case for the 'C' button to clear the input field
tk.Button(root, text='=', width=5, height=2, font=("Arial", 24), bg='#ff9800', command=calculate).grid(row=5, column=2, columnspan=1, padx=10, pady=10)

# Run the application
root.mainloop()
