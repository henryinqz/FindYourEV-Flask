from typing import TextIO, List, Dict, Union
import random
from constants import *

def clean_data(input_file: TextIO) -> Dict:
    input_file.readline().strip().split(",") # First row

    cars = {}
    for info in input_file.readlines():
        info_list = info.split(",")
        for index in range(len(info_list)):
            info_list[index] = info_list[index].strip()

        cars[info_list[MODEL[INDEX]]] = {
            BRAND[CONSTANT]: info_list[BRAND[INDEX]],
            YEAR[CONSTANT]: int(info_list[YEAR[INDEX]]),
            POWER[CONSTANT]: int(info_list[POWER[INDEX]]),
            DRIVETRAIN[CONSTANT]: info_list[DRIVETRAIN[INDEX]],
            FORM_FACTOR[CONSTANT]: info_list[FORM_FACTOR[INDEX]],
            PRICE[CONSTANT]: int(info_list[PRICE[INDEX]]),
            EV_TYPE[CONSTANT]: info_list[EV_TYPE[INDEX]],
            # SAFETY_RATING[CONSTANT]: float(info_list[SAFETY_RATING[INDEX]]),
            RANGE_CAPACITY[CONSTANT]: int(info_list[RANGE_CAPACITY[INDEX]]),
            IMAGE[CONSTANT]: info_list[IMAGE[INDEX]]
        }
    return cars

def search_data(car_data: Dict, search: List[List]) -> List[str]:
    '''
    Return a list of car models that match search query.

    search = [
        [brand, ["Audi", "Honda"]],
        [year, {MIN_YEAR, MAX_YEAR}],
        [power, [HIGH_POWER, NORMAL_POWER, LOW_POWER]],
        [drivetrain, ["AWD", "FWD", "RWD"]],
        [form_factors, ["Compact", "Hatchback", "Large", "Mid-size", "Minivan", "Sedan", "Station Wagon", "Subcompact", "SUV"]],
        [price, {MIN_PRICE, MAX_PRICE}],
        [ev_type, ["PHEV", "BEV", "HFCV"]],
        # [safety_rating, {MIN_RATING, MAX_RATING}],
        [range_capacity, {MIN_RANGE, MAX_RANGE}]
        ]
    ''' 
    search_data = list(car_data.keys())

    for specification, query in search:
        if specification == BRAND[CONSTANT]:
            search_data = update_car_models(get_models_from_brands(car_data, query), search_data)
        elif specification == YEAR[CONSTANT]:
            search_data = update_car_models(get_models_from_years(car_data, query), search_data)
        elif specification == POWER[CONSTANT]:
            search_data = update_car_models(get_models_from_power(car_data, query), search_data)
        elif specification == DRIVETRAIN[CONSTANT]:
            search_data = update_car_models(get_models_from_drivetrain(car_data, query), search_data)
        elif specification == FORM_FACTOR[CONSTANT]:
            search_data = update_car_models(get_models_from_form_factor(car_data, query), search_data)
        elif specification == PRICE[CONSTANT]:
            search_data = update_car_models(get_models_from_price(car_data, query), search_data)
        elif specification == EV_TYPE[CONSTANT]:
            search_data = update_car_models(get_models_from_ev_type(car_data, query), search_data)
        # elif specification == SAFETY_RATING[CONSTANT]:
        #     search_data = update_car_models(get_models_from_safety_rating(car_data, query), search_data)
        elif specification == RANGE_CAPACITY[CONSTANT]:
            search_data = update_car_models(get_models_from_range(car_data, query), search_data)

    return search_data

def update_car_models(cars_with_search_query: List[str], car_models: List[str]) -> List[str]:
    searched_models = car_models.copy()

    for car in car_models:
        if car not in cars_with_search_query:
            searched_models.remove(car)

    return searched_models # Change to searched_models.copy() if there are any bugs!

def get_models_from_brands(car_data: Dict, brands: List[str]) -> List[str]:
    '''
    brands = ["Audi", "Honda"]
    '''
    models_from_search_brands = []

    for model in car_data:
        model_data = car_data[model]
        if model_data["brand"] in brands:
                models_from_search_brands.append(model)
    
    return models_from_search_brands

def get_models_from_years(car_data: Dict, years: Dict[str, int]) -> List[str]:
    '''
    years = {MIN_YEAR, MAX_YEAR}
    '''
    models_from_search_years = []

    for model in car_data:
        model_data = car_data[model]
        if years[MIN_YR] <= model_data[YEAR[CONSTANT]] <= years[MAX_YR]:
                models_from_search_years.append(model)
    
    return models_from_search_years

