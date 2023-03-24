from kivy.core.window import Window
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen

from ObjectHandler import Configurations
from ApplicationHandler import Account

UI = Configurations.UI
SETTINGS = Configurations.SETTINGS

Window.size = 1280, 720

"""
=====================================================================
|| WARNING: THIS PROGRAM IS NOT MEANT TO ACTUALLY SECURE PASSWORDS ||
=====================================================================
The features of this program include:
    - Adding usernames/passwords for specific applications/websites
    - Removing usernames/passwords for specific apps/sites
    - Changing usernames/passwords for specific apps/sites
    - Importing text files of usernames/passwords to be encrypted. 
        - FORMAT: app/website,username,password
    - Exporting encrypted files. 
    
All usernames and passwords are stored encrypted. 
Everytime they are accessed they will be decrypted.
This program will be ran through a GUI. 
"""

class LoginWindow(MDScreen):
    def validateLogin(self, username, password):
        if username == Configurations.USERNAME and password == Configurations.PASSWORD: 
            return True
        else: 
            return False
        
class HomeWindow(MDScreen):
    pass

class WindowManager(MDScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.title = "Password Protector"
        self.kv = Builder.load_file(UI)
        return self.kv
    
    def validateData(*values):
        for value in values:
            if value == "" and values.index(value) != 0:
                return "False"
            else:
                pass
        return "True"
        
    ## ACCOUNTS ##
    def createAccount(self, app, name, email, pw):
        self.account = Account(app, name, email, pw).createAccount()
        return "True"

    

MainApp().run()