
import requests
import pandas as pd
import os
import glob
import json
import re

pd.options.display.max_columns = None
CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
r = requests.get('https://swapi.dev/api/')
json_data = r.json()
# Data dir is where the original data is stored
raw_data = CURR_DIR_PATH + "/raw/"
# Target dir is where the transformed data is stored
harmonized_data = CURR_DIR_PATH + "/harmonized/"
# print(json_data)


def get_data_raw(data):
    for key, value in data.items():
        q = requests.get(value)
        result_data = q.json()["results"]
        if key == "films":
            df = pd.DataFrame(result_data)
            p = re.compile(r'\r\n')
            df['opening_crawl'] = [p.sub('', x) for x in df['opening_crawl']]
            print(df)
            # df["opening_crawl"].str.replace("\r", "")
            # df["opening_crawl"].str.replace("\n", "")
            df.to_csv(raw_data + key + ".csv", index=False)
        else:
            # print(result_data)
            df = pd.DataFrame(result_data)
            df.to_csv(raw_data + key + ".csv", index=False)
            # print(df)


get_data_raw(json_data)

def get_data_harmonized():
    df = pd.read_csv(raw_data + "films.csv")
    print(df)

# get_data_harmonized()






