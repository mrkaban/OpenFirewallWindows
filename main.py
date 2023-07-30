from tkinter import Tk, Button
from firewall_manager import FirewallManager
from gui_elements import GUIElement
from rules_list import RulesList

class OpenSafeWallApp:
    def __init__(self):
        self.window = Tk()
        self.window.title("OpenSafeWall")
        
        self.gui_element = GUIElement()
        self.firewall_manager = FirewallManager()
        
        self.rules_list = RulesList(self.window)
        self.rules_list.pack()
        
        self.refresh_button = Button(self.window, text="Refresh", command=self.refresh_rules)
        self.refresh_button.pack()
        
        self.add_rule_button = Button(self.window, text="Add Rule", command=self.add_rule)
        self.add_rule_button.pack()
        
        self.window.mainloop()
    
    def refresh_rules(self):
        self.rules_list.refresh()
    
    def add_rule(self):
        self.gui_element.add_rule_button_clicked()
        self.refresh_rules()
    
if __name__ == '__main__':
    app = OpenSafeWallApp()