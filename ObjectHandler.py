from dataclasses import dataclass
from cryptography.fernet import Fernet

import StorageHandler as SH

@dataclass
class Configurations:
    ## FILES $$
    SETTINGS:str = "Configs/Settings.json"
    UI:str = "Configs/UI.kv"
    ACCOUNTS:str = "Configs/Applications.json"
    
    ## IMAGES ##
    LOGIN_BACKGROUND:str = "Images/Login_Background.jpg"

class Security:
    def __init__(self, key):
        self.fernet = Fernet(key)

    def encryptData(self, data:str):
        temp_encrypted = self.fernet.encrypt(data.encode('utf-8')).decode()
        return temp_encrypted
    
    def decryptData(self, data:str):
        temp_decrypted = self.fernet.decrypt(data).decode()
        return temp_decrypted
    
class Account:

    def __init__(self, app_name, app_email, app_username, app_password) -> None:
        self.fernet = Security("PNC7uPvO_CBBXdgNjQrUaG3L9iBaIlF9O2HXPlRlwco=")
        self.app_name = app_name
        self.app_email = app_email
        self.app_username = app_username
        self.app_password = app_password
    
    def createAccount(self):
        data = dict(SH.readJson(Configurations.ACCOUNTS))
        if self.app_name in data:
            if self.app_email not in data[self.app_name]:
                data[self.app_name].update({
                    self.app_email: {
                        "username": self.app_username,
                        "password": self.fernet.encryptData(self.app_password).decode()
                    }
                })
            else:
                raise KeyError
        else:
            data.update({
                self.app_name: {
                    self.app_email: {
                        "username": self.app_username,
                        "password": self.fernet.encryptData(self.app_password).decode()
                    }
                }
            })
        
        SH.writeJson(Configurations.ACCOUNTS, data)
    
    def editAccount(self):
        data = SH.readJson(Configurations.ACCOUNTS)
        if self.app_name in data:
            if self.app_email in data[self.app_name]:
                data[self.app_name][self.app_email]["username"] = self.app_username
                data[self.app_name][self.app_email]["password"] = self.fernet.encryptData(self.app_password)  # noqa: E501
                SH.writeJson(Configurations.ACCOUNTS, data)
            else:
                raise KeyError
        else:
            raise KeyError
    
    def deleteAccount(self):
        data = SH.readJson(Configurations.ACCOUNTS)
        if self.app_name in data:

            if len(data[self.app_name]) == 1:
                del data[self.app_name]
                SH.writeJson(Configurations.ACCOUNTS, data)
    
            elif self.app_email in data[self.app_name]:
                del data[self.app_name][self.app_email]
                SH.writeJson(Configurations.ACCOUNTS, data)

            else:
                raise KeyError
        else:
            raise KeyError


class Settings:
    data = SH.readJson(Configurations.SETTINGS)
    fernet = Security("PNC7uPvO_CBBXdgNjQrUaG3L9iBaIlF9O2HXPlRlwco=")
    def __init__(
            self, 
            root_username = data["root_username"], 
            root_password = fernet.decryptData(data["root_password"])
        ) -> None:
        
        self.fernet = Security("PNC7uPvO_CBBXdgNjQrUaG3L9iBaIlF9O2HXPlRlwco=")
        self.root_username:str = root_username
        self.root_password:str = root_password
    
    def saveSettings(self):
        data = SH.readJson(Configurations.SETTINGS)
        data["root_username"] = self.root_username
        data["root_password"] = str(self.fernet.encryptData(self.root_password))
        SH.writeJson(Configurations.SETTINGS, data)


