import tkinter as tk  # Import the tkinter library for GUI
from time import strftime  # Import strftime from the time module to format time

# Create the main window for the application
root = tk.Tk()
root.title('Digital Clock')  # Set the title of the window

# Create a label widget to display the time
label = tk.Label(root, font=('calibri', 50, 'bold'), background='yellow',foreground='black')  # Set the font and background color
label.pack(anchor='center')  # Pack the label in the center of the window

# Define a function to update the time
def time():
    # Use strftime to get the current time in 12-hour format with AM/PM and the date
    string = strftime('%H:%M:%S %p\n%D')  # 12-hour format with AM/PM and the current date
    label.config(text=string)  # Update the label with the formatted time string
    label.after(1000, time)  # Call the time function again after 1000 milliseconds (1 second)

time()  # Call the time function to start the clock
root.mainloop()  # Start the Tkinter event loop, which keeps the window open and updates the clock
