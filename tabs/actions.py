# from addnewtask import *
import pickle
from addnewtask import AddNewTask
from addnewbilling import AddNewBilling
from addnewproxy import AddNewProxy
from addnewcapture import AddNewCapture
from encryption import decrypt , encrypt

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

    
    
    
def delete_all(list_of_tasks):
    for task in list_of_tasks:
        task_tab_action_delete(task)
    

def task_tab_action_delete(task_data: dict):
    '''
    This function oversees the action executed  when  the  delete
    button for an individual task in the task tab is pressed.
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
        if task.task_id == task_data['ID']:
            tasks.remove(task)
        else:
            pass
    
    with open('tasksfile.txt', 'wb') as fp:
        data = pickle.dumps(tasks)
        encrypted_data = encrypt(data)
        fp.write(encrypted_data)
        print('Done writing list into a binary file')



    print(f"Task Tab , Task ID {task_data['ID']} Deleted")



def task_tab_action_edit(task_data: dict, column_data: dict , root_window,data_show_frame,tab_property):
    '''
    This  function  is  responsible  for  handling   the   action
    triggered when the edit button for an individual task in  the
    task   tab   is   pressed.   Simply   update   the  value  of
    'column_data[each_key]['label']['text']' to display it in the
    interface.
    '''
    print(f"Task Tab , Task ID {task_data['ID']} Edit")
    print('=======================')
    for each_key in list(column_data.keys())[1:-1]:
        # column_data[each_key]["label"]["text"] = each_key + "777"
        print(each_key)
    # print(task_data)
    print('=======================')
    print(f"Task Tab , Task ID {task_data['ID']} Edited")
    AddNewTask(root_window,data_show_frame,tab_property,new_task_id='101' ,  edit = True , task_id = task_data['ID'] , edited_column = column_data )
    



def task_tab_action_add_new_task(root_window,data_show_frame,tab_property  ):
    # Need to provide task_id by default 101
    # for each_key in list(column_data.keys())[1:-1]:
        # column_data[each_key]["label"]["text"] = each_key + "777"
        # print(each_key)
    AddNewTask(root_window,data_show_frame,tab_property,new_task_id='101' )



# Billing Tab
def billing_tab_action_delete(task_data: dict):
    '''
    This function oversees the action executed  when  the  delete
    button for an individual biller in the billing tab is pressed.
    '''

    billings = []
    try:
        # for reading also binary mode is important
        with open('billingsfile.txt', 'rb') as fp:
            data = fp.read()
            decrypted_data = decrypt(data)
            n_list = pickle.loads(decrypted_data)
            # n_list = pickle.load(fp)
            billings = n_list
    except:
        billings = []

    for billing in billings:
        if billing.key_id == task_data['ID']:
            billings.remove(billing)
        else:
            pass
    
    with open('billingsfile.txt', 'wb') as fp:
        data = pickle.dumps(billings)
        encrypted_data = encrypt(data)
        fp.write(encrypted_data)
        print('Done writing list into a binary file')

    print(f"Billing Tab , Billing ID {task_data['ID']} Deleted")

def billing_tab_action_edit(task_data: dict,column_data:dict , root_window,data_show_frame,tab_property):
    '''
    This  function  is  responsible  for  handling   the   action
    triggered when the edit button for an individual biller in the
    billing   tab   is   pressed.  Simply   update  the  value of
    'column_data[each_key]['label']['text']' to display it in the
    interface.
    '''
    # print(f"Billing Tab , Task ID {task_data['ID']} Edit")
    # for each_key in list(column_data.keys())[1:-1]:
    #     column_data[each_key]["label"]["text"] = each_key+"555"
    # print(f"Billing Tab , Task ID {task_data['ID']} Edited")
    AddNewBilling(root_window,data_show_frame,tab_property,new_billing_id='101' , edit = True , task_id = task_data['ID'] , edited_column = column_data)

def billing_tab_action_add_new_billing(root_window,data_show_frame,tab_property):
        # Need to provide billing_id by default 101
    AddNewBilling(root_window,data_show_frame,tab_property,new_billing_id='101')


# Proxies Tab

def proxies_tab_action_add_new_data_to_DB(proxy_data: dict):
    '''
    This method to add new proxy data to the database.
    '''
    print(f"Proxies Tab , Proxy ID {proxy_data['ID']} New proxy add to DB")

def proxies_tab_action_start(proxy_data: dict):
    '''
    This function handles the action performed when the start/run
    button for an individual proxy in the proxy tab is pressed.
    '''
    print(f"Proxies Tab , Proxy ID {proxy_data['ID']} Started")

def proxies_tab_action_terminate(proxy_data: dict):
    '''
    This function manages the action  taken  when  the  terminate
    button for an individual proxy in the proxy tab is pressed.
    '''
    print(f"Proxies Tab , Proxy ID {proxy_data['ID']} Terminated")

def proxies_tab_action_edit(proxy_data: dict, column_data: dict , root_window,data_show_frame,tab_property):
    '''
    This  function  is  responsible  for  handling   the   action
    triggered when the edit button for an individual proxy in  the
    proxy   tab   is   pressed.   Simply   update   the  value  of
    'column_data[each_key]['label']['text']' to display it in the
    interface.
    '''
    # print(f"Proxies Tab , Proxy ID {proxy_data['ID']} Edit")
    # for each_key in list(column_data.keys())[1:-1]:
    #     column_data[each_key]["label"]["text"] = each_key + "777"
    # print(f"Proxies Tab , Proxy ID {proxy_data['ID']} Edited")
    AddNewProxy(root_window,data_show_frame,tab_property,new_proxy_id='101' , edit = True , task_id = proxy_data['ID'] , edited_column = column_data)

def proxies_tab_action_delete(proxy_data: dict):
    '''
    This function oversees the action executed  when  the  delete
    button for an individual proxy in the proxy tab is pressed.
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
        if proxy.proxy_id == proxy_data['ID']:
            proxies.remove(proxy)
        else:
            pass
    print(proxies)
    with open('proxiesfile.txt', 'wb') as fp:
        pickle.dump(proxies, fp)
        print('Done writing list into a binary file')


    print(f"Proxies Tab , Proxy ID {proxy_data['ID']} Deleted")

