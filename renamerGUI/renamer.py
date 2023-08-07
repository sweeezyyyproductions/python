import os
import tkinter as tk
from tkinter import filedialog

def rename_files(directory_path, prefix=''):
    files = os.listdir(directory_path)
    for file in files:
        # Add the renaming logic here using os.rename()
        # You can use os.path.join() to get the full file path
        new_filename = f"{prefix}{file}"
        os.rename(os.path.join(directory_path, file), os.path.join(directory_path, new_filename))

def browse_directory():
    directory_path = filedialog.askdirectory()
    entry_directory.delete(0, tk.END)
    entry_directory.insert(0, directory_path)
    update_example()  # Update the example label after selecting the directory

def update_example():
    directory_path = entry_directory.get()
    prefix = entry_prefix.get()

    # Fetch the first filename in the directory (if available)
    files = os.listdir(directory_path)
    first_filename = files[0] if files else ""

    example_label.config(text=f"Example: {prefix}{first_filename}")

def run_script():
    directory_path = entry_directory.get()
    prefix = entry_prefix.get()
    rename_files(directory_path, prefix)

# Create the main application window
main = tk.Tk()
main.title("File Renamer")

# Create widgets for user input
label_directory = tk.Label(main, text="Select Directory:")
entry_directory = tk.Entry(main, width=50)
button_browse = tk.Button(main, text="Browse", command=browse_directory)

label_prefix = tk.Label(main, text="Enter Prefix:")
entry_prefix = tk.Entry(main, width=50)
entry_prefix.bind("<KeyRelease>", lambda event: update_example())  # Bind the key release event to update_example()

button_run = tk.Button(main, text="Run Script", command=run_script)

# Create a Label widget to display an example of the renamed files
example_label = tk.Label(main, text="Example: ", fg="blue")

# Layout the widgets using the grid geometry manager
label_directory.grid(row=0, column=0, padx=10, pady=5)
entry_directory.grid(row=0, column=1, padx=10, pady=5)
button_browse.grid(row=0, column=2, padx=10, pady=5)

label_prefix.grid(row=1, column=0, padx=10, pady=5)
entry_prefix.grid(row=1, column=1, padx=10, pady=5)
example_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

button_run.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

# Start the main event loop
main.mainloop()
