from data_process import *

cars = []
database = open("ev_database.csv", "r")
car_data = clean_data(database)