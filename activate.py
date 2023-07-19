"""
├──────┴────────────────────┴───────┴──────────────────────┤
│                       Description                        │
├──────────────────────────────────────────────────────────┤
│ This  script  serves  the   purpose  of   entering   the │
│ activation key and handling its processing. It is always │
│ the  initial  script  that  runs  when "mintrower.py" is │
│ executed.  Upon   receiving  a  favorable   response, it │
│ triggers the mandatory execution of "main.py".           │
└──────────────────────────────────────────────────────────┘
"""
from mainwindow import *
from popupHandling import PopupHandling
import requests
from eth_account.messages import defunct_hash_message
from web3 import Web3

class ProductActivation:
    def __init__(self, root_window):
        self.root = root_window
        self.root.bind("<Configure>", self.window_response)
        self.popup = PopupHandling(self.root)

        self.activation_key_check( force_from="window_execute")

    """
    This  function  verifying  if  user  have  obtained  a valid
    activation   key   from   the   previous   launch.   If  the 
    "product_already_activate" value is true, it  will open  the 
    main working interface.  Otherwise,  it  will switch to  the 
    activation window.
    """
    def check_valid_user(self, product_already_activate: bool = False):
        if product_already_activate == True:
            self.execute_main_window()
        else:
            self.activation_window()

    """Activation window configuration"""
    def activation_window(self):
        # Create the Activation Window
        self.window = Toplevel(self.root)
        self.window_configuration = WindowConfiguration(self.window)
        self.window_configuration.geometry(800, 450)
        self.window_configuration.resizable(width=False, height=False)
        self.navigation_bar_canvas, self.working_area_canvas = self.window_configuration.custom_navigation_bar()
        # Navigation Bar Design
        self.navigation_bar_property = NavigationBarProperty(self.navigation_bar_canvas)
        self.navigation_bar_property.window_control()  # Enable Window Control Buttons
        # Navigation Bar Dragging
        self.window_configuration.draggable()
        self.property()

    """Activation window Property(Widgets)"""
    def property(self):
        _Frame = Frame(self.working_area_canvas, bg=Colors__.color()["navigation bar"]["selected tab"], height=450 - 30, width=800, border=0, borderwidth=0, highlightthickness=0)
        _Frame.pack()
        _Frame.pack_propagate(False)
        # Top Margin Label
        Label(_Frame, pady=20, font=("Calibri Light", "16", "normal"), bg=Colors__.color()["navigation bar"]["selected tab"], fg="#9c9c9e", border=0, borderwidth=0, highlightthickness=0).pack(anchor=W)

        """Activation key"""
        activation_key_frame_1 = Frame(_Frame, pady=10, bg=Colors__.color()["navigation bar"]["selected tab"], border=0, borderwidth=0, highlightthickness=0)
        activation_key_frame_1.pack()
        # Activation Code Label Widget
        Label(activation_key_frame_1, text="Activation Key", font=("Calibri Light", "16", "normal"), bg=Colors__.color()["navigation bar"]["selected tab"], fg="#9c9c9e", border=0, borderwidth=0, highlightthickness=0).pack(anchor=W)
        # Activation Code Entry Widget
        self.activation_key = Entry(activation_key_frame_1, width=38, font=("Calibri Light", "14", "normal"), bg=Colors__.color()["task"]["bg"], fg="#4e4e4f", border=0, borderwidth=0, highlightthickness=0)
        self.activation_key.pack(ipady=3, anchor=W)

        """Wallet Address"""
        # wallet_address_frame = Frame(_Frame, pady=10, bg=Colors__.color()["navigation bar"]["selected tab"], border=0, borderwidth=0, highlightthickness=0)
        # wallet_address_frame.pack()
        # # Wallet Address Label Widget
        # Label(wallet_address_frame, text="Wallet Address", font=("Calibri Light", "16", "normal"), bg=Colors__.color()["navigation bar"]["selected tab"], fg="#9c9c9e", border=0, borderwidth=0, highlightthickness=0).pack(anchor=W)
        # # Wallet Address Entry Widget
        # self.wallet_address = Entry(wallet_address_frame, width=38, font=("Calibri Light", "14", "normal"), bg=Colors__.color()["task"]["bg"], fg="#4e4e4f", border=0, borderwidth=0, highlightthickness=0)
        # self.wallet_address.pack(ipady=3, anchor=W)

        """Second Activation key"""
        activation_key_frame_2 = Frame(_Frame, bg=Colors__.color()["navigation bar"]["selected tab"], pady=10, border=0, borderwidth=0, highlightthickness=0)
        # activation_key_frame_2.pack()
        # Second Activation Code Label Widget
        Label(activation_key_frame_2, text="Activation key-2", font=("Calibri Light", "16", "normal"), bg=Colors__.color()["navigation bar"]["selected tab"], fg="#9c9c9e", border=0, borderwidth=0, highlightthickness=0).pack(anchor=W)
        # Second Activation Code Entry Widget
        self.activation_key_2 = Entry(activation_key_frame_2, width=38, font=("Calibri Light", "14", "normal"), bg=Colors__.color()["task"]["bg"], fg="#4e4e4f", border=0, borderwidth=0, highlightthickness=0)
        self.activation_key_2.pack(ipady=3, anchor=W)

        """Activation Button"""
        activation_btn_Frame = Frame(_Frame, bg=Colors__.color()["navigation bar"]["selected tab"], pady=60, border=0, borderwidth=0, highlightthickness=0)
        activation_btn_Frame.pack()
        # Button
        activation_btn_obj = TkWidget()
        self.activation_btn = activation_btn_obj.image_btn(activation_btn_Frame, imgTk=image__.icons("activate".lower()), imgTk_hover=image__.icons("activate".lower() + "_hover"), dimension=(384 + 10, 32 + 10), bg=Colors__.color()["navigation bar"]["selected tab"], activebackground=Colors__.color()["navigation bar"]["selected tab"])
        self.activation_btn.pack()
        self.activation_btn["command"] = self.activation_key_check

    """
    Main window execution function.This function call MainWindow
    Class from mainwindow.py file
    """
    def execute_main_window(self):
        main_window = MainWindow(self.root)
        self.window = main_window.get_main_window()

    """Window controlling Event listener Function"""
    def window_response(self, e):
        self.root.iconify()
        if self.window.state() == 'normal':
            self.window.withdraw()
        elif self.window.state() == 'withdrawn':
            self.window.deiconify()

    """Activation key check function"""
    def activation_key_check(self,force_from="activation_key"):
        if force_from == "window_execute":
            """
            Here will be the code that determine whether the  activation
            key is present in previous records. If the key is found,  it 
            will be checked for validity.  If  the  key  is  valid,  the 
            "product_already_activated"  value  will   be  set to  True; 
            otherwise, it will be set to False.
            """
            # Default value
            # product_already_activate = False
            product_already_activate = True
            self.check_valid_user(product_already_activate=product_already_activate)

        elif force_from == "activation_key":
            self.activation_key_as_text = str(self.activation_key.get()).strip()
            self.activation_key_2_as_text = str(self.activation_key_2.get()).strip()
            # print(self.activation_key_as_text)
            """
            Here will be the code to check if the activation key is valid 
            or not. If it is valid, then set the  variable to  True, and 
            then execute the main window. 
            """
            from flaskapp import verified, verified_message, allow

            if verified and allow:
                self.window.destroy()
                self.execute_main_window()
            elif verified and not allow:
                self.popup.error_popup("Authenticated but not allowed",
                                       f"{verified_message}"
                                        )
            else:
                self.popup.error_popup("Not verified",
                                       f"{verified_message}"
                                        )



            # valid_activation_code = False

            # if valid_activation_code == True:
            #     self.window.destroy()
            #     self.execute_main_window()


