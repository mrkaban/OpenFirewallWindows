from firewall_manager import FirewallManager
from rules_list import RulesList
import tkinter as tk

class GUIElement:
    def __init__(self):
        self.firewall_manager = FirewallManager()

    def refresh_button_clicked(self):
        # Обработчик события нажатия кнопки "Refresh"
        self.rules_list.refresh()
    
    def add_rule_button_clicked(self):
        # Обработчик события нажатия кнопки "Add Rule"
        rule_name = self.rule_name_entry.get()
        application_path = self.app_path_entry.get()
        if rule_name and application_path:
            self.firewall_manager.add_rule(rule_name, application_path)
            self.rules_list.refresh()

    def create_gui(self):
        root = tk.Tk()
        
        # Создание элементов интерфейса
        refresh_button = tk.Button(root, text="Refresh", command=self.refresh_button_clicked)
        rule_name_label = tk.Label(root, text="Rule Name:")
        self.rule_name_entry = tk.Entry(root)
        app_path_label = tk.Label(root, text="Application Path:")
        self.app_path_entry = tk.Entry(root)
        add_rule_button = tk.Button(root, text="Add Rule", command=self.add_rule_button_clicked)
        
        # Расположение элементов на форме
        refresh_button.pack()
        rule_name_label.pack()
        self.rule_name_entry.pack()
        app_path_label.pack()
        self.app_path_entry.pack()
        add_rule_button.pack()
        
        self.rules_list = RulesList(root)
        self.rules_list.pack()
        
        root.mainloop()

# Создание экземпляра класса GUIElement и запуск GUI
gui_element = GUIElement()
gui_element.create_gui()