## Stopwatch , exercise group 3, Innovations
## 6/2/2026
##

## Constants
UPDATE_MILLIS = 100

## Global vars
running = False
count_time = 0.0    # seconds, float
last_update = 0.0   # unix epoch, not used.
update_count = 0

# Imports
import tkinter as tk
import time

##  Create the main application window
root = tk.Tk()
root.title("Stopwatch Team3")  # Set the window title
root.geometry("300x500") # Set the initial size of the window

# Function to be called when the button is clicked
def stop_start_click():
    """
    event handler for start/stop button
    :return:
    """
    timer.config(text="reset") # Update the label text

def lap_reset_click():
    """
    Event handler for button. Lap if running, reset if stopped
    :return:
    """
    pass

def update_display():
    global update_count
    update_count += 1
    timer.config(text=str(update_count))
    root.after(UPDATE_MILLIS, update_display)



# Add widgets
# Create text field
timer = tk.Label(root, text="00:00:00")

timer.pack(pady=20) # Use the pack geometry manager to place the widget with padding

# Create Buttons
button1 = tk.Button(root, text="Start", command=stop_start_click)
button1.pack(pady=10) # Place the button below the label
button2 = tk.Button(root, text="Reset", command=lap_reset_click)
button2.pack(pady=10) # Place the button below the label

# 3. Start the event loop
# This keeps the window open, waiting for user interactions (events)
update_display()
root.mainloop()
