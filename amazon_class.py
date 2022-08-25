########################
##  IMPORT LIBRARIES  ##
########################

import pyautogui as p
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time as t

######################
##  DEFINE CLASSES  ##
######################


class amazon:
    def __init__(self, name=None, surname=None, mail=None, pwd=None):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.pwd = pwd

    def __del__(self):
        print("Amazon class cleared.")

    def CreateAccount(self):
        print("Hello my name is " + self.name)
