########################
##  IMPORT LIBRARIES  ##
########################

import string
import random
import names


class generator:
    def __init__(self, name=None, surname=None, mail=None, pwd=None):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.pwd = pwd

    def __del__(self):
        print("Generation ended.")

    def random(self):

        characters = list(string.ascii_letters +
                          string.digits + "!@#$%^&*()")
        length = 12
        random.shuffle(characters)
        password = []
        for i in range(length):
            password.append(random.choice(characters))
        random.shuffle(password)

        self.pwd = "".join(password)
        self.name = names.get_first_name()
        self.surname = names.get_last_name()
        self.mail = self.name.lower()+"."+self.surname.lower() + \
            "."+str(random.randint(0, 99999))
        return self
