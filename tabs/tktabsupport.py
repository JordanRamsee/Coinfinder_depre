"""

├──────┴────────────────────┴───────┴──────────────────────┤
│                       Description                        │
├──────────────────────────────────────────────────────────┤
│                                                          │
│                                                          │
└──────────────────────────────────────────────────────────┘
"""
from tkinter import *
from icons import *
from colors import *
from tksupport import *
from tabs.tkscrollableframe import *
from tabs.actions import *




class TabProperty:
    def __init__(self,base):
        self.tab_base_frame = base

    """
    This method generates three frames  called  Header,  Middle,
    and Footer  Frame.  The  Middle  Frame  is  designed  to  be 
    scrollable. If  the user fails to specify a height  for  any 
    of the frames, that particular frame will not be processed.
    """
    def create_frames(self, width: int = 1300 - 15, header_height: int = 0, middle_height: int = 0, bottom_height: int = 0):
        self.width = width
        # Header Frame
        self.header_frame = Frame(self.tab_base_frame, bg=Colors__.color()["working space"]["bg"], width=self.width,height=header_height, border=0, borderwidth=0, highlightthickness=0)
        if header_height != 0:
            self.header_frame.pack()
            self.header_frame.pack_propagate(False)
            # Header Bottom separation
            Label(self.header_frame, bg=Colors__.color()["working space"]["bg"]).pack()
        # Middle Frame
        self.middle_frame = Frame(self.tab_base_frame, bg=Colors__.color()["working space"]["bg"], border=0, borderwidth=0,highlightthickness=0)
        if middle_height != 0:
            self.middle_frame.pack()
            scroll_frame_obj =  TkScrollFrame(self.middle_frame,height=middle_height,width=self.width)
            self.data_show_frame = scroll_frame_obj.create_scrollable_frame()
        # Bottom Frame
        self.total_control_frame = Frame(self.tab_base_frame, bg=Colors__.color()["working space"]["bg"], width=1300 - 15,height=bottom_height, border=0, borderwidth=0, highlightthickness=0)
        if bottom_height != 0:
            self.total_control_frame.pack()
            self.total_control_frame.pack_propagate(False)

        return self.header_frame ,self.data_show_frame , self.total_control_frame

    """
    This particular section is tasked  with  generating  the
    header. The heading is determined by utilizing  the keys 
    from the 'column_data_details' dictionary.
    """
    def tree_view_heading(self,frame:object,column_data_details:dict):
        self.column_data_details = column_data_details

        header_column_data = {}
        for index, each_header_column_data in enumerate(list(self.column_data_details.keys())):
            header_column_data[each_header_column_data] = {}
            header_column_data[each_header_column_data]["frame"] = Frame(frame,width=self.column_data_details[each_header_column_data]["width"],height=40,padx=5,bg=Colors__.color()["task"]["bg"],border=0,borderwidth=0,highlightthickness=0)
            header_column_data[each_header_column_data]["frame"].pack(side=LEFT,anchor=W)
            header_column_data[each_header_column_data]["frame"].pack_propagate(False)

            if each_header_column_data != "Selector":
                header_column_data[each_header_column_data]["label"] = Label(header_column_data[each_header_column_data]["frame"],bg=Colors__.color()["task"]["bg"],fg=Colors__.color()["task"]["fg"],font=("Arial","11","bold"),pady=12,border=0,borderwidth=0,highlightthickness=0)
                header_column_data[each_header_column_data]["label"]["text"] = each_header_column_data
                header_column_data[each_header_column_data]["label"].pack()

            if index != len(list(self.column_data_details.keys()))-1:
                header_column_data[each_header_column_data]["seperator"] = Frame(frame,width=1,height=25,bg="#313132",border=0,borderwidth=0,highlightthickness=0)
                header_column_data[each_header_column_data]["seperator"].pack(side=LEFT,anchor=W)
                header_column_data[each_header_column_data]["seperator"].pack_propagate(False)



    def individual_data(self,base_frame,display_data):
        individual_data_frame11 = Frame(base_frame,width=1300-15,height=45,bg=Colors__.color()["task"]["bg"],border=0,borderwidth=0,highlightthickness=0)
        individual_data_frame11.pack()
        individual_data_frame11.pack_propagate(False)

        individual_data_frame = Frame(individual_data_frame11,width=1300-15,height=40,bg=Colors__.color()["task"]["bg"],border=0,borderwidth=0,highlightthickness=0)
        individual_data_frame.pack()
        individual_data_frame.pack_propagate(False)

        individual_data_seperator_frame = Frame(individual_data_frame11,width=1300-15,height=5,bg=Colors__.color()["working space"]["bg"],border=0,borderwidth=0,highlightthickness=0)
        individual_data_seperator_frame.pack()
        individual_data_seperator_frame.pack_propagate(False)


        column_data = {}
        for index,each_column_data in enumerate(list(self.column_data_details.keys())):
            column_data[each_column_data] = {}
            column_data[each_column_data]["frame"] = Frame(individual_data_frame,width=self.column_data_details[each_column_data]["width"],height=40,padx=5,bg=Colors__.color()["task"]["bg"],border=0,borderwidth=0,highlightthickness=0)
            column_data[each_column_data]["frame"].pack(side=LEFT,anchor=W)
            column_data[each_column_data]["frame"].pack_propagate(False)
            # Text Content
            if each_column_data == "Actions":
                self.individual_data_control(column_data[each_column_data]["frame"],individual_data_frame11,display_data,column_data)
            else:
                if each_column_data == "Selector":
                    column_data[each_column_data]["select_box_obj"] = TkWidget()
                    column_data[each_column_data]["select_box"] = column_data[each_column_data]["select_box_obj"].image_btn(column_data[each_column_data]["frame"] , imgTk=image__.icons("select_box".lower(),dimension=(14,14)), imgTk_hover=image__.icons("select_box".lower()+"_hover",dimension=(14,14)), dimension= (24,53), bg = Colors__.color()["task"]["bg"], activebackground = Colors__.color()["task"]["action bg"])
                    column_data[each_column_data]["select_box"].pack()
                    column_data[each_column_data]["select_box"]["command"] = lambda selected = False, btn_widget = column_data[each_column_data]["select_box"], btn_obj = column_data[each_column_data]["select_box_obj"], base_frame = individual_data_frame: self.toggle_checkbox(selected,btn_widget,btn_obj,base_frame)
                else:
                    column_data[each_column_data]["label"] = Label(column_data[each_column_data]["frame"],bg=Colors__.color()["task"]["bg"],fg=Colors__.color()["task"]["fg"],font=("Arial","11"),pady=12,border=0,borderwidth=0,highlightthickness=0)
                    column_data[each_column_data]["label"]["text"] = display_data[each_column_data]
                    if self.column_data_details[each_column_data]["text_align"].upper() == "CENTER":
                        column_data[each_column_data]["label"].pack()
                    else:
                        column_data[each_column_data]["label"].pack(anchor=self.column_data_details[each_column_data]["anchor"])

            if index != len(list(self.column_data_details.keys()))-1:
                column_data[each_column_data]["seperator"] = Frame(individual_data_frame,width=1,height=25,bg="#313132",border=0,borderwidth=0,highlightthickness=0)
                column_data[each_column_data]["seperator"].pack(side=LEFT,anchor=W)
                column_data[each_column_data]["seperator"].pack_propagate(False)

        # self.middle_frame_canvas.yview_moveto(1.0)
        # self.middle_frame_canvas.yview_moveto(1.0)  # Scrolls to the bottom


    def set_individual_data_control(self, controls:tuple=(), tab_name:str=""):
        self.control_btns = controls
        self.current_tab_name = tab_name

    def individual_data_control(self, frmae, root_frame, display_data, column_data):
        individual_control_frame = Frame(frmae,bg=Colors__.color()["task"]["bg"],pady=4,border=0,borderwidth=0,highlightthickness=0)
        individual_control_frame.pack()


        self.action_btn_bg_config = {
            "task": {
                "left" : {"width":32*3, "type": "double", "canvas_width":32*3, "bg":"red"},
                "right": {"width": 32+16, "type": "single", "canvas_width":32*2, "bg":"green"},
            },
            "billing": {
                "left": {"width": 32 + 16, "type": "single", "canvas_width":32*2, "bg":"red"},
                "right": {"width": 32 + 16, "type": "single", "canvas_width":32*2, "bg":"green"},
            }
        }

        self.action_btn_bg = {}
        for each_section_action in self.action_btn_bg_config[self.current_tab_name]:
            self.action_btn_bg[each_section_action] = Canvas(individual_control_frame,bg=Colors__.color()["task"]["bg"],height=40,width=self.action_btn_bg_config[self.current_tab_name][each_section_action]["width"],border=0,borderwidth=0,highlightthickness=0)
            self.action_btn_bg[each_section_action].pack(side=LEFT)
            self.action_btn_bg[each_section_action].pack_propagate()
            self.action_btn_bg[each_section_action+"_bg_image"] = control_base_image(type=self.action_btn_bg_config[self.current_tab_name][each_section_action]["type"])
            self.action_btn_bg[each_section_action].background = self.action_btn_bg[each_section_action+"_bg_image"]
            self.action_btn_bg[each_section_action].create_image(int((self.action_btn_bg_config[self.current_tab_name][each_section_action]["canvas_width"])/2), int(32/2), image=self.action_btn_bg[each_section_action+"_bg_image"])




        individual_control_btn = {}
        '''
        This  section pertains  to  the  action  buttons  and  their 
        respective functionalities within the task tab.
        '''
        if self.current_tab_name == "task":
            control_btn_details = {
                "run":  {"place": {"x": 20, "y": 8}},
                "edit": {"place": {"x": 60, "y": 8}},
            }
            for each_control_btn in control_btn_details:
                individual_control_btn[each_control_btn] = {}
                individual_control_btn[each_control_btn]["btn_obj"] = TkWidget()
                individual_control_btn[each_control_btn]["btn"] = individual_control_btn[each_control_btn]["btn_obj"].image_btn(self.action_btn_bg["left"] , imgTk=image__.icons(each_control_btn.lower(),dimension=(12,12)), imgTk_hover=image__.icons(each_control_btn.lower()+"_hover",dimension=(12,12)), dimension= (16,16), bg = Colors__.color()["task"]["action bg"], activebackground = Colors__.color()["task"]["action bg"])
                individual_control_btn[each_control_btn]["btn"].place(x=control_btn_details[each_control_btn]["place"]["x"],y=control_btn_details[each_control_btn]["place"]["y"])
            # Button Press Action
            individual_control_btn["run"]["btn"]["command"] = lambda Tk_btn_=individual_control_btn["run"],stage = "run", display_data= display_data : self.run_stop_each_individual(Tk_btn_,stage, display_data)
        elif self.current_tab_name == "billing":
            individual_control_btn["edit"] = {}
            individual_control_btn["edit"]["btn_obj"] = TkWidget()
            individual_control_btn["edit"]["btn"] = individual_control_btn["edit"]["btn_obj"].image_btn(self.action_btn_bg["left"] , imgTk=image__.icons("edit".lower(),dimension=(12,12)), imgTk_hover=image__.icons("edit".lower()+"_hover",dimension=(12,12)), dimension= (16,16), bg = Colors__.color()["task"]["action bg"], activebackground = Colors__.color()["task"]["action bg"])
            individual_control_btn["edit"]["btn"].place(x=15,y=8)
        # Edit Button Press Action
        individual_control_btn["edit"]["btn"]["command"] = lambda display_data = display_data, column_data=column_data : self.edit_data(display_data,column_data)

        # Delete Button
        individual_control_btn["delete"] = {}
        individual_control_btn["delete"]["btn_obj"] = TkWidget()
        individual_control_btn["delete"]["btn"] = individual_control_btn["delete"]["btn_obj"].image_btn(self.action_btn_bg["right"] , imgTk=image__.icons("delete".lower(),dimension=(12,12)), imgTk_hover=image__.icons("delete".lower()+"_hover",dimension=(12,12)), dimension= (16,16), bg = Colors__.color()["task"]["action bg"], activebackground = Colors__.color()["task"]["action bg"])
        individual_control_btn["delete"]["btn"].place(x=15,y=8)
        # Command
        individual_control_btn["delete"]["btn"]["command"] = lambda root_frame=root_frame, display_data = display_data : self.delete_data(root_frame, display_data)



    #need to change according to tab
    def run_stop_each_individual(self,Tk_btn_,stage,display_data):
        if stage == "run":
            Tk_btn_["btn_obj"].update_btn_image(imgTk=image__.icons("stop".lower(),dimension=(12,12)), imgTk_hover=image__.icons("stop".lower()+"_hover",dimension=(12,12)))
            Tk_btn_["btn"]["command"] = lambda Tk_btn_=Tk_btn_,stage = "stop" : self.run_stop_each_individual(Tk_btn_,stage,display_data)
            # Task Start Function
            task_tab_action_start(display_data)

        else:
            Tk_btn_["btn_obj"].update_btn_image(imgTk=image__.icons("run".lower(),dimension=(12,12)), imgTk_hover=image__.icons("run".lower()+"_hover",dimension=(12,12)))
            Tk_btn_["btn"]["command"] = lambda Tk_btn_=Tk_btn_,stage = "run" : self.run_stop_each_individual(Tk_btn_,stage,display_data)
            # Task Terminate Function
            task_tab_action_terminate(display_data)




    def delete_data(self,root_frame,display_data):
        if self.current_tab_name == "task":
            task_tab_action_delete(display_data)
        elif self.current_tab_name == "billing":
            billing_tab_action_delete(display_data)

        root_frame.destroy()


    def toggle_checkbox_highlighter(self,base_frame,color):
        for child in base_frame.winfo_children():
            if child.winfo_class() == "Frame":
                for child_ in child.winfo_children():
                    if child_.winfo_class() == "Label":
                        child_["fg"] = color


    # Need to change according to tab
    def toggle_checkbox(self,selected,btn_widget,btn_obj,base_frame):
        if selected == True:
            btn_obj.update_btn_image(imgTk=image__.icons("select_box".lower(),dimension=(14,14)), imgTk_hover=image__.icons("select_box".lower()+"_hover",dimension=(14,14)))
            btn_widget["command"] = lambda selected = False, btn_widget = btn_widget, btn_obj = btn_obj , base_frame=base_frame: self.toggle_checkbox(selected,btn_widget,btn_obj,base_frame)
            self.toggle_checkbox_highlighter(base_frame, Colors__.color()["task"]["fg"])
        else:
            btn_obj.update_btn_image(imgTk=image__.icons("select_box_selected".lower(),dimension=(14,14)), imgTk_hover=image__.icons("select_box_selected".lower()+"_hover",dimension=(14,14)))
            btn_widget["command"] = lambda selected = True, btn_widget = btn_widget, btn_obj = btn_obj, base_frame=base_frame: self.toggle_checkbox(selected,btn_widget,btn_obj,base_frame)
            self.toggle_checkbox_highlighter(base_frame, Colors__.color()["task"]["active fg"])


    def edit_data(self,display_data, column_data):
        if self.current_tab_name == "task":
            task_tab_action_edit(display_data,column_data)
        elif self.current_tab_name == "billing":
            billing_tab_action_edit(display_data,column_data)

