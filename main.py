########################
##  IMPORT LIBRARIES  ##
########################

from amazon_class import amazon
from generator import generator
from google_class import google

################
##  MAIN JOB  ##
################

Generate = generator()
Amazon = amazon()
Google = google()

user = Generate.random()

print("Name: "+user.name+"\nSurname: "+user.surname +
      "\nMail: "+user.mail+"\nPass: "+user.pwd)

Google.CreateAccount(user)
