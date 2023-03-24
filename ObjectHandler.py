from dataclasses import dataclass

@dataclass
class Configurations:
    
    ## USERS ##
    USERNAME:str = "Bigimus"
    PASSWORD:str = "test"
    PIN:str = "1021"
    
    ## FILES $$
    SETTINGS:str = "Configs/Settings.json"
    UI:str = "Configs/UI.kv"
    ACCOUNTS:str = "Configs/Applications.json"
    
    ## IMAGES ##
    LOGIN_BACKGROUND:str = "Images/Login_Background.jpg"