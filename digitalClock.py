import tkinter as tk
from time import strftime, localtime

def update_time():
    current_time = localtime()
    string_time = strftime('%H:%M:%S %p', current_time)
    string_date = strftime('%A, %B %d, %Y', current_time)
    label.config(text=string_time + "\n" + string_date)

    # Change background color based on the time of day
    hour = current_time.tm_hour
    if 6 <= hour < 12:
        label.config(background='lightyellow', foreground='blue')
    elif 12 <= hour < 18:
        label.config(background='lightgreen', foreground='black')
    else:
        label.config(background='navajowhite', foreground='darkred')

    label.after(1000, update_time)

def toggle_mode():
    if mode.get() == 'Digital':
        mode.set('Analog')
    else:
        mode.set('Digital')

# Create the main window
root = tk.Tk()
root.title("Enhanced Clock")

# Title for the clock
title_label = tk.Label(root, text="My Awesome Clock", font=('calibri', 16, 'bold'))
title_label.pack(pady=10)

# Create a label to display the time and date
label = tk.Label(root, text="Yo Get Going", font=('calibri', 20, 'bold'), background='pink', foreground='blue', padx=20, pady=20)
label.pack(anchor='center')

# Button to toggle between digital and analog modes
mode = tk.StringVar() 
mode.set('Digital')
toggle_button = tk.Button(root, text="Toggle Mode", command=toggle_mode)
toggle_button.pack(pady=10)

# Update the time initially and then every second
update_time()

# Run the Tkinter event loop
root.mainloop()
