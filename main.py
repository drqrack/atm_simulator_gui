import tkinter as tk
from commands import check_balance

# Create the main window
root = tk.Tk()

# Add a title to main window
root.title("ATM Simulator")
# Specify main window size
root.geometry("500x400")

# Add account number entry
account_number_entry = tk.Entry(root, width=50)
account_number_entry.pack(side='top')

# Add check balance button
check_balance_btn = tk.Button(root, text="Check Balance", width='15', height='2', command=lambda:check_balance(account_number_entry.get()))
check_balance_btn.pack(side='top')

# Add deposit button
deposit_btn = tk.Button(root, text="Deposit", width='15', height='2')
deposit_btn.pack(side='top')

# Open the main window
root.mainloop()