import json
import pickle
import numpy as np

__city = None
__dataColumns = None
__model = None
__type = None

def get_estimated_price(city,sqft,bedroom, type, Age):
    try:
        loc_index = __dataColumns.index(city.lower())
    except:
        loc_index = -1

    try:
        loc_index2 = __dataColumns.index(type.lower())
    except:
        loc_index2 = -1

    x = np.zeros(len(__dataColumns))
    x[0] = bedroom
    x[1] = sqft
    x[2] = Age
    if loc_index >= 0:
        x[loc_index] = 1
    if loc_index2 >= 0:
        x[loc_index2] = 1

    return round(__model.predict([x])[0],2)

def get_city_names():
    return __city

def get_types():
    return __type


def load_saved_artifacts():
    print('Loading saved artifacts')
    global __dataColumns
    global __city
    global __type
    global __model


    with open("./Artifacts/columns.json", "r") as f:
        __dataColumns= json.load(f)['data_columns']
        __city = __dataColumns[3:7]
        __type = __dataColumns[7:]


    with open("./Artifacts/Canada_home_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)
        print("loading saved artifacts... done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_city_names())
    print(get_types())
    print(get_estimated_price('Calgary',100, 2,'Condo',2))