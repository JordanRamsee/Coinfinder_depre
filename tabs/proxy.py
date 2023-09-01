from tkinter import *
from tkinter import ttk
from colors import *
from icons import *
from tksupport import *
from addnewproxy import *
from tabs.tktabsupport import *

class ProxyTab:
    def __init__(self, base_canvas):
        self.base_canvas = base_canvas

        self.column_data_details = {
            "Selector": {"width": 50, "text_align": CENTER, "anchor": "center"},
            "ID": {"width": 100, "text_align": LEFT, "anchor": "center"},
            "Proxy IP": {"width": 230, "text_align": LEFT, "anchor": W},
            "Proxy Port": {"width": 120+130, "text_align": LEFT, "anchor": W},
            "Proxy Username": {"width": 180+56, "text_align": LEFT, "anchor": W},
            "Proxy Password": {"width": 150+150, "text_align": CENTER, "anchor": W},
            "Actions": {"width": 112, "text_align": LEFT, "anchor": W},
        }

        self.tab_property = TabProperty(self.base_canvas)
        self.tab_property.set_individual_data_control(controls=("run", "edit"), tab_name="proxy")
        self.header_frame ,self.data_show_frame , self.total_control_frame = self.tab_property.create_frames(header_height=70,middle_height=540,bottom_height=58)
        #Make Heading
        self.tab_property.tree_view_heading(self.header_frame,self.column_data_details)
        #Total Control Area
        self.total_control_panel(self.total_control_frame)


        ''''
        In this section,  retrieve  the data from the  database that
        was previously imported. The initial  imported  data will be 
        displayed at the top  of  the frame. Ensure that the data is 
        provided,  as  the  display_data  dictionary   keys  remains 
        unchanged. 
        '''

        proxies = []
        try:
            # for reading also binary mode is important
            with open('proxiesfile.txt', 'rb') as fp:
                n_list = pickle.load(fp)
                proxies = n_list
        except:
            proxies = []

        for proxy in proxies:
            display_data = {
                "Selector": "",
                "ID": proxy.proxy_id,
                "Proxy IP": proxy.proxy_ip,
                "Proxy Port": proxy.proxy_port,
                "Proxy Username": proxy.proxy_username,
                "Proxy Password": proxy.proxy_password,
                "Actions": "",
            }
            # Function that import data
            self.tab_property.individual_data(self.data_show_frame, display_data)

    def total_control_panel(self,frame):
        # Total Control button
        self.control_btns_details = {
            "add_new_proxy": {"dimension": (138 + 10, 32+10)},
            "delete_all": {"dimension": (129 + 10, 32 + 10)},
        }

        self.left_control_frmae = Frame(frame, bg=Colors__.color()["working space"]["bg"], border=0, borderwidth=0, highlightthickness=0)
        self.left_control_frmae.pack(side=LEFT, anchor=W)

        self.right_control_frmae = Frame(frame, bg=Colors__.color()["working space"]["bg"], border=0, borderwidth=0, highlightthickness=0)
        self.right_control_frmae.pack(side=RIGHT, anchor=E)

        self.total_control_btns = {}
        for each_control_btn in list(self.control_btns_details.keys())[:2]:
            self.total_control_btns[each_control_btn] = {}
            self.total_control_btns[each_control_btn]["btn_obj"] = TkWidget()
            self.total_control_btns[each_control_btn]["btn"] = self.total_control_btns[each_control_btn]["btn_obj"].image_btn(self.left_control_frmae, imgTk=image__.icons(each_control_btn.lower()), imgTk_hover=image__.icons(each_control_btn.lower()+"_hover"), dimension=self.control_btns_details[each_control_btn]["dimension"], bg=Colors__.color()["working space"]["bg"], activebackground=Colors__.color()["working space"]["bg"])
            self.total_control_btns[each_control_btn]["btn"].pack(side=LEFT, anchor=W)
        # Add New Task Button Call
        self.total_control_btns["add_new_proxy"]["btn"]["command"] = lambda root_=self.base_canvas.winfo_toplevel(), task_tab_frame=self.data_show_frame, details=self.tab_property: proxies_tab_action_add_new_proxy(root_,task_tab_frame,details)
        self.total_control_btns["delete_all"]["btn"]["command"] =  self.tab_property.delete_all


        # Left Control Button's Frame
        for each_control_btn in list(self.control_btns_details.keys())[2:]:
            self.total_control_btns[each_control_btn] = {}
            self.total_control_btns[each_control_btn]["btn_obj"] = TkWidget()
            self.total_control_btns[each_control_btn]["btn"] = self.total_control_btns[each_control_btn]["btn_obj"].image_btn(self.right_control_frmae, imgTk=image__.icons(each_control_btn.lower()), imgTk_hover=image__.icons(each_control_btn.lower()+"_hover"), dimension=self.control_btns_details[each_control_btn]["dimension"], bg=Colors__.color()["working space"]["bg"], activebackground=Colors__.color()["working space"]["bg"])
            self.total_control_btns[each_control_btn]["btn"].pack(side=LEFT, anchor=W)























