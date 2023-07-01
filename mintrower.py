"""
╔══════════════════════════════════════════════════════════╗
║                      mintrower.py                        ║
╚══════════════════════════════════════════════════════════╝
┌──────────────────────────────────────────────────────────┐
│                        Author                            │
├──────┬────────────────────┬───────┬──────────────────────┤
│ Name │ A S M Saad         │ Email │ asmsaad3@gmail.com   │
├──────┼────────────────────┼───────┼──────────────────────┤
│ Date │ June 6, 2023       │ Github│ asmsaad/mintrower    │
├──────┴────────────────────┴───────┴──────────────────────┤
│                       Description                        │
├──────────────────────────────────────────────────────────┤
│ This script serves as the main  script,  overseeing  the │
│ execution of all other scripts in a  hierarchical manner │
└──────────────────────────────────────────────────────────┘
"""
from icons import *
from activate import *


class MainWindow:
    def __init__(self):
        # Create a window
        self.root = Tk()

        ProductActivation(self.root)

        # Window configuration
        self.root.iconify()
        self.root.geometry("0x0")
        self.root.iconphoto(False, image__.icons("logo"))
        self.root.title("Mintrower")
        self.root.mainloop()


if __name__ == "__main__":
    MainWindow()
