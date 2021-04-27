from findyourev.data_process import *

cars = []
database = open("findyourev/ev_database.csv", "r")
car_data = clean_data(database)
database.close()


car_data_unique_vals = get_unique_data_values(car_data)
brands = car_data_unique_vals[BRAND[CONSTANT]]
drivetrains = car_data_unique_vals[DRIVETRAIN[CONSTANT]]
form_factors = car_data_unique_vals[FORM_FACTOR[CONSTANT]]
ev_types = car_data_unique_vals[EV_TYPE[CONSTANT]]
prices = car_data_unique_vals[PRICE[CONSTANT]]
years = car_data_unique_vals[YEAR[CONSTANT]]
powers = car_data_unique_vals[POWER[CONSTANT]]
range_capacities = car_data_unique_vals[RANGE_CAPACITY[CONSTANT]]