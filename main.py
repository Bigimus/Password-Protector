from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen 
from kivymd.uix.menu import MDDropdownMenu

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
    
class SearchWindow(MDScreen):
    def openAppMenu(self):
        data = SH.readJson(APPLICATION)
        apps = [
            {
            "text": f"{app}",
            "viewclass": "OneLineListItem",
            "on_release": lambda x = f"{app}":  self.setApp(x)
            } for app in data
        ]
        self.app_menu = MDDropdownMenu(
            caller = self.ids.search_app,
            items = apps,
            width_mult = 4,
            position = "bottom",
            max_height = dp(224)
        )
        
        self.app_menu.open()
    
    def setApp(self, app):
        self.ids.search_app.text = app
        self.app_menu.dismiss()
        self.openEmailMenu(app)

    def openEmailMenu(self, app):
        data = SH.readJson(APPLICATION)
        emails = [
            {
            "text": f"{email}",
            "viewclass": "OneLineListItem",
            "on_release": lambda x = f"{email}":  self.setEmail(x, app)
            } for email in data[app]
        ]
        self.email_menu = MDDropdownMenu(
            caller = self.ids.search_email,
            items = emails,
            width_mult = 4,
            position = "bottom",
            max_height = dp(200)
        )
        self.email_menu.open()
    
    def setEmail(self, email, app):
        self.ids.search_email.text = email
        self.email_menu.dismiss()
        self.searchAccount(app, email)
    
    def searchAccount(self, app, email):
        data = SH.readJson(APPLICATION)
        data = data[app][email]
        self.ids.account_username.text = data["username"]
        self.ids.account_password.text = data["password"]
        
class CreateWindow(MDScreen):
    def createAccount(self, app, email, username, password):
        self.account = Account(app, email, username, password).createAccount()
        self.ids.account_app.text = ""
        self.ids.account_email.text = ""
        self.ids.account_username.text = ""
        self.ids.account_password.text = ""

class SettingsWindow(MDScreen):
    def saveSettings(self, root_username, root_password):
        self.settings = Settings(
            root_username, 
            root_password
        ).saveSettings()

class DeleteWindow(SearchWindow):
    def deleteAccount(self, app, email, username, password):
        self.account = Account(app, email, username, password).deleteAccount()
        self.ids.search_app.text = ""
        self.ids.search_email.text = ""
        self.ids.account_username.text = ""
        self.ids.account_password.text = ""

class EditWindow(SearchWindow):
    def saveAccount(self, app, email, username, password):
        self.account = Account(app, email, username, password).editAccount()
        self.ids.search_app.text = ""
        self.ids.search_email.text = ""
        self.ids.account_username.text = ""
        self.ids.account_password.text = ""

class WindowManager(MDScreenManager):
    pass

class MainApp(MDApp):
    data = SH.readJson(SETTINGS)
    root_username = data["root_username"]
    root_password = data["root_password"]
    
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.title = "Password Protector"
        self.theme_cls.theme_style = "Dark"
        self.kv = Builder.load_file(UI)
        self.loadSettings() 
        return self.kv
    
    def validateData(*args):
        for arg in args:
            if arg == "" and args.index(arg) != 0:
                return False
            else:
                pass
        return True

    def loadSettings(self):
        data = SH.readJson(SETTINGS)
        global root_username, root_password
        root_username = data["root_username"]
        root_password = data["root_password"]

MainApp().run()