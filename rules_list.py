import tkinter as tk
from firewall_manager import fw_manager

class RulesList(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
        self.rules_list = tk.Listbox(self)
        self.rules_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.add_button = tk.Button(self, text="Add Rule", command=self.add_rule_button_clicked)
        self.add_button.pack(side=tk.RIGHT)
        
        self.refresh_button = tk.Button(self, text="Refresh", command=self.refresh_button_clicked)
        self.refresh_button.pack(side=tk.RIGHT)
        
    def refresh_button_clicked(self):
        self.refresh()
    
    def add_rule_button_clicked(self):
        # Some code to open a dialog or window for rule creation
        # and handle the user input for adding a new firewall rule
        pass
    
    def refresh(self):
        self.rules_list.delete(0, tk.END)
        rules = fw_manager.list_rules()
        
        for rule in rules:
            self.rules_list.insert(tk.END, rule.Name)