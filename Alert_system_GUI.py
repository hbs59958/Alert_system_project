# Project: Alert System GUI
# Author: Helina Semu
# Description: A Tkinter-based GUI application that displays system statuses (Normal, Attention Needed, Critical Error) 
# based on serial input from an Arduino. The status is updated dynamically with colors representing each state.

import tkinter as tk
from tkinter import messagebox
import serial
import threading

# Serial communication setup
ser = serial.Serial('COM3', 9600)
ser.flushInput()

# GUI setup
root = tk.Tk()
root.title("Alert System")

# Set the background color and window size
root.configure(bg="#282c34")  # Dark background
root.geometry("600x400")  # Set the window size

# Colors
NORMAL_COLOR = "green"        # Green for normal status
ATTENTION_COLOR = "blue"      # Blue for attention needed
CRITICAL_COLOR = "red"        # Red for critical error
UNKNOWN_COLOR = "gray"        # Gray for unknown status

# Create a frame for better organization
frame = tk.Frame(root, bg="#282c34")
frame.pack(expand=True)

# Create labels for status display with updated styles
status_label = tk.Label(frame, text="System Status", font=("Helvetica", 40), bg="#282c34", fg="white")
status_label.pack(pady=20)

status_message = tk.Label(frame, text="Normal", font=("Helvetica", 32), fg=NORMAL_COLOR, bg="#282c34")
status_message.pack(pady=20)

# Function to update the GUI based on serial data
def update_gui():
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            if line == "ATTENTION":
                status_message.config(text="Attention Needed", fg=ATTENTION_COLOR)
            elif line == "CRITICAL":
                status_message.config(text="Critical Error", fg=CRITICAL_COLOR)
            elif line == "NORMAL":
                status_message.config(text="Normal", fg=NORMAL_COLOR)
            else:
                status_message.config(text="Unknown Status", fg=UNKNOWN_COLOR)
        root.update_idletasks()
        root.update()

# Run the update_gui function in a separate thread
thread = threading.Thread(target=update_gui, daemon=True)
thread.start()

# Start the GUI loop
root.mainloop()
