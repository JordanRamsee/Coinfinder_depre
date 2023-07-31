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
from tabs.tasks import *
from tabs.billing import *
from tabs.capture import *
from tabs.proxy import *

class Tab:
    def __init__(self, tab_frame,working_canvas):
        self.tab_frame = tab_frame
        self.working_canvas =  working_canvas

        self.show_tabs()

    def show_tabs(self):
        self.tab_details = {
            "Task": {
                "img": {
                    "normal": image__.icons("task"),
                     "hover": image__.icons("task_hover"),
                     "selected": image__.icons("task_selected")
                },
                "bg" : Colors__.color()["working space"]["bg"],
            },
            "Billing": {
                "img": {
                    "normal": image__.icons("billing"),
                    "hover": image__.icons("billing_hover"),
                    "selected": image__.icons("billing_selected")
                },
                "bg" : Colors__.color()["working space"]["bg"],
            },
            "Proxies": {
                "img": {
                    "normal": image__.icons("proxies"),
                    "hover": image__.icons("proxies_hover"),
                    "selected": image__.icons("proxies_selected")
                },
                "bg" : Colors__.color()["working space"]["bg"],
            },

            "Capture": {
                "img": {
                    "normal": image__.icons("capture"),
                    "hover": image__.icons("capture_hover"),
                    "selected": image__.icons("capture_selected")
                },
                "bg" : Colors__.color()["working space"]["bg"],
            },

            "Settings": {
                "img": {
                    "normal": image__.icons("settings"),
                    "hover": image__.icons("settings_hover"),
                    "selected": image__.icons("settings_selected")
                },
                "bg" : Colors__.color()["working space"]["bg"],
            },

        }

        self.tab_btns = {}

        for individual_tab_name in self.tab_details:
            self.tab_btns[individual_tab_name] = {}
            self.tab_btns[individual_tab_name]["btn_obj"] = TkWidget()
            self.tab_btns[individual_tab_name]["btn"] = self.tab_btns[individual_tab_name]["btn_obj"].image_btn(self.tab_frame , imgTk=image__.icons(individual_tab_name.lower()), imgTk_hover=image__.icons(individual_tab_name.lower()+"_hover"), dimension= (110, 32), bg = Colors__.color()["navigation bar"]["bg"], activebackground = Colors__.color()["navigation bar"]["bg"])
            self.tab_btns[individual_tab_name]["btn"].pack(anchor=W,side=LEFT)
            self.tab_btns[individual_tab_name]["btn"].bind("<Button-1>",lambda e, tab_name = individual_tab_name : self.change_tab_action(e,tab_name))
            # Define Each Tab Frame
            self.tab_btns[individual_tab_name]["working_canvas"] = TKScrollCanvas(self.working_canvas,bg=self.tab_details[individual_tab_name]["bg"],height=750-30,width=1300,border=0,borderwidth=0,highlightthickness=0)
            self.tab_btns[individual_tab_name]["working_canvas"].pack_propagate(False)
            # print(individual_tab_name)

            if individual_tab_name == "Task" : TaskTab(self.tab_btns[individual_tab_name]["working_canvas"])
            elif individual_tab_name == "Billing": BillingTab(self.tab_btns[individual_tab_name]["working_canvas"])
            elif individual_tab_name == "Proxies": ProxyTab(self.tab_btns[individual_tab_name]["working_canvas"])
            elif individual_tab_name == "Capture": CaptureTab(self.tab_btns[individual_tab_name]["working_canvas"])
            elif individual_tab_name == "Settings": pass



        # Default Selected Tab
        default_selected_tab = list(self.tab_details.keys())[0]
        self.tab_btns[default_selected_tab]["btn_obj"].update_btn_image(imgTk=self.tab_details[default_selected_tab.capitalize()]["img"]["selected"], imgTk_hover=self.tab_details[default_selected_tab.capitalize()]["img"]["selected"] , bg = Colors__.color()["navigation bar"]["selected tab"])
        self.tab_btns[default_selected_tab]["working_canvas"].pack(anchor=W)



    def change_tab_action(self,event,tab_name):
        self.tab_btns[tab_name]["working_canvas"].pack(anchor=W)
        for each_tab_name in list(self.tab_details.keys()):
            if tab_name == each_tab_name:
                self.tab_btns[each_tab_name]["btn_obj"].update_btn_image(imgTk=self.tab_details[each_tab_name.capitalize()]["img"]["selected"], imgTk_hover=self.tab_details[each_tab_name.capitalize()]["img"]["selected"] , bg = Colors__.color()["navigation bar"]["selected tab"])
            else:
                self.tab_btns[each_tab_name]["btn_obj"].update_btn_image(imgTk=self.tab_details[each_tab_name.capitalize()]["img"]["normal"], imgTk_hover=self.tab_details[each_tab_name.capitalize()]["img"]["hover"] , bg = Colors__.color()["navigation bar"]["bg"])
                self.tab_btns[each_tab_name]["working_canvas"].pack_forget()





