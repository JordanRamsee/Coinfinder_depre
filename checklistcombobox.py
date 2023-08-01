import tkinter as tk


class CheckListComboBox(tk.Menubutton):
    """A combobox widget with checkboxes"""

    def __init__(self, master, text, values, **kwargs):
        """Create a CheckListComboBox widget

        Args:
            master: the parent widget
            text: the text of the button
            values: a list of tuples (label, variable) for the checkboxes
            kwargs: additional options for the Menubutton widget
        """
        # initialize the Menubutton widget
        super().__init__(master, text=text, relief=tk.RAISED, **kwargs)

        # create a Menu widget and set it as the menu option
        self.menu = tk.Menu(self, tearoff=0 )
        
        
        self["menu"] = self.menu

        self.values = values

        # create the checkboxes and store them in a list
        self.checkboxes = []
        for label, variable in values:
            checkbox = self.menu.add_checkbutton(label=label, variable=variable , command=lambda:self.rerender())
            self.checkboxes.append(checkbox)

    def get_values(self):
        """Return a list of values of the checkboxes"""
        return [var.get() for _, var in self.values]
    
    def rerender(self):
        self.menu.post(self.winfo_rootx(), self.winfo_rooty() + self.winfo_height())

    def get(self):
        result = ""
        for value in self.values:
            if value[1].get() > 0:
                result += value[0] + ", "
        try:
            result.removesuffix(", ")
        except :
            pass

        return result

    def bind_command(self, index, command):
        """Bind a function to handle the changes of a checkbox

        Args:
            index: the index of the checkbox in the values list
            command: the function to execute when the checkbox changes
        """
        # get the label and variable of the checkbox
        label, variable = self.values[index]

        # configure the command option of the checkbox
        self.menu.entryconfig(index, command=command)

    def update_text(self):
        self.menu.post(self.winfo_rootx(), self.winfo_rooty() + self.winfo_height())

        self["text"] = self.get()    

    def post_menu(self):
        """Store the current values of the checkboxes before showing the menu"""
        self.prev_values = self.get_values()

    def unpost_menu(self, event=None):
        """Compare the current values with the previous values and call update_text if there is any change"""
        curr_values = self.get_values()
        if curr_values != self.prev_values:
            self.update_text()
        