"""
├──────┴────────────────────┴───────┴──────────────────────┤
│                       Description                        │
├──────────────────────────────────────────────────────────┤
│                                                          │
│                                                          │
└──────────────────────────────────────────────────────────┘
"""
from tkinter import *
from colors import *

class TkScrollFrame:
    def __init__(self, base_frame, height=0, width=0):
        self.base_frame = base_frame
        self.width = width
        self.height = height

    def create_scrollable_frame(self):
        self.scrollable_canvas = Canvas(self.base_frame, height=self.height, width=self.width, bg=Colors__.color()["working space"]["bg"], border=0, borderwidth=0, highlightthickness=0)
        self.scrollable_canvas.pack(side="left", fill="both", expand=True)
        # Scrollable Frame
        self.scrollable_frame = Frame(self.scrollable_canvas, bg=Colors__.color()["working space"]["bg"], padx=0, border=0, borderwidth=0, highlightthickness=0)
        self.scrollable_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        # Bind the mouse wheel event to the canvas
        self.scrollable_canvas.bind_all("<MouseWheel>", self.on_mousewheel)
        # Update the scroll region when the frame size changes
        self.scrollable_frame.bind("<Configure>", lambda e: self.scrollable_canvas.configure(scrollregion=self.scrollable_canvas.bbox("all")))

        # Add a scrollbar to the canvas
        self.scrollbar = Scrollbar(self.base_frame, orient="vertical", command=self.scrollable_canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollable_canvas.configure(yscrollcommand=self.scrollbar.set)

        return self.scrollable_frame

    def on_mousewheel(self,e):
        self.scrollable_canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")

class TKScrollCanvas(Canvas): 
    def __init__(self, master=None, cnf={}, **kw):
        # Call the parent constructor
        super().__init__(master, cnf, **kw)
        self.pack()
        # Scrollable Frame
        self.scrollable_frame = Frame(self)
        self.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        # Bind the mouse wheel event to the canvas
        self.bind_all("<MouseWheel>", self.on_mousewheel)
        # Update the scroll region when the frame size changes
        self.scrollable_frame.bind("<Configure>", lambda e: self.configure(scrollregion=self.bbox("all")))

    def on_mousewheel(self,e):
        self.yview_scroll(int(-1 * (e.delta / 120)), "units")



