import win32com.client

class FirewallManager:
    def __init__(self):
        self.fwMgr = win32com.client.Dispatch("HNetCfg.FwMgr")
        self.fwProfile = self.fwMgr.LocalPolicy.CurrentProfile
    
    def list_rules(self):
        rules = self.fwProfile.Rules()
        for rule in rules:
            print(rule.Name)
    
    def add_rule(self, rule_name, application_path):
        new_rule = win32com.client.Dispatch("HNetCfg.FWRule")
        new_rule.Name = rule_name
        new_rule.ApplicationName = application_path
        new_rule.Action = 1  # Allow
        new_rule.Direction = 1  # Inbound
        new_rule.Enabled = True
        new_rule.InterfaceTypes = "All"
        self.fwProfile.Rules().Add(new_rule)
    
    def delete_rule(self, rule_name):
        rules = self.fwProfile.Rules()
        for rule in rules:
            if rule.Name == rule_name:
                rules.Remove(rule)
                break

fw_manager = FirewallManager()