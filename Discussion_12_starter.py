import requests
from bs4 import BeautifulSoup
import sqlite3
import os
import matplotlib.pyplot as plt

# Don't change anything in this function
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

# Create a function called grab_data
# It should return the data of the table that needs to be inserted in the database
# It should return a dictionary like this : {'Novak Djokovic': 2, 'Naomi Osaka': 2, 'Iga Świątek': 1, 'Kevin Krawietz': 1, 'Simona Halep': 1, 'Hsieh Su-wei': 1}

def grab_data(url):
    pass


# Create a function called database to insert the values of the dictionary into the table called tennis
def database(dictionary):
    cur, conn = setUpDatabase('tennis.db')
    pass


# Create a vizualization using matplotlib
def viz(data):
    pass



# Uncomment this to make sure your function works
# data = grab_data("https://en.wikipedia.org/wiki/Grand_Slam_(tennis)")
# database(data)
# viz(data)

