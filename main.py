from os import remove
from cryptography.fernet import Fernet
import tkinter as tk
import linecache as lc

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
key = Fernet.generate_key()
fernet = Fernet(key)

#window = tk.Tk()
def replaceLine(fileName, lineNum, text):
    lines = open(fileName, 'r').readlines()
    lines[lineNum] = text
    out = open(fileName, 'w')
    out.writelines(lines)
    out.close()

def encodeData(password):
    tempEncoded = fernet.encrypt(password.encode())
    print("Encoded!")
    return tempEncoded

def decodeData(password):
    tempDecoded = fernet.encrypt(password.decode())
    print("Decoded!")
    return tempDecoded

def addData():
    with open('ENCODED_USERNAMES_PASSWORDS.txt', mode = "a+") as file:
        tempData = input("Input in this format! APPLICATION/WEBSITE,USERNAME,PASSWORD, be sure to include the commas! ")   
        file.seek(0)
        data = file.read(100)
        if len(data) > 0 :
            file.write("\n") 
        tempList = tempData.split(",")
        tempEncoded = encodeData(tempList[2])
        tempStr = tempList[0] + ',' + tempList[1] + ',' + str(tempEncoded)
        file.writelines(tempStr)
    file.close

def changeData():
    with open('ENCODED_USERNAMES_PASSWORDS.txt', mode = "r+") as file:
        print("WIP")
        tempMatch = []
        tempUsers = [] 
        tempDict = {}
        app = input("Input the APPLICATION/WEBSITE you wish to edit. ")
        for num,line in enumerate(file,1):
            temp = line.split(",")
            if temp[0] != app:
                continue
            else:
                print("Match")
                tempMatch.append(num)
        if len(tempMatch) >> 1:
            for i in tempMatch:
                tempString = lc.getline(r"ENCODED_USERNAMES_PASSWORDS.txt", i)
                temp = tempString.split(",")
                tempUsers.append(temp[1])
                tempDict.update({temp[1]:i})
            usernameSelect = input("Which username would you like to remove? " + str(tempUsers))
            for i in tempUsers:
                if i != usernameSelect:
                    continue
                else:
                    lineNum = tempDict.get(i)
                    #need to work in changing the contents of the line instead of just deleting it. 
                    #replaceLine("ENCODED_USERNAMES_PASSWORDS.txt",lineNum - 1,"")
        else:
            confirmation = input("Are you sure you want to delete this data? (Y/N) ")
            if confirmation == "Y" or confirmation == "y":
                #replaceLine("ENCODED_USERNAMES_PASSWORDS.txt",tempMatch[0] - 1,"")

def removeData():
    with open('ENCODED_USERNAMES_PASSWORDS.txt', mode = "r+") as file:
        tempMatch = []
        tempUsers = [] 
        tempDict = {}
        app = input("Input the APPLICATION/WEBSITE you wish to remove. ")
        for num,line in enumerate(file,1):
            temp = line.split(",")
            if temp[0] != app:
                continue
            else:
                print("Match")
                tempMatch.append(num)
        if len(tempMatch) >> 1:
            for i in tempMatch:
                tempString = lc.getline(r"ENCODED_USERNAMES_PASSWORDS.txt", i)
                temp = tempString.split(",")
                tempUsers.append(temp[1])
                tempDict.update({temp[1]:i})
            usernameSelect = input("Which username would you like to remove? " + str(tempUsers))
            for i in tempUsers:
                if i != usernameSelect:
                    continue
                else:
                    lineNum = tempDict.get(i)
                    replaceLine("ENCODED_USERNAMES_PASSWORDS.txt",lineNum - 1,"")
        else:
            confirmation = input("Are you sure you want to delete this data? (Y/N) ")
            if confirmation == "Y" or confirmation == "y":
                replaceLine("ENCODED_USERNAMES_PASSWORDS.txt",tempMatch[0] - 1,"")
    
def importData():
    fileName = input("Type in the text file path: (ex: user/home/desktop/somefile.txt) ")
    print(fileName)
    with open('USERNAMES_PASSWORDS.txt') as file:
        with open("ENCODED_USERNAMES_PASSWORDS.txt", mode = "r+") as file2:
            for line in file:
                temp = line.split(",")
                tempEncoded = encodeData(temp[1])
                tempStr = temp[0] + "," + temp[1] + "," + str(tempEncoded) + "\n"
                file2.writelines(tempStr)
        file2.close
    file.close

def exportData():
    print("WIP")
