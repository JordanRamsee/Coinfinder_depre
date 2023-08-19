import pickle
from tkinter import *
from tkinter import ttk
from window import *
from navigationbar import  *
from tksupport import *
from checklistcombobox import *
import ccxt
from storebilling import StoreBilling
from storeproxy import StoreProxy

# from tabs.actions import proxy_tab_action_add_new_data_to_DB
#
class AddNewCapture:
    def __init__(self,root_window,data_show_frame,tab_property,new_capture_id:str=''):
        self.new_capture_id = new_capture_id
        self.data_show_frame = data_show_frame
        self.tab_property = tab_property

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

    def property(self):

        # Loop through all the api keys and add them to the dropdown window
        billings = []
        api_dropdown_values = []

        # Read stored list of api key objects 
        with open("billingsfile.txt", "rb") as score_file:
            billings = []
            while True:
                try:
                    billings.append(pickle.load(score_file))
                except EOFError:
                    break
        
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
            "API Key": {"type": "ComboBox", "values": api_dropdown_values},
            "Proxy": {"type": "ComboBox", "values": proxy_dropdown_values},
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

                self.add_new_data_widget[each_info]["insert_data"] = ttk.Combobox(self.add_new_data_widget[each_info]["frame"],state="readonly", width=17,font=("Arial", "12", "normal"),style="TCombobox")
                self.add_new_data_widget[each_info]["insert_data"].pack(side=RIGHT,anchor=E,ipady=4)
                self.add_new_data_widget[each_info]["insert_data"]["value"] = self.entry_widget_info[each_info]["values"]


            elif self.entry_widget_info[each_info]["type"] == "Entry":
                self.add_new_data_widget[each_info]["insert_data"] = ttk.Entry(self.add_new_data_widget[each_info]["frame"], width=16+2, font=("Arial", "12", "normal"))
                self.add_new_data_widget[each_info]["insert_data"].pack(side=RIGHT,anchor=E,ipady=4,ipadx=2)

            elif self.entry_widget_info[each_info]["type"] == "CheckListComoboBox":
                self.entry_widget_info[each_info]["values_data"] = list()
                for value in self.entry_widget_info[each_info]["values"]:
                    self.entry_widget_info[each_info]["values_data"].append((value, tk.IntVar()))

                self.add_new_data_widget[each_info]["insert_data"] = CheckListComboBox(self.add_new_data_widget[each_info]["frame"], text=each_info, values = self.entry_widget_info[each_info]["values_data"], width=17,font=("Arial", "12", "normal"))
                self.add_new_data_widget[each_info]["insert_data"].pack(side=RIGHT,anchor=E,ipady=4)

                resultString = ""
                for value in self.entry_widget_info[each_info]["values_data"]:
                    if value[1].get() > 0:
                        resultString += value[0] + ", "
                    
                resultString.removesuffix(", ")


        save_btn_obj = TkWidget()
        save_btn = save_btn_obj.image_btn(self.data_entry_root_Frame , imgTk=image__.icons("save".lower()), imgTk_hover=image__.icons("save".lower()+"_hover"), dimension= (107+10,35+10), bg = Colors__.color()["navigation bar"]["selected tab"], activebackground = Colors__.color()["navigation bar"]["selected tab"])
        save_btn.pack()
        save_btn["command"] = self.save_btn_action


        billings = []
        try:
            # for reading also binary mode is important
            with open('billingsfile.txt', 'rb') as fp:
                n_list = pickle.load(fp)
                billings = n_list
                return billings
        except:
            billings = []
            return billings

    def get_balance(self, api_key, proxy):
        data_list = [{'asset': 'BNB', 'amount': '1000.00000000', 'date': '8/19/2023'},
                {'asset': 'BTC', 'amount': '1.00000000', 'date': '8/19/2023'},
                {'asset': 'BUSD', 'amount': '10000.00000000', 'date': '8/19/2023'},
                {'asset': 'ETH', 'amount': '100.00000000', 'date': '8/19/2023'},
                {'asset': 'LTC', 'amount': '500.00000000', 'date': '8/19/2023'},
                {'asset': 'TRX', 'amount': '500000.00000000', 'date': '8/19/2023'},
                {'asset': 'USDT', 'amount': '10000.00000000', 'date': '8/19/2023'},
                {'asset': 'XRP', 'amount': '50000.00000000', 'date': '8/19/2023'}]        
        return data_list


    def save_btn_action(self):
        '''
        Within this function, It will be adding  data  to  the  capture
        table and positioning it at the bottom of the capture  tab. The
        display_data dictionary contains the  information  that will
        be displayed in the capture table, and  it  must align with the
        keys present in self.entry_widget_info.
        '''

        
        
        display_data = {
            "ID": self.new_capture_id,
            "Coin": "",
            "Amount": "",
            "Date": "",
            "Actions": ""
        }


        # I NEED THE DATA FROM THE GET BALANCE FUNCTION TO BE DISPLAYED
        # I NEED TO PASS THE API KEY AND THE PROXY INTO THE FUNCTION
        data = self.get_balance("api_key", "proxy")

        for each_widget_data in list(display_data.keys())[1:-1]:
            display_data[each_widget_data] = str(self.add_new_data_widget[each_widget_data]["insert_data"].get()).strip()

        # Set Initial Status
        display_data["Status"] = "New"
        self.tab_property.individual_data(self.data_show_frame, display_data)

        # New capture adding to DB
        # capture_tab_action_add_new_data_to_DB(display_data)


        self.window.destroy()




if __name__ == "__main__":
    root = Tk()
    AddNewCapture(root)
    root.mainloop()