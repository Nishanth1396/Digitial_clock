import tkinter as tk
from time import strftime

def update_time():
    string_time = strftime('%H:%M:%S %p')
    label.config(text=string_time)
    label.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title("Simple Clock")

# Create a label to display the time
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')

# Place the label in the center of the window
label.pack(anchor='center')

# Update the time initially and then every second
update_time()

# Run the Tkinter event loop
root.mainloop()