# def get_models_from_power(car_data: Dict, power: int) -> List[str]:
#     '''
#     power = [HIGH_POWER, NORMAL_POWER, LOW_POWER]
#     '''
#     models_from_search_power = []

#     for model in car_data:
#         model_data = car_data[model]
        
#         for power_level in power:
#             # HIGH_POWER
#             if power_level == HIGH_POWER and model_data[POWER[CONSTANT]] >= HIGH_POWER:
#                 models_from_search_power.append(model)
#             # NORMAL_POWER
#             elif power_level == NORMAL_POWER and NORMAL_POWER <= model_data[POWER[CONSTANT]] < HIGH_POWER:
#                 models_from_search_power.append(model)
#             # LOWER POWER
#             elif power_level == LOW_POWER and LOW_POWER <= model_data[POWER[CONSTANT]] < NORMAL_POWER:
#                 models_from_search_power.append(model)
    
#     return models_from_search_power
def get_models_from_power(car_data: Dict, power: Dict[str, int]) -> List[str]:
    '''
    power = {MIN_POWER, MAX_POWER}
    '''
    models_from_search_power = []

    for model in car_data:
        model_data = car_data[model]
        if power[MIN_POWER] <= model_data[POWER[CONSTANT]] <= power[MAX_POWER]:
                models_from_search_power.append(model)
    
    return models_from_search_power

def get_models_from_drivetrain(car_data: Dict, drivetrain: List[str]) -> List[str]:
    '''
    drivetrain = ["AWD", "FWD", "RWD"]
    '''
    models_from_search_drivetrain = []

    for model in car_data:
        model_data = car_data[model]
        if model_data[DRIVETRAIN[CONSTANT]] in drivetrain:
                models_from_search_drivetrain.append(model)
    
    return models_from_search_drivetrain

def get_models_from_form_factor(car_data: Dict, form_factors: List[str]) -> List[str]:
    '''
    form_factors = ["Compact", "Hatchback", "Large", "Mid-size", "Minivan", "Sedan", "Station Wagon", "Subcompact", "SUV"]
    '''
    models_from_search_form_factor = []

    for model in car_data:
        model_data = car_data[model]
        if model_data[FORM_FACTOR[CONSTANT]] in form_factors:
                models_from_search_form_factor.append(model)
    
    return models_from_search_form_factor

def get_models_from_price(car_data: Dict, price: Dict[str, int]) -> List[str]:
    '''
    price = {MIN_PRICE, MAX_PRICE}
    '''
    models_from_search_price = []

    for model in car_data:
        model_data = car_data[model]
        if price[MIN_PRICE] <= model_data[PRICE[CONSTANT]] <= price[MAX_PRICE]:
                models_from_search_price.append(model)
    
    return models_from_search_price

def get_models_from_ev_type(car_data: Dict, ev_type: List[str]) -> List[str]:
    '''
    ev_type = ["PHEV", "BEV", "HFCV"]
    '''
    models_from_search_ev_type = []

    for model in car_data:
        model_data = car_data[model]
        if model_data[EV_TYPE[CONSTANT]] in ev_type:
                models_from_search_ev_type.append(model)
    
    return models_from_search_ev_type

# def get_models_from_safety_rating(car_data: Dict, safety_rating: Dict[str, int]) -> List[str]:
#     '''
#     safety_rating = {MIN_RATING, MAX_RATING}
#     '''
#     models_from_search_safety = []
    
#     for model in car_data:
#         model_data = car_data[model]
#         if safety_rating[MIN_RATING] <= model_data[SAFETY_RATING[CONSTANT]] <= safety_rating[MAX_RATING]:
#             models_from_search_safety.append(model)
    
#     return models_from_search_safety

def get_models_from_range(car_data: Dict, range_capacity: Dict[str, int]) -> List[str]:
    '''
    range_capacity = {MIN_RANGE, MAX_RANGE}
    '''
    models_from_search_range = []

    for model in car_data:
        model_data = car_data[model]
        if range_capacity[MIN_RANGE] <= model_data[RANGE_CAPACITY[CONSTANT]] <= range_capacity[MAX_RANGE]:
            models_from_search_range.append(model)
    
    return models_from_search_range

