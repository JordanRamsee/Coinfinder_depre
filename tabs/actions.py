# from addnewtask import *
from addnewtask import AddNewTask





# Task Tab
def task_tab_action_add_new_data_to_DB(task_data: dict):
    '''
    This method to add new task data to the database.
    '''
    print(f"Task Tab , Task ID {task_data['ID']} New task add to DB")


def task_tab_action_start(task_data: dict):
    '''
    This function handles the action performed when the start/run
    button for an individual task in the task tab is pressed.
    '''
    print(f"Task Tab , Task ID {task_data['ID']} Started")

def task_tab_action_terminate(task_data: dict):
    '''
    This function manages the action  taken  when  the  terminate
    button for an individual task in the task tab is pressed.
    '''
    print(f"Task Tab , Task ID {task_data['ID']} Terminated")

def task_tab_action_edit(task_data: dict, column_data: dict):
    '''
    This  function  is  responsible  for  handling   the   action
    triggered when the edit button for an individual task in  the
    task   tab   is   pressed.   Simply   update   the  value  of
    'column_data[each_key]['label']['text']' to display it in the
    interface.
    '''
    print(f"Task Tab , Task ID {task_data['ID']} Edit")
    for each_key in list(column_data.keys())[1:-1]:
        column_data[each_key]["label"]["text"] = each_key + "777"
    print(f"Task Tab , Task ID {task_data['ID']} Edited")

def task_tab_action_delete(task_data: dict):
    '''
    This function oversees the action executed  when  the  delete
    button for an individual task in the task tab is pressed.
    '''
    print(f"Task Tab , Task ID {task_data['ID']} Deleted")

def task_tab_action_add_new_task(root_window,data_show_frame,tab_property):
    # Need to provide task_id by default 101
    AddNewTask(root_window,data_show_frame,tab_property,new_task_id='101')



# Billing Tab
def billing_tab_action_delete(task_data: dict):
    '''
    This function oversees the action executed  when  the  delete
    button for an individual biller in the billing tab is pressed.
    '''
    print(f"Billing Tab , Billing ID {task_data['ID']} Deleted")

def billing_tab_action_edit(task_data: dict,column_data:dict):
    '''
    This  function  is  responsible  for  handling   the   action
    triggered when the edit button for an individual biller in the
    billing   tab   is   pressed.  Simply   update  the  value of
    'column_data[each_key]['label']['text']' to display it in the
    interface.
    '''
    print(f"Billing Tab , Task ID {task_data['ID']} Edit")
    for each_key in list(column_data.keys())[1:-1]:
        column_data[each_key]["label"]["text"] = each_key+"555"
    print(f"Billing Tab , Task ID {task_data['ID']} Edited")

