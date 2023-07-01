"""
╔══════════════════════════════════════════════════════════╗
║                      mainwindow.py                       ║
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
│ This  script  serves  as  the  primary  script  for  the │
│ MainWindow,   responsible    for   managing    all   the │
│ application's widgets, except for the activation window, │
│ in a hierarchical  manner. Its  role  is  to handle  the │
│ window properties of the MainWindow.                     │
└──────────────────────────────────────────────────────────┘
"""
from tab import *
from icons import *


class MainWindow:
    def __init__(self,root_window):
        self.root = root_window
        self.property()

    def property(self):
        # Create Main Window
        self.window = Toplevel()
        self.window_configuration = WindowConfiguration(self.window)
        self.window_configuration.geometry(1300, 700)
        self.window_configuration.resizable(width=False, height=False)
        self.navigation_bar_canvas, self.working_area_canvas = self.window_configuration.custom_navigation_bar()
        # Navigation bar design
        self.navigation_bar_property = NavigationBarProperty(self.navigation_bar_canvas, root_window=self.root)
        self.navigation_bar_property.window_control()  # Enable Window Control Buttons
        self.navigation_bar_property.notification()  # Notification Button
        # Add tab
        self.tab_frame = self.navigation_bar_property.tab_frame()
        Tab(self.tab_frame, self.working_area_canvas)
        # Enable Navigation-Bar Window Dragging
        self.window_configuration.draggable()

    def get_main_window(self):
        return self.window

if __name__ == "__main__":
    MainWindow()
