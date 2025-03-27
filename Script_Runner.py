# TODO fix documentation, implement script_checker to check if the file exists, then implement error handling for script_runner
# 4fun, does the process open another process?

# tkinter for building the graphical user interface
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# importing subprocess module to run my scripts as a subprocess rather than importing the files as a whole
import subprocess

# importing time simply for testing purposes
import time

# importing sys to handle running my python script as an executable (don't totally understand this yet)
import sys

# when called it removes the grid of specifically our run button
#       this is done to ensure the user cannot run multiple scripts at once using the launcher
def hide_button():
    run_script_button.grid_forget()
    
# This exists to recreate the grid of the buttons label to place it back when no active script is running
def return_button():
    run_script_button.grid(column=3, row=2, sticky=W)

# This will attempt to run the script, it will give the user a messagebox back that the script is invalid
#   should only run when attempting to run a script, which should only be clickable when no current script is running
#       !!!!!!!!!!! TOFIX? this is kinda bad, it doesn't check if the script exists, it just checks if our
#                   functions that runs the script hits an error?
#       !!!!!!!!!!! TOXFIX? Isn't showing errors at all atm...???
 
def script_checker():
    try:
        script_runner()
    except: 
        messagebox.showerror(title="Invalid Script", message="This is not recognized as a valid script")

# This should handle opening the script 
def script_runner():
    # Makes sure were referring to the current script in the global namespace
    global current_script
    
    # !!!!!!!!!!!!!! MIGHT want to change where we hide the button depending on how we want to implement the script_checker function
    hide_button()
    current_script = subprocess.Popen([sys.executable, f'IndividualScripts\\{osrs_script.get()}'])

def script_terminator():
    # Makes sure were referring to the current script in the global namespace
    global current_script

    # if there is no current script ongoing (current_script should be set to none at all time after script termination):
    #       terminate the script, return the start script button, set our current_script to None, alert user
    if current_script != None:
        current_script.terminate()
        return_button()
        current_script = None
        messagebox.showwarning(title="Script Finish", message="The script has been exited")
    # else, no script is currently running, return an error message (gui) and then return the start script button
    else:
        messagebox.showerror(title="No Script", message="No script should currently be running")
        # !!!!!!!!!!!!!!!!! MIGHT want to change returning the button here depending on how we handle hiding the button
        return_button()


# creating main graphical interface, root is the main graphical interface object created by calling the class Tk using Tk()
root = Tk()
root.title("OSRS Script Launcher")

# creating the main frame of the GUI, then creating a grid which contains some columns, rows, etc... styling stuff
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Creates a field to enter the name of our script, it expects a full name with the extension as well e.g. 'script1.py'
#       stores this in the ttk.Entry()'s textvariable parameter.
#       this is stored as a stringVar which is NOT a string, but an object which holds some string value, use .get() on it
#       also creates the visual grid/component of the entry field

osrs_script = StringVar()
osrs_script_entry = ttk.Entry(mainframe, width=20, textvariable=osrs_script)
osrs_script_entry.grid(column=2, row=1, sticky=(W,E))

# Creates the label and then the grid for our entry field for the script
ttk.Label(mainframe, text="Script Full File Name\ne.g. 'super_hack_script.py'").grid(column=3, row=1, sticky=W)

run_script_button = ttk.Button(mainframe, text="Run Script", command=script_checker)
run_script_button.grid(column=3, row=2, sticky=W)


# creates a button that handles ending the script
#   the command argument is where we handle running the script, it's what happens when the button is clicked
#   the .grid method called after we create the button, it handles the visual components of the button
ttk.Button(mainframe, text="End Script", command=script_terminator).grid(column=3, row=3, sticky=W)

# Our current script, should always be either None when no script is running, or set to our current script
current_script = None

# runs our GUI until the exit button is clicked/process closed
root.mainloop()