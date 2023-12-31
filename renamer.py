import os
import tkinter as tk
from tkinter import filedialog

def rename_files(directory_path, prefix=''):
    # The same code as before

def browse_directory():
    directory_path = filedialog.askdirectory()
    entry_directory.delete(0, tk.END)
    entry_directory.insert(0, directory_path)

def run_script():
    directory_path = entry_directory.get()
    prefix = entry_prefix.get()
    rename_files(directory_path, prefix)

# Create the main application window
root = tk.Tk()
root.title("File Renamer")

# Create widgets for user input
label_directory = tk.Label(root, text="Select Directory:")
entry_directory = tk.Entry(root, width=50)
button_browse = tk.Button(root, text="Browse", command=browse_directory)

label_prefix = tk.Label(root, text="Enter Prefix:")
entry_prefix = tk.Entry(root, width=50)

button_run = tk.Button(root, text="Run Script", command=run_script)

# Layout the widgets using the grid geometry manager
label_directory.grid(row=0, column=0, padx=10, pady=5)
entry_directory.grid(row=0, column=1, padx=10, pady=5)
button_browse.grid(row=0, column=2, padx=10, pady=5)

label_prefix.grid(row=1, column=0, padx=10, pady=5)
entry_prefix.grid(row=1, column=1, padx=10, pady=5)

button_run.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

# Start the main event loop
root.mainloop()
