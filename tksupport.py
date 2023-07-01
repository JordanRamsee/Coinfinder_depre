"""
╔══════════════════════════════════════════════════════════╗
║                      tksupport.py                        ║
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
│                                                          │
│                                                          │
└──────────────────────────────────────────────────────────┘
"""
from tkinter import *


class TkWidget:
    def __init__(self):
        pass



    def img_label(self, base, imgTk: object = None, imgTk_hover: object = None,dimension: tuple = (32, 32), bg: str = "white"):
        self.img_label = Label(base, bg=bg, width = dimension[0], height=dimension[1],border=0, borderwidth=0,highlightthickness=0)
        self.img_label["image"] = imgTk
        self.img_label.image = imgTk
        return self.img_label

    def image_btn(self, base, imgTk: object = None, imgTk_hover: object = None,dimension: tuple = (32, 32), bg: str = "white", activebackground: str = "white"):
        self.hover_in_img  = imgTk_hover
        self.hover_out_img = imgTk
        self.btn = Button(base, bg=bg, activebackground=activebackground, width = dimension[0], height=dimension[1],border=0, borderwidth=0,highlightthickness=0)
        self.btn["image"] = imgTk
        self.btn.image = imgTk
        if imgTk_hover != None:
            self.btn.bind("<Enter>",self.image_btn_hover_in)
            self.btn.bind("<Leave>", self.image_btn_hover_out)
        return self.btn

    def update_btn_image(self,imgTk: object = None, imgTk_hover: object = None, bg=None):
        self.hover_in_img = imgTk_hover
        self.hover_out_img = imgTk
        self.btn["image"] = imgTk
        self.btn.image = imgTk

        if bg!=None:
            self.btn["bg"] = bg

    def image_btn_hover_in(self,event):
        self.btn["image"] = self.hover_in_img
        self.btn.image = self.hover_in_img

    def image_btn_hover_out(self,event):
        self.btn["image"] = self.hover_out_img
        self.btn.image = self.hover_out_img