def proxies_tab_action_add_new_proxy(root_window,data_show_frame,tab_property):
    # Need to provide proxy_id by default 101
    AddNewProxy(root_window,data_show_frame,tab_property,new_proxy_id='101')


# Captures Tab

def captures_tab_action_add_new_data_to_DB(capture_data: dict):
    '''
    This method to add new capture data to the database.
    '''
    print(f"Captures Tab , Capture ID {capture_data['ID']} New capture add to DB")

def captures_tab_action_start(capture_data: dict):
    '''
    This function handles the action performed when the start/run
    button for an individual proxy in the proxy tab is pressed.
    '''
    print(f"Captures Tab , Capture ID {capture_data['ID']} Started")

def captures_tab_action_terminate(capture_data: dict):
    '''
    This function manages the action  taken  when  the  terminate
    button for an individual proxy in the proxy tab is pressed.
    '''
    print(f"Captures Tab , Capture ID {capture_data['ID']} Terminated")

def captures_tab_action_edit(capture_data: dict, column_data: dict):
    '''
    This  function  is  responsible  for  handling   the   action
    triggered when the edit button for an individual proxy in  the
    proxy   tab   is   pressed.   Simply   update   the  value  of
    'column_data[each_key]['label']['text']' to display it in the
    interface.
    '''
    print(f"Captures Tab , Capture ID {capture_data['ID']} Edit")
    for each_key in list(column_data.keys())[1:-1]:
        column_data[each_key]["label"]["text"] = each_key + "777"
    print(f"Captures Tab , Capture ID {capture_data['ID']} Edited")


def captures_tab_action_delete(capture_data: dict):
    '''
    This function oversees the action executed  when  the  delete
    button for an individual proxy in the proxy tab is pressed.
    '''  
    captures = []
    try:
        # for reading also binary mode is important
        with open('capturesfile.txt', 'rb') as fp:
            n_list = pickle.load(fp)
            captures = n_list
    except:
        captures = []

    for capture in captures:
        if capture.capture_id == capture_data['ID']:
            captures.remove(capture)
        else:
            pass
    
    with open('capturesfile.txt', 'wb') as fp:
        pickle.dump(captures, fp)
        print('Done writing list into a binary file')

    print(f"Captures Tab , Capture ID {capture_data['ID']} Deleted")

def captures_tab_action_add_new_capture(root_window,data_show_frame,tab_property):
        # Need to provide task_id by default 101
    AddNewCapture(root_window,data_show_frame,tab_property,new_capture_id='101')
    
    