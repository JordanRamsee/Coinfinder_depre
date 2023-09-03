from tkinter import *
from tkinter import ttk
from colors import *
from icons import *
from tksupport import *
# from addnewtask import *
from tabs.tktabsupport import *
from tabs.actions import *
from encryption import  decrypt

class TaskTab:
    list_of_tasks = []
    def __init__(self, base_canvas):
        self.base_canvas = base_canvas

        self.column_data_details = {
            "Selector": {"width": 35, "text_align": CENTER, "anchor": "center"},
            "ID": {"width": 50, "text_align": LEFT, "anchor": "center"},
            "Exchanges": {"width": 280 + 100, "text_align": LEFT, "anchor": W},
            "Proxy": {"width": 180, "text_align": LEFT, "anchor": W},
            "Crypto Pairs": {"width": 200, "text_align": LEFT, "anchor": W},
            "Exchanges for Proxy": {"width": 250, "text_align": LEFT, "anchor": W},
            "Actions": {"width": 160, "text_align": LEFT, "anchor": W},
        }

        self.tab_property = TabProperty(self.base_canvas)
        self.tab_property.set_individual_data_control(controls=("run", "edit", "delete"), tab_name="task")
        self.header_frame ,self.data_show_frame , self.total_control_frame = self.tab_property.create_frames(
            header_height=70,middle_height=540,bottom_height=58)
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
        tasks = []
        try:
            # for reading also binary mode is important
            with open('tasksfile.txt', 'rb') as fp:
                data = fp.read()
                decrypted_data = decrypt(data)
                n_list = pickle.loads(decrypted_data)
                tasks = n_list
        except:
            tasks = []

        for task in tasks:
            display_data = {
                "Selector": "",
                "ID": task.task_id,
                "Exchanges": task.exchanges,
                "Proxy": task.proxy,
                "Crypto Pairs": task.crypto_pair,
                "Exchanges for Proxy": task.proxy_exchanges,
                "Actions": "",
            }
            # Function that import data
            self.tab_property.individual_data(self.data_show_frame, display_data)


  
            
        

    def total_control_panel(self,frame):
        # Total Control button
        self.control_btns_details = {
            "add_new": {"dimension": (138 + 10, 32+10)},
            "delete_all": {"dimension": (129 + 10, 32 + 10)},
            "run_all": {"dimension": (114+10, 32+10)},
            "stop_all": {"dimension": (114+10, 32+10)},
        }

        self.left_control_frmae = Frame(frame, 
                                        bg=Colors__.color()["working space"]["bg"], 
                                        border=0, borderwidth=0, highlightthickness=0)
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
        self.total_control_btns["add_new"]["btn"]["command"] = lambda root_=self.base_canvas.winfo_toplevel(), task_tab_frame=self.data_show_frame, details=self.tab_property: task_tab_action_add_new_task(root_,task_tab_frame,details)
        self.total_control_btns["delete_all"]["btn"]["command"] =  self.tab_property.delete_all

        # Left Control Button's Frame
        for each_control_btn in list(self.control_btns_details.keys())[2:]:
            self.total_control_btns[each_control_btn] = {}
            self.total_control_btns[each_control_btn]["btn_obj"] = TkWidget()
            self.total_control_btns[each_control_btn]["btn"] = self.total_control_btns[each_control_btn]["btn_obj"].image_btn(self.right_control_frmae, imgTk=image__.icons(each_control_btn.lower()), imgTk_hover=image__.icons(each_control_btn.lower()+"_hover"), dimension=self.control_btns_details[each_control_btn]["dimension"], bg=Colors__.color()["working space"]["bg"], activebackground=Colors__.color()["working space"]["bg"])
            self.total_control_btns[each_control_btn]["btn"].pack(side=LEFT, anchor=W)
    