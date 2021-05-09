from flask import render_template, url_for, flash, redirect, session
from findyourev import app
from findyourev.forms import SearchForm

from findyourev.data import cars, car_data
# from findyourev.data import car_data
from findyourev.data_process import * # Import from findyourev.data?
from findyourev.constants import *

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        # Reset cars list
        cars.clear() # Reset cars list
        # if "cars" in session:
        #     session["cars"].clear()
        # session["cars"] = []

        # Load search query
        search = []
        price, year, range_capacity, power = {}, {}, {}, {}
        for key in form.data:
            if key != "submit" and key != "csrf_token" and form.data[key] != []:
                if key == MIN_PRICE or key == MAX_PRICE:
                    price[key] = form.data[key]
                elif key == MIN_YR or key == MAX_YR:
                    year[key] = form.data[key]
                elif key == MIN_RANGE or key == MAX_RANGE:
                    range_capacity[key] = form.data[key]
                elif key == MIN_POWER or key == MAX_POWER:
                    power[key] = form.data[key]
                else:
                    search.append([key, form.data[key]])

        search.append([PRICE[CONSTANT], price]) # Price dict {MIN_PRICE, MAX_PRICE}
        search.append([YEAR[CONSTANT], year]) # Year dict {MIN_YEAR, MAX_YEAR}
        search.append([RANGE_CAPACITY[CONSTANT], range_capacity]) # Range dict {MIN_RANGE, MAX_RANGE}
        search.append([POWER[CONSTANT], power]) # Power dict {MIN_POWER, MAX_POWER}
        
        # Get random search data, then send
        car_search_data = search_data(car_data, search) # Car model names in list
        random_search_data = get_data_from_model(car_data, get_random_cars_from_search_data(car_search_data, -1)) # Get all cars from search query 
        for key in random_search_data:
            new_car = random_search_data[key]
            new_car["model"] = key
            cars.append(new_car)
            # session["cars"].append(new_car)

        if len(random_search_data) > 0:
            flash(f"Queried {len(random_search_data)} cars!", "success")
            return redirect(url_for("results"))
        else:
            flash("Search query yielded no results!", "danger")

    return render_template("search.html", title="Search", form=form)

@app.route("/results")
def results():
    if cars == []:
    # if "cars" not in session:
        flash("No cars found!", "danger")
        return redirect(url_for("search"))
    return render_template("results.html", title="Results", cars=cars)
    # return render_template("results.html", title="Results", cars=session["cars"])