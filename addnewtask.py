"""
╔══════════════════════════════════════════════════════════╗
║                      addnewtask.py                       ║
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

import pickle
from tkinter import *
from tkinter import ttk
from storetask import StoreTask
from window import *
from navigationbar import  *
from tksupport import *
from checklistcombobox import *
from encryption import encrypt , decrypt
# from tabs.actions import task_tab_action_add_new_data_to_DB
#
class AddNewTask:
    def __init__(self,root_window,data_show_frame,tab_property,new_task_id:str='' , edit = False , task_id = 0 , edited_column = None):
        self.new_task_id = new_task_id
        self.data_show_frame = data_show_frame
        self.tab_property = tab_property
        self.edit = edit
        self.task_id = task_id
        self.edited_column = edited_column
        self.exchange_values = []
        # those variables are used to store widgets for further use
        self.proxies_combobox = []
        self.exchange_for_proxies_combobox = []
        self.exchanges_widget = []
        self.crypto_pairs_widget = []
        # Create a window
        self.toplevel_window_obj = TkTopLevel(root_window.winfo_toplevel(),(350, 650))
        self.window = self.toplevel_window_obj.create()

        self.window_configuration = WindowConfiguration(self.window)
        # self.window_configuration.geometry(350, 550)
        self.window_configuration.geometry(350, 650)
        self.window_configuration.resizable(width=False, height=False)
        self.navigation_bar_canvas, self.working_area_canvas = self.window_configuration.custom_navigation_bar()
        # Navigation bar design
        self.navigation_bar_property = NavigationBarProperty(self.navigation_bar_canvas,btns=("terminate"))
        self.navigation_bar_property.window_control()  # Enable Window Control Buttons

        self.window_configuration.draggable()

        self.toplevel_window_obj.make_center_on_root_window()

        self.property()
        
        # save_btn_obj = TkWidget()
        # save_btn = save_btn_obj.image_btn(self.data_entry_root_Frame , imgTk=image__.icons("saveee".lower()), imgTk_hover=image__.icons("save".lower()+"_hover"), dimension= (107+10,35+10), bg = Colors__.color()["navigation bar"]["selected tab"], activebackground = Colors__.color()["navigation bar"]["selected tab"])
        # save_btn.pack()
        # save_btn["command"] = self.save_btn_action

    def property(self):
        

        billings = []
        api_dropdown_values = []

        # Read stored list of api key objects 
        with open("billingsfile.txt", "rb") as score_file:
            billings = []
            decrypted_data = decrypt(score_file.read())
            data = pickle.loads(decrypted_data)
            try:
                billings.append(data)
            except :
                pass
        
        # Checks to see if the list is empty, if it's pass and if it's not then add the id and exchange to the dropdown value
        if not billings:
            pass
        else:
            for billing in billings:
                for bill in billing:
                    api_dropdown_values.append(bill.key_id + '. ' + bill.exchange)


        proxies = []
        proxy_dropdown_values = []
        
        with open("proxiesfile.txt", "rb") as proxy_file:
            proxies = []
            while True:
                try:
                    proxies.append(pickle.load(proxy_file))
                except EOFError:
                    break
        
        if not proxies:
            pass
        else:
            for proxyObject in proxies:
                for proxy in proxyObject:
                    proxy_dropdown_values.append(proxy.proxy_ip + ':' + proxy.proxy_port)



        self.entry_widget_info = {
            # "Website": {"type": "CheckListComoboBox", "values": ["FinishLine/JD Sports US", "Footsites (US)", "Footsites (EU)", "Supreme (US)", "Supreme (EU)", "Demandware", "Yeezy Supply", "Kith EU", "Kith US"]},
            # "Billing Profile": {"type": "CheckListComoboBox", "values": ["Profile 1", "Profile 2", "Profile 3", "Profile 4"]},
            # "Proxy": {"type": "Entry", "values": []},
            # "Size": {"type": "Entry", "values": []},
            # "Keyword": {"type": "Entry", "values": []},
            "Exchanges": {"type": "CheckListComoboBox", "values": api_dropdown_values},
            "Proxy": {"type": "ComboBox", "values": []},
            "Crypto Pairs": {"type": "CheckListComoboBox", "values": ["All", "Large Cap"]},
            "Exchanges for Proxy" : {"type": "ComboBox", "values": ["All", "None"]}
        }

        self.data_entry_root_Frame = Frame(self.working_area_canvas,bg=Colors__.color()["navigation bar"]["selected tab"],height=650-32,width=350,border=0,borderwidth=0,highlightthickness=0)
        self.data_entry_root_Frame.pack()
        self.data_entry_root_Frame.pack_propagate(False)

        data_entry_Frame = Frame(self.data_entry_root_Frame,bg=Colors__.color()["navigation bar"]["selected tab"],height=580,width=350-15,pady=5,border=0,borderwidth=0,highlightthickness=0)
        data_entry_Frame.pack()
        # Set the initial theme
        # self.data_entry_Frame.tk.call("source", "res/Theme/azure.tcl")
        # self.data_entry_Frame.tk.call("set_theme", "dark")

        # Label(data_entry_Frame,text="11").pack()
        data_entry_Frame.pack_propagate(False)

        style = ttk.Style()
        style.theme_use('default')
        style.configure("Round.TButton", relief="flat", borderwidth=0, padding=6 , foreground="#9c9c9e" )

        style.configure("TCombobox", fieldbackground=Colors__.color()["task"]["bg"], background=Colors__.color()["task"]["bg"] ,  fieldforeground=[('readonly', 'blue')] , border=0,borderwidth=0,foreground="#9c9c9e")
        # style.configure("TCombobox.field", foreground="blue")
        style.configure("TEntry", fieldbackground=Colors__.color()["task"]["bg"], background=Colors__.color()["task"]["bg"],border=0,borderwidth=0,foreground="#9c9c9e")
        # style.configure("TCombobox.padding", padding=10)

        self.add_new_data_widget = {}
        for index, each_info in enumerate(list(self.entry_widget_info.keys())):
            self.add_new_data_widget[each_info] = {}
            self.add_new_data_widget[each_info]["frame"]= Frame(data_entry_Frame,bg=Colors__.color()["navigation bar"]["selected tab"],height=33,width=350-15,border=0,borderwidth=0,highlightthickness=0)
            self.add_new_data_widget[each_info]["frame"].pack(anchor=W)
            self.add_new_data_widget[each_info]["frame"].pack_propagate(False)

            self.add_new_data_widget[each_info]["label"] = Label(self.add_new_data_widget[each_info]["frame"],text=each_info,bg=Colors__.color()["navigation bar"]["selected tab"],fg="#9c9c9e",font=("Arial", "12", "normal"))
            self.add_new_data_widget[each_info]["label"].pack(side=LEFT,anchor=W)

            if self.entry_widget_info[each_info]["type"] == "ComboBox":

                self.add_new_data_widget[each_info]["insert_data"] = ttk.Combobox(self.add_new_data_widget[each_info]["frame"],state="readonly", width=17,font=("Arial", "12", "normal"),style="TCombobox" )
                self.add_new_data_widget[each_info]["insert_data"].pack(side=RIGHT,anchor=E,ipady=4)
                self.add_new_data_widget[each_info]["insert_data"]["value"] = self.entry_widget_info[each_info]["values"]
                self.add_new_data_widget[each_info]["insert_data"]["post"]
                if each_info == "Proxy":
                    self.proxies_combobox.append(self.add_new_data_widget[each_info]["insert_data"])
                    self.add_new_data_widget[each_info]["insert_data"]["postcommand"] = lambda : self.update_proxy_combobox_values()
                elif each_info == "Exchanges for Proxy":
                    self.exchange_for_proxies_combobox.append(self.add_new_data_widget[each_info]["insert_data"])
                    self.add_new_data_widget[each_info]["insert_data"]["postcommand"] = lambda : self.update_exchanges_combobox_values()
                    
            elif self.entry_widget_info[each_info]["type"] == "Entry":
                self.add_new_data_widget[each_info]["insert_data"] = ttk.Entry(self.add_new_data_widget[each_info]["frame"], width=16+2, font=("Arial", "12", "normal"))
                self.add_new_data_widget[each_info]["insert_data"].pack(side=RIGHT,anchor=E,ipady=4,ipadx=2)

            elif self.entry_widget_info[each_info]["type"] == "CheckListComoboBox":
                self.entry_widget_info[each_info]["values_data"] = list()
                for value in self.entry_widget_info[each_info]["values"]:
                    self.entry_widget_info[each_info]["values_data"].append((value, tk.IntVar()))

                self.add_new_data_widget[each_info]["insert_data"] = CheckListComboBox(self.add_new_data_widget[each_info]["frame"], text=each_info, values = self.entry_widget_info[each_info]["values_data"], width=17,font=("Arial", "12", "normal") , )
                if each_info == "Exchanges":
                    self.exchanges_widget = self.add_new_data_widget[each_info]["insert_data"]                     
                elif each_info == "Crypto Pairs":
                    self.crypto_pairs_widget = self.add_new_data_widget[each_info]["insert_data"]
                self.add_new_data_widget[each_info]["insert_data"].pack(side=RIGHT,anchor=E,ipady=4)

                resultString = ""
                for value in self.entry_widget_info[each_info]["values_data"]:
                    if value[1].get() > 0:
                        resultString += value[0] + ", "
                try:
                    resultString.removesuffix(", ")
                except:
                    pass

        save_btn_obj = TkWidget()
        save_btn = save_btn_obj.image_btn(self.data_entry_root_Frame , imgTk=image__.icons("save".lower()), imgTk_hover=image__.icons("save".lower()+"_hover"), dimension= (107+10,35+10), bg = Colors__.color()["navigation bar"]["selected tab"], activebackground = Colors__.color()["navigation bar"]["selected tab"])
        save_btn.pack()
        save_btn["command"] = self.save_btn_action

    def update_proxy_combobox_values(self):
        ''' 
        this method is used to change the values of the 
        proxy combobox based on the selected exchanges 
        '''
        values = []
        proxies = {
            "Binance" : ['aaa:aaa' , 'bbb:bbb' , 'ccc:ccc'] , 
            "Binance US" : ['111:111' , '222:222' , '333:333'] , 
            "Bitget" : ['AAA:AAA' , 'BBB:BBB' , 'CCC:CCC'],
            "Gemini" : ["&&&:&&&" , "***:***" , "###:###"]
            }
        selected_exchanges =  self.exchanges_widget.get_checked_values()
        for exchange in selected_exchanges:
            try : 
                proxy_list = proxies[exchange]
                values += proxy_list
            except KeyError:
                pass
            
        self.proxies_combobox[0]["values"] = values
        
    def update_exchanges_combobox_values(self):
        ''' 
        this method is used to change the values of the 
        exchange for proxies combobox based on the selected crypto pairs 
        '''
        values = []
        proxies = {
            "All" : ['option 1' , 'option 2' , 'option 3'] , 
            "Large Cap" : ['111' , '222' , '333'] , 
            }
        selected_crypto_pairs =  self.crypto_pairs_widget.get_checked_values()
        for exchange in selected_crypto_pairs:
            try : 
                proxy_list = proxies[exchange]
                values += proxy_list
            except KeyError:
                pass
            
        self.exchange_for_proxies_combobox[0]["values"] = values
    def save_btn_action(self):
       
        if self.edit:
            self.save_edited_task()
        else:
            self.add_new_task_data()
            
        
    def save_edited_task(self):
        tasks = []
            
        # for reading also binary mode is important
        try:
            with open('tasksfile.txt', 'rb') as fp:
                data = fp.read()
                decrypted_data = decrypt(data)
                n_list = pickle.loads(decrypted_data)
                # n_list = pickle.load(fp)
                for task in n_list:
                    if self.task_id == task.task_id:
                        n_list.remove(task)
                tasks = n_list      
        except:
            tasks = []
        
        display_data = {
        "ID": self.task_id,
        "Exchanges": "",
        "Proxy": "",
        "Crypto Pairs": "",
        "Exchanges for Proxy": "",
    }

        for each_widget_data in list(display_data.keys())[1:]:
            display_data[each_widget_data] = str(self.add_new_data_widget[each_widget_data]["insert_data"].get()).strip()
        updated_task = StoreTask(self.task_id, display_data["Exchanges"], display_data["Proxy"], display_data["Crypto Pairs"], display_data["Exchanges for Proxy"])
        print(updated_task.proxy_exchanges)
        tasks.append(updated_task)
        tasks = sorted(tasks , key = lambda k : k.task_id) 
        with open('tasksfile.txt', 'wb') as fp:
            data = pickle.dumps(tasks)
            encrypted_data = encrypt(data)
            fp.write(encrypted_data)
            # pickle.dump(tasks, fp)
            
       
        # update ui with the new data
        for key in display_data.keys():
            self.edited_column[f'{key}']["label"]["text"] = display_data[f'{key}']
        self.window.destroy()
        
    def add_new_task_data(self):
        '''
        Within this function, It will be adding  data  to  the  task
        table and positioning it at the bottom of the task  tab. The
        display_data dictionary contains the  information  that will
        be displayed in the task table, and  it  must align with the
        keys present in self.entry_widget_info.
        '''
        
        tasks = []
        try:
            # for reading also binary mode is important
            with open('tasksfile.txt', 'rb') as fp:
                data = fp.read()
                decrypted_data = decrypt(data)
                n_list = pickle.loads(decrypted_data)
                # n_list = pickle.load(fp)
                tasks = n_list
        except:
            tasks = []


        task_id = "1"
        try:
            for task in tasks:
                task_id = str(int(task.task_id) + 1)
        except:
            task_id = "1"
        
        display_data = {
            "ID": task_id,
            "Exchanges": "",
            "Proxy": "",
            "Crypto Pairs": "",
            "Exchanges for Proxy": "",
        }

        for each_widget_data in list(display_data.keys())[1:]:
            display_data[each_widget_data] = str(self.add_new_data_widget[each_widget_data]["insert_data"].get()).strip()

        # Set Initial Status
        display_data["Status"] = "New"
        self.tab_property.individual_data(self.data_show_frame, display_data)


        tasks.append(StoreTask(task_id, display_data["Exchanges"], display_data["Proxy"], display_data["Crypto Pairs"], display_data["Exchanges for Proxy"]))


        # store list in binary file so 'wb' mode
        with open('tasksfile.txt', 'wb') as fp:
            
            data = pickle.dumps(tasks)
            encrypted_data = encrypt(data)
            fp.write(encrypted_data)
            print('Done writing list into a binary file')


        # New task adding to DB
        # task_tab_action_add_new_data_to_DB(display_data)
      
        self.window.destroy()





if __name__ == "__main__":
    root = Tk()
    AddNewTask(root)
    root.mainloop()




