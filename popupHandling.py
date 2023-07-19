# generate a class that has different methods to handle popups in tkinter
from tkinter import *
from colors import *

class PopupHandling:
    def __init__(self, window):
        self.window = window
        self.window.bind("<Configure>", self.allocate_window_area_EL)

        self.navigation_bar = Canvas(self.window, bg=Colors__.color()["navigation bar"]["bg"], border=0, borderwidth=0, highlightthickness=0)
        self.navigation_bar.pack(anchor=W)

        self.working_area = Canvas(self.window, bg=Colors__.color()["working space"]["bg"], border=0, borderwidth=0, highlightthickness=0)
        self.working_area.pack(anchor=W)

        self.allocate_window_area()

    def allocate_window_area(self):
        window_height = self.window.winfo_height()
        window_width = self.window.winfo_width()
        self.navigation_bar.config(height=30, width=window_width)
        self.working_area.config(height=window_height - 30, width=window_width)

    def allocate_window_area_EL(self, event):
        self.allocate_window_area()

    def drag_window(self, navigation_bar):
        self.iconify_window = None
        self.navigation_bar = navigation_bar
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0

        for each_widget in self.navigation_bar.winfo_children() + [self.navigation_bar]:
            if each_widget.winfo_class() != "Button":
                # print(each_widget.winfo_class(), each_widget.winfo_name())
                each_widget.bind("<Button-1>", self.on_drag_start)
                each_widget.bind("<ButtonRelease-1>", self.on_drag_stop)
                each_widget.bind("<B1-Motion>", self.on_drag_motion)

    def on_drag_start(self, event):
        self.offset_x = event.x
        self.offset_y = event.y
        self.dragging = True

    def on_drag_stop(self, event):
        self.dragging = False

    def on_drag_motion(self, event):
        if self.dragging:
            x = self.window.winfo_x() + event.x - self.offset_x
            y = self.window.winfo_y() + event.y - self.offset_y
            self.window.geometry("+{x}+{y}".format(x=x, y=y))

    def iconify_window(self):
        self.window.iconify()

    def deiconify_window(self):
        self.window.deiconify()

    def destroy_window(self):
        self.window.destroy()


    def error_popup(self, title, message):
        self.error_popup_window = Toplevel(self.window)
        self.error_popup_window.title(title)
        self.error_popup_window.resizable(False, False)
        self.error_popup_window.attributes("-topmost", True)
        self.error_popup_window.grab_set()
        self.error_popup_window.focus_set()
        self.error_popup_window.bind("<Escape>", lambda event: self.error_popup_window.destroy())
        self.error_popup_window.bind("<Return>", lambda event: self.error_popup_window.destroy())

        self.error_popup_window_label = Label(self.error_popup_window, text=message, font=("Helvetica", 12))
        self.error_popup_window_label.pack(pady=10)

        self.error_popup_window_button = Button(self.error_popup_window, text="OK", command=self.error_popup_window.destroy)
        self.error_popup_window_button.pack(pady=10)

        self.error_popup_window.mainloop()