def get_random_cars_from_search_data(search_data: List[str], num_results: int) -> List[str]:
    if num_results > len(search_data) or num_results == -1: # Requesting more results than exists in search_data or no limit (-1)
        num_results = len(search_data)
        
    return random.sample(search_data, num_results)

def get_data_from_model(car_data: List[str], search_data: List[str]) -> Dict:
    search_data_dict = {}
    for model in search_data:
        search_data_dict[model] = car_data[model]

    return search_data_dict

# ---
def get_unique_data_values(car_data: Dict) -> Dict:
    '''
    Return sorted all_unique_data = {
        BRAND[CONSTANT]: ['Audi', ... , 'Volvo'],
        YEAR[CONSTANT]: {MIN_YR: 0, MAX_YR: 1000000},
        POWER[CONSTANT]: {MIN_POWER: 0, MAX_POWER: 1000},
        DRIVETRAIN[CONSTANT]: ['AWD', ... , 'RWD'],
        FORM_FACTOR[CONSTANT]: ['Compact', ... , 'Subcompact'],
        PRICE[CONSTANT]: {MIN_PRICE: 0, MAX_PRICE: 1000},
        EV_TYPE[CONSTANT]: ['BEV', ... , 'PHEV'],
        RANGE_CAPACITY[CONSTANT]: {MIN_RANGE: 0, MAX_RANGE: 5000},
    }
    (note: no models)
    '''
    all_unique_data = {}
    
    brands, drivetrains, form_factors, ev_types = [], [], [], []
    years = dict.fromkeys([MIN_YR, MAX_YR])
    powers = dict.fromkeys([MIN_POWER, MAX_POWER])
    prices = dict.fromkeys([MIN_PRICE, MAX_PRICE])
    range_capacities = dict.fromkeys([MIN_RANGE, MAX_RANGE])

    for key in car_data:
        # Brand
        brand = car_data[key][BRAND[CONSTANT]]
        if brand not in brands:
            brands.append(brand)

        # Drivetrain
        drivetrain = car_data[key][DRIVETRAIN[CONSTANT]]
        if drivetrain not in drivetrains:
            drivetrains.append(drivetrain)

        # Form factor
        form_factor = car_data[key][FORM_FACTOR[CONSTANT]]
        if form_factor not in form_factors:
            form_factors.append(form_factor)

        # EV Type
        ev_type = car_data[key][EV_TYPE[CONSTANT]]
        if ev_type not in ev_types:
            ev_types.append(ev_type)

        # Price {MIN_PRICE: 0, MAX_PRICE: 1000000}
        price = car_data[key][PRICE[CONSTANT]]
        if prices[MIN_PRICE] == None or prices[MIN_PRICE] > price:
            prices[MIN_PRICE] = price
        if prices[MAX_PRICE] == None or prices[MAX_PRICE] < price:
            prices[MAX_PRICE] = price

        # Year
        year = car_data[key][YEAR[CONSTANT]]
        if years[MIN_YR] == None or years[MIN_YR] > year:
            years[MIN_YR] = year
        if years[MAX_YR] == None or years[MAX_YR] < year:
            years[MAX_YR] = year

        # Power
        power = car_data[key][POWER[CONSTANT]]
        if powers[MIN_POWER] == None or powers[MIN_POWER] > power:
            powers[MIN_POWER] = power
        if powers[MAX_POWER] == None or powers[MAX_POWER] < power:
            powers[MAX_POWER] = power

        # Range
        range_capacity = car_data[key][RANGE_CAPACITY[CONSTANT]]
        if range_capacities[MIN_RANGE] == None or range_capacities[MIN_RANGE] > range_capacity:
            range_capacities[MIN_RANGE] = range_capacity
        if range_capacities[MAX_RANGE] == None or range_capacities[MAX_RANGE] < range_capacity:
            range_capacities[MAX_RANGE] = range_capacity

    brands.sort()
    drivetrains.sort()
    form_factors.sort()
    ev_types.sort()
    
    all_unique_data[BRAND[CONSTANT]] = brands
    all_unique_data[DRIVETRAIN[CONSTANT]] = drivetrains
    all_unique_data[FORM_FACTOR[CONSTANT]] = form_factors
    all_unique_data[EV_TYPE[CONSTANT]] = ev_types
    all_unique_data[PRICE[CONSTANT]] = prices
    all_unique_data[YEAR[CONSTANT]] = years
    all_unique_data[POWER[CONSTANT]] = powers
    all_unique_data[RANGE_CAPACITY[CONSTANT]] = range_capacities

    return all_unique_data