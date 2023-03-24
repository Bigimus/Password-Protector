import StorageHandler as SH
from ObjectHandler import Configurations as Config

SETTINGS = Config.SETTINGS
ACCOUNTS = Config.ACCOUNTS

class Account:
    def __init__(self, app_name, app_username, app_email, app_password) -> None:
        self.app_name = app_name
        self.app_username = app_username
        self.app_email = app_email
        self.app_password = app_password
    
    def createAccount(self):
        data = dict(SH.readJson(ACCOUNTS))
        if self.app_name in data:
            if self.app_email not in data[self.app_name]:
                data[self.app_name].update({
                    self.app_email: {
                        "username": self.app_username,
                        "password": self.app_password
                    }
                })
            else:
                raise KeyError
        else:
            data.update({
                self.app_name: {
                    self.app_email: {
                        "username": self.app_username,
                        "password": self.app_password
                    }
                }
            })
        
        SH.writeJson(ACCOUNTS, data)


        
        
        
