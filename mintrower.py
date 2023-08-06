"""
├──────┴────────────────────┴───────┴──────────────────────┤
│                       Description                        │
├──────────────────────────────────────────────────────────┤
│ This script serves as the main  script,  overseeing  the │
│ execution of all other scripts in a  hierarchical manner │
└──────────────────────────────────────────────────────────┘
"""
from icons import *
from activate import *
import threading
from flaskapp import app
import os

class MainWindow:
    def __init__(self):
        # Create a window
        self.root = Tk()

        ProductActivation(self.root)

        # Window configuration
        self.root.iconify()
        self.root.geometry("800x600")  # Set an appropriate initial size
        self.root.iconphoto(False, image__.icons("logo"))
        self.root.title("Mintrower")
        self.root.mainloop()

def flask_runner():
    app.run()

if __name__ == "__main__":

    # Set up the flag
    closed_flag = threading.Event()

    # Create a thread for the main window
    main_thread = threading.Thread(target=MainWindow)
    main_thread.start()

    # Create a thread for Flask app
    flask_thread = threading.Thread(target=flask_runner, daemon=True)
    flask_thread.start()

    # Wait for any of the threads to complete
    main_thread.join()
    closed_flag.set()  # Set the flag to indicate that a window has been closed

    # Check if the Flask thread is still running
    if flask_thread.is_alive():
        os._exit(0)  # Exit the script forcibly