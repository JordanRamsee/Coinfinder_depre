"""
├──────┴────────────────────┴───────┴──────────────────────┤
│                       Description                        │
├──────────────────────────────────────────────────────────┤
│                                                          │
│                                                          │
└──────────────────────────────────────────────────────────┘
"""
from icons import *
from tksupport import *
from tkinter import ttk
from colors import *


class NavigationBarProperty:
    def __init__(self, navigation_bar,root_window = None,btns=("terminate","minimize")):
        self.naviagtion_bar_btns = btns
        self.root_window = root_window
        self.naviagtion_bar = navigation_bar

        #Left App Icon
        self.naviagtion_bar_app_icon = {}
        self.naviagtion_bar_app_icon["img_lbl_obj"] = TkWidget()
        self.naviagtion_bar_app_icon["img_lbl"] = self.naviagtion_bar_app_icon["img_lbl_obj"].img_label(self.naviagtion_bar, imgTk=image__.icons("logo",dimension=(37, 24)), dimension= (50, 32), bg = Colors__.color()["navigation bar"]["bg"])
        self.naviagtion_bar_app_icon["img_lbl"].pack(side=LEFT,anchor =W)





    def tab_frame(self):
        self.app_tab_frame = Frame(self.naviagtion_bar, bg="yellow", height=30,width=500,border=0,borderwidth=0, highlightthickness=0)
        self.app_tab_frame.pack(side=LEFT, anchor=W)

        return  self.app_tab_frame


    def notification(self):

        #Notification Btn
        self.notification_btn = {}
        self.notification_btn["btn_obj"] = TkWidget()
        self.notification_btn["btn"] =  self.notification_btn["btn_obj"].image_btn(self.naviagtion_bar , imgTk=image__.icons("notification",dimension=(20, 20)), imgTk_hover=image__.icons("notification_hover",dimension=(20, 20)), dimension= (32, 32), bg = Colors__.color()["navigation bar"]["bg"], activebackground = Colors__.color()["navigation bar"]["bg"])
        self.notification_btn["btn"].pack(side=RIGHT, anchor=E)
        #Status Change
        # PEnding Notification
        self.notification_btn["btn_obj"].update_btn_image(imgTk=image__.icons("pending_notification",dimension=(20, 20)), imgTk_hover=image__.icons("pending_notification_hover",dimension=(20, 20)))
        # NO pending Notification
        # self.notification_btn["btn_obj"].update_btn_image(imgTk=image__.icons("notification",dimension=(20, 20)), imgTk_hover=image__.icons("notification_hover",dimension=(20, 20)))

    def window_control(self):
        self.window_control_frame = Frame(self.naviagtion_bar,bg=Colors__.color()["navigation bar"]["bg"], border=0, borderwidth=0, highlightthickness=0)
        self.window_control_frame.pack(side=RIGHT, anchor=E)



        self.window_control_types = {
            "terminate": "",
            # "maximaize": "",
            "minimize": "",
        }

        self.window_control_btns = {}
        for column , each_window_control_type in enumerate(list(self.window_control_types.keys())):
            if each_window_control_type in self.naviagtion_bar_btns:
                self.window_control_btns[each_window_control_type] = {}
                self.window_control_btns[each_window_control_type]["btn_obj"] = TkWidget()
                self.window_control_btns[each_window_control_type]["btn"] =  self.window_control_btns[each_window_control_type]["btn_obj"].image_btn(self.window_control_frame , imgTk=image__.icons(each_window_control_type,dimension=(18, 18)), imgTk_hover=image__.icons(each_window_control_type+"_hover",dimension=(18, 18)), dimension= (32, 45), bg = Colors__.color()["navigation bar"]["bg"], activebackground = Colors__.color()["navigation bar"]["bg"])
                self.window_control_btns[each_window_control_type]["btn"].pack(side=RIGHT, anchor=E)

                if each_window_control_type == "terminate":
                    self.window_control_btns[each_window_control_type]["btn"]["command"] = self.terminate_window
                elif each_window_control_type == "minimize":
                    self.window_control_btns[each_window_control_type]["btn"]["command"] = self.minimize_window




        # self.notification()

    def terminate_window(self):
        if self.root_window == None:
            self.naviagtion_bar.winfo_toplevel().destroy()
        else:
            self.root_window.destroy()

    def minimize_window(self):
        self.naviagtion_bar.winfo_toplevel().withdraw()



