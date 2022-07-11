
import requests
import pandas as pd
import os
import glob

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
r = requests.get('https://swapi.dev/api/')
json_data = r.json()



def get_data(data):
    for key, value in data.items():
        q = requests.get(value)
        df = pd.DataFrame(q)
        df.to_csv(CURR_DIR_PATH + "/" + key + ".csv", index=False)
        print(df)


get_data(json_data)





