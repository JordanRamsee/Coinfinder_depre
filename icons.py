"""
╔══════════════════════════════════════════════════════════╗
║                        icons.py                          ║
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
from PIL import Image, ImageTk, ImageFont, ImageDraw
from colors import *
import datetime



'''This function make tab button image'''
def tab_button_icon(icon:object = None, text:str = None, text_bg:str = None, img_width:int = 286, img_original_height:int =18, diff_icon_text:int = 250, place_icon:str = "left", rounded:bool = False,round_bg:str='#242437'):
    # Determine text image width and height
    width, height = (len(text)*img_width, 512)
    # Text position
    if rounded :
        position = (0, 150)
        font = ImageFont.truetype('./res/fonts/OxfordStreet.ttf', size=422 - 90)
    else:
        position = (0,110)
        font = ImageFont.truetype('./res/fonts/OxfordStreet.ttf', size=422)



    # Create Text Image with transparent background
    text_image = Image.new("RGBA", (width, height), 0)

    draw = ImageDraw.Draw(text_image)
    draw.text(position, text, font=font, fill=text_bg)
    # text_image.show()

    # Text Image with Icon with transparent background
    total_width = width + 512 + diff_icon_text
    merged_image = Image.new("RGBA", (total_width, height), 0)
    if place_icon.lower() == 'left':
        merged_image.paste(icon, (0, int((512-icon.size[1])/2)))
        merged_image.paste(text_image, (512+diff_icon_text, 0))
    else:
        merged_image.paste(text_image, (0, 0))
        merged_image.paste(icon, (total_width - icon.size[0], int((512-icon.size[1])/2)))

    # Rounded Shape
    if rounded == True:
        round_shape_img = Image.new("RGBA", (total_width+300, height+150), 0)
        round_rect = ImageDraw.Draw(round_shape_img)
        round_rect.rounded_rectangle((0,0,total_width+300, height+150),radius=120,fill=round_bg)
        round_shape_img.paste(merged_image,(150,80),merged_image)
        merged_image = round_shape_img
        final_image = merged_image.resize((int((total_width/height)*img_original_height),img_original_height),Image.LANCZOS)
        # print(text,final_image.size)
        return final_image

    final_image = merged_image.resize((int((total_width/height)*img_original_height),img_original_height),Image.LANCZOS)
    # final_image.show()
    # print(final_image.size)
    return ImageTk.PhotoImage(final_image)



def control_base_image(type:str="double"):
    _custom_height =28
    new_img = Image.new("RGBA",(512*3,512),0)
    draw = ImageDraw.Draw(new_img)

    if type=="double":
        width_ , height_ = (512*3,512)
        radius = 100
    else:
        width_, height_ = (512 * 2, 512)
        radius = 130

    border= 12
    draw.rounded_rectangle((0,0,width_,height_),fill=Colors__.color()["task"]["separator"],radius=radius)
    draw.rounded_rectangle((border,border,width_-border,height_-border),fill=Colors__.color()["task"]["action bg"],radius=radius-10)
    if type == "double":
        draw.rounded_rectangle((int(width_/2)-int((border-10)/2),int((height_/3)/2), int(width_/2)+int((border-10)/2), height_-int((height_/3)/2) ), fill=Colors__.color()["task"]["separator"], radius=150)

    mod_img  =  new_img.resize( (int(width_/height_)*_custom_height,_custom_height) , Image.LANCZOS)
    # mod_img.show()

    return ImageTk.PhotoImage(mod_img)


def activation_btn_img(bg="normal"):
    if bg=="normal":
        fill_color = "#37de8f"
    else:
        fill_color = "#5fe5a5"
    _custom_height = 32
    radius = 100
    width_, height_ = (int(512 * 15), int(512*1.2))
    new_img = Image.new("RGBA", (width_, height_), 0)
    draw = ImageDraw.Draw(new_img)
    draw.rounded_rectangle((0, 0, width_, height_), fill=fill_color, radius=radius)
    font = ImageFont.truetype('./res/fonts/OxfordStreet.ttf', size=422)
    position = (int(width_/2)-512-150, 210-50)
    draw.text(position, "Activate", font=font, fill="white")

    mod_img = new_img.resize((int(width_ / height_) * _custom_height, _custom_height), Image.LANCZOS)

    # print(mod_img.size)
    # mod_img.show()

    return mod_img



# activation_btn_img()
# tab_button_icon(icon = Image.open("./res/icons/control/plus.png").resize((300,300),Image.LANCZOS), text = "CREATE TASK", text_bg  = "#cecfc6", img_width  = 200, img_original_height  =32, diff_icon_text  = 0, place_icon = "right",rounded=True,round_bg='#242437')
# tab_button_icon(icon = Image.open("./res/icons/control/plus.png").resize((300,300),Image.LANCZOS), text = "CREATE TASK", text_bg  = "#e5e6dc", img_width  = 200, img_original_height  =32, diff_icon_text  = 0, place_icon = "right",rounded=True,round_bg='#242437')
#
# tab_button_icon(icon = Image.open("./res/icons/control/_delete.png").resize((320,320),Image.LANCZOS), text =   "DELETE  ALL", text_bg  = "#cecfc6", img_width  = 200-13, img_original_height  =32, diff_icon_text  = 0, place_icon = "right",rounded=True,round_bg='#242437')
# tab_button_icon(icon = Image.open("./res/icons/control/_delete.png").resize((320,320),Image.LANCZOS), text =   "DELETE  ALL", text_bg  = "#e5e6dc", img_width  = 200-13, img_original_height  =32, diff_icon_text  = 0, place_icon = "right",rounded=True,round_bg='#242437')

# tab_button_icon(icon = Image.open("./res/icons/control/play.png").resize((300,300),Image.LANCZOS), text =   "START ALL", text_bg  = "#ffffff", img_width  = 200-13, img_original_height  =32, diff_icon_text  = 0, place_icon = "right",rounded=True,round_bg='#37cd8f')
# tab_button_icon(icon = Image.open("./res/icons/control/play.png").resize((300,300),Image.LANCZOS), text =   "START ALL", text_bg  = "#e6e6e6", img_width  = 200-13, img_original_height  =32, diff_icon_text  = 0, place_icon = "right",rounded=True,round_bg='#37cd8f')
#
# tab_button_icon(icon = Image.open("./res/icons/control/_stop.png").resize((300,350),Image.LANCZOS), text =   " STOP ALL", text_bg  = "#ffffff", img_width  = 200-13, img_original_height  =32, diff_icon_text  = 0, place_icon = "right",rounded=True,round_bg='#f54e64')
# tab_button_icon(icon = Image.open("./res/icons/control/_stop.png").resize((300,350),Image.LANCZOS), text =   " STOP ALL", text_bg  = "#e6e6e6", img_width  = 200-13, img_original_height  =32, diff_icon_text  = 0, place_icon = "right",rounded=True,round_bg='#f54e64')



'''This Class return images into Tk formate. By the use of dimension argument user can chage the image diameter'''
class image__:
    def __init__(self) -> None:
        pass

    def icons(name, dimension=()):
        if name == "logo": return ImageTk.PhotoImage(Image.open("./res/icons/logo.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))


        # Window control
        elif name == "terminate": return ImageTk.PhotoImage(Image.open("./res/icons/terminate.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))
        elif name == "terminate_hover": return ImageTk.PhotoImage(Image.open("./res/icons/terminate_hover.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))
        elif name == "minimize": return ImageTk.PhotoImage(Image.open("./res/icons/minimize.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))
        elif name == "minimize_hover": return ImageTk.PhotoImage(Image.open("./res/icons/minimize_hover.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))


        # Notification
        elif name == "notification": return ImageTk.PhotoImage(Image.open("./res/icons/notification.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))
        elif name == "notification_hover": return ImageTk.PhotoImage(Image.open("./res/icons/notification_hover.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))
        elif name == "pending_notification": return ImageTk.PhotoImage(Image.open("./res/icons/pending_notification.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))
        elif name == "pending_notification_hover": return ImageTk.PhotoImage(Image.open("./res/icons/pending_notification_hover.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))


        # Tab
        elif name == "task": return tab_button_icon(icon=Image.open("./res/icons/tabs/task.png"),text="Tasks",text_bg=Colors__.color()["navigation bar"]["fg"]["normal"],img_width=193)
        elif name == "task_hover": return tab_button_icon(icon=Image.open("./res/icons/tabs/task_hover.png"),text="Tasks",text_bg=Colors__.color()["navigation bar"]["fg"]["hover"],img_width=193)
        elif name == "task_selected": return tab_button_icon(icon=Image.open("./res/icons/tabs/task_selected.png"),text="Tasks",text_bg=Colors__.color()["navigation bar"]["fg"]["selected"],img_width=193)

        elif name == "billing": return tab_button_icon(icon=Image.open("./res/icons/tabs/billing.png"),text="Billings",text_bg=Colors__.color()["navigation bar"]["fg"]["normal"],img_width=193)
        elif name == "billing_hover": return tab_button_icon(icon=Image.open("./res/icons/tabs/billing_hover.png"),text="Billings",text_bg=Colors__.color()["navigation bar"]["fg"]["hover"],img_width=193)
        elif name == "billing_selected": return tab_button_icon(icon=Image.open("./res/icons/tabs/billing_selected.png"),text="Billings",text_bg=Colors__.color()["navigation bar"]["fg"]["selected"],img_width=193)

        elif name == "proxies": return tab_button_icon(icon=Image.open("./res/icons/tabs/proxies.png"),text="Proxies",text_bg=Colors__.color()["navigation bar"]["fg"]["normal"],img_width=174)
        elif name == "proxies_hover": return tab_button_icon(icon=Image.open("./res/icons/tabs/proxies_hover.png"),text="Proxies",text_bg=Colors__.color()["navigation bar"]["fg"]["hover"],img_width=174)
        elif name == "proxies_selected": return tab_button_icon(icon=Image.open("./res/icons/tabs/proxies_selected.png"),text="Proxies",text_bg=Colors__.color()["navigation bar"]["fg"]["selected"],img_width=174)

        elif name == "capture": return tab_button_icon(icon=Image.open("./res/icons/tabs/capture.png"),text="Capture",text_bg=Colors__.color()["navigation bar"]["fg"]["normal"],img_width=184)
        elif name == "capture_hover": return tab_button_icon(icon=Image.open("./res/icons/tabs/capture_hover.png"),text="Capture",text_bg=Colors__.color()["navigation bar"]["fg"]["hover"],img_width=184)
        elif name == "capture_selected": return tab_button_icon(icon=Image.open("./res/icons/tabs/capture_selected.png"),text="Capture",text_bg=Colors__.color()["navigation bar"]["fg"]["selected"],img_width=184)

        elif name == "settings": return tab_button_icon(icon=Image.open("./res/icons/tabs/settings.png"),text="Settings",text_bg=Colors__.color()["navigation bar"]["fg"]["normal"],img_width=172)
        elif name == "settings_hover": return tab_button_icon(icon=Image.open("./res/icons/tabs/settings_hover.png"),text="Settings",text_bg=Colors__.color()["navigation bar"]["fg"]["hover"],img_width=172)
        elif name == "settings_selected": return tab_button_icon(icon=Image.open("./res/icons/tabs/settings_selected.png"),text="Settings",text_bg=Colors__.color()["navigation bar"]["fg"]["selected"],img_width=172)


        # Control
        elif name == "add_new": return ImageTk.PhotoImage(tab_button_icon(icon = Image.open("./res/icons/control/plus.png").resize((250,250),Image.LANCZOS), text = "CREATE TASK", text_bg  = "#cecfc6", img_width  = 200-45, img_original_height  =32, diff_icon_text  = 0, place_icon = "right",rounded=True,round_bg='#242437').resize((dimension if len(dimension) == 2 else (138, 32)), Image.LANCZOS))
        elif name == "add_new_hover": return ImageTk.PhotoImage(tab_button_icon(icon = Image.open("./res/icons/control/plus.png").resize((250,250),Image.LANCZOS), text = "CREATE TASK", text_bg  = "#e5e6dc", img_width  = 200-45, img_original_height  =32, diff_icon_text  = 0, place_icon = "right",rounded=True,round_bg='#242437').resize((dimension if len(dimension) == 2 else (138, 32)), Image.LANCZOS))

        elif name == "delete_all": return ImageTk.PhotoImage(tab_button_icon(icon = Image.open("./res/icons/control/delete.png").resize((270,270),Image.LANCZOS), text =   "DELETE  ALL", text_bg  = "#cecfc6", img_width  = 200-13-45, img_original_height  =32, diff_icon_text  = 0, place_icon = "right",rounded=True,round_bg='#242437').resize((dimension if len(dimension) == 2 else (129, 32)), Image.LANCZOS))
        elif name == "delete_all_hover": return ImageTk.PhotoImage(tab_button_icon(icon = Image.open("./res/icons/control/delete.png").resize((270,270),Image.LANCZOS), text =   "DELETE  ALL", text_bg  = "#e5e6dc", img_width  = 200-13-45, img_original_height  =32, diff_icon_text  = 0, place_icon = "right",rounded=True,round_bg='#242437').resize((dimension if len(dimension) == 2 else (129, 32)), Image.LANCZOS))

        elif name == "run_all": return ImageTk.PhotoImage(tab_button_icon(icon = Image.open("./res/icons/control/play.png").resize((250,250),Image.LANCZOS), text =   "START ALL", text_bg  = "#ffffff", img_width  = 200-13-38, img_original_height  =32, diff_icon_text  = 0, place_icon = "right",rounded=True,round_bg='#37cd8f').resize((dimension if len(dimension) == 2 else (114, 32)), Image.LANCZOS))
        elif name == "run_all_hover": return ImageTk.PhotoImage(tab_button_icon(icon = Image.open("./res/icons/control/play.png").resize((250,250),Image.LANCZOS), text =   "START ALL", text_bg  = "#e6e6e6", img_width  = 200-13-38, img_original_height  =32, diff_icon_text  = 0, place_icon = "right",rounded=True,round_bg='#37cd8f').resize((dimension if len(dimension) == 2 else (114, 32)), Image.LANCZOS))

        elif name == "stop_all": return ImageTk.PhotoImage(tab_button_icon(icon = Image.open("./res/icons/control/_stop.png").resize((280,300),Image.LANCZOS), text =   " STOP  ALL", text_bg  = "#ffffff", img_width  = 200-13-38, img_original_height  =32, diff_icon_text  = 0, place_icon = "right",rounded=True,round_bg='#f54e64').resize((dimension if len(dimension) == 2 else (114, 32)), Image.LANCZOS))
        elif name == "stop_all_hover": return ImageTk.PhotoImage(tab_button_icon(icon = Image.open("./res/icons/control/_stop.png").resize((280,300),Image.LANCZOS), text =   " STOP  ALL", text_bg  = "#e6e6e6", img_width  = 200-13-38, img_original_height  =32, diff_icon_text  = 0, place_icon = "right",rounded=True,round_bg='#f54e64').resize((dimension if len(dimension) == 2 else (114, 32)), Image.LANCZOS))

        elif name == "delete": return ImageTk.PhotoImage(Image.open("./res/icons/control/delete.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))
        elif name == "delete_hover": return ImageTk.PhotoImage(Image.open("./res/icons/control/delete_hover.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))



        elif name == "paush": return ImageTk.PhotoImage(Image.open("./res/icons/control/paush.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))
        elif name == "paush_hover": return ImageTk.PhotoImage(Image.open("./res/icons/control/paush_hover.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))

        elif name == "run": return ImageTk.PhotoImage(Image.open("./res/icons/control/run.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))
        elif name == "run_hover": return ImageTk.PhotoImage(Image.open("./res/icons/control/run_hover.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))

        elif name == "edit": return ImageTk.PhotoImage(Image.open("./res/icons/control/edit.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))
        elif name == "edit_hover": return ImageTk.PhotoImage(Image.open("./res/icons/control/edit_hover.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))

        elif name == "stop": return ImageTk.PhotoImage(Image.open("./res/icons/control/stop.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))
        elif name == "stop_hover": return ImageTk.PhotoImage(Image.open("./res/icons/control/stop_hover.png").resize((dimension if len(dimension) == 2 else (32, 32)), Image.LANCZOS))


        #Select Box
        elif name == "select_box": return ImageTk.PhotoImage(Image.open("./res/icons/select_box.png").resize((dimension if len(dimension) == 2 else (24, 24)), Image.LANCZOS))
        elif name == "select_box_hover": return ImageTk.PhotoImage(Image.open("./res/icons/select_box_hover.png").resize((dimension if len(dimension) == 2 else (24, 24)), Image.LANCZOS))

        elif name == "select_box_selected": return ImageTk.PhotoImage(Image.open("./res/icons/select_box_selected.png").resize((dimension if len(dimension) == 2 else (24, 24)), Image.LANCZOS))
        elif name == "select_box_selected_hover": return ImageTk.PhotoImage(Image.open("./res/icons/select_box_selected_hover.png").resize((dimension if len(dimension) == 2 else (24, 24)), Image.LANCZOS))


        # Save
        elif name == "save": return ImageTk.PhotoImage(Image.open("./res/icons/save.png").resize((dimension if len(dimension) == 2 else (107, 35)), Image.LANCZOS))
        elif name == "save_hover": return ImageTk.PhotoImage(Image.open("./res/icons/save_hover.png").resize((dimension if len(dimension) == 2 else (107, 35)), Image.LANCZOS))

        ## Save
        elif name == "activate": return ImageTk.PhotoImage(activation_btn_img(bg="normal").resize((dimension if len(dimension) == 2 else (384, 32)), Image.LANCZOS))
        elif name == "activate_hover": return ImageTk.PhotoImage(activation_btn_img(bg="hover").resize((dimension if len(dimension) == 2 else (384, 32)), Image.LANCZOS))









