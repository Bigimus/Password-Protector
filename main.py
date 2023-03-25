from kivy.core.window import Window
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen

from ObjectHandler import Configurations as Config
from ObjectHandler import Account
from ObjectHandler import Settings

import StorageHandler as SH

UI = Config.UI
SETTINGS = Config.SETTINGS
APPLICATION = Config.ACCOUNTS

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
This program will be ran through a GUI
"""

class LoginWindow(MDScreen):
    def validateLogin(self, username, password):
        if username == Settings().root_username and password == Settings().root_password:   # noqa: E501
            return "True"
        else: 
            return "False"
        
class HomeWindow(MDScreen):
    pass

class WindowManager(MDScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.title = "Password Protector"
        self.kv = Builder.load_file(UI)
        self.theme_cls.theme_style = "Dark"
        self.loadSettings()
        self.searchApplication("Steam")
        return self.kv
    
    def validateData(*args):
        for arg in args:
            if arg == "" and args.index(arg) != 0:
                return False
            else:
                pass
        return True
     
    ## ACCOUNTS ##
    def createAccount(self, app, name, email, pw):
        if self.validateData(app, name, email, pw) is True:
            self.account = Account(app, name, email, pw).createAccount()
            return True
        else:
            return False

    def searchApplication(self, application):
        pass

    def searchEmail(self, application, email):
        pass

    ## SETTINGS ##
    def saveSettings(self, root_username, root_password):
        if self.validateData(root_username, root_password) is True:
            self.settings = Settings(root_username, root_password).saveSettings()
            return True
        else:
            return False

    def loadSettings(self):
        data = SH.readJson(SETTINGS)
        self.root_username = data["root_username"]
        self.root_password = data["root_password"]

    


MainApp().run()