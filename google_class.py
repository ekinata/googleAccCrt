########################
##  IMPORT LIBRARIES  ##
########################

import pyautogui as p
import time as t
import os

######################
##  DEFINE CLASSES  ##
######################


class google:
    def __init__(self, name=None, surname=None, mail=None, pwd=None):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.pwd = pwd

    def __del__(self):
        print("Google class cleared.")

    def CreateAccount(self, user):
        cmd = "\"C:\Program Files\Google\Chrome\Application\chrome.exe\" -incognito https://accounts.google.com/signup"
        os.system(cmd)
        t.sleep(2)
        p.write(user.name, 0.05)
        p.press('tab')
        p.write(user.surname, 0.05)
        p.press('tab')
        p.write(user.mail, 0.05)
        p.press('tab')
        p.press('tab')
        p.write(user.pwd, 0.05)
        p.press('tab')
        p.write(user.pwd, 0.05)
        p.press('enter')
