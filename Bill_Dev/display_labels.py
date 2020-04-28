import json
from pprint import pprint
import os

import pandas as pd

# with open("Finished_labels/RJ_result.json", 'r') as f:
#     parsed_json = json.load(f)

def generate_df(parsed_json, i):
    result = parsed_json[i]['completions'][0]['result']
    id = parsed_json[i]['data']['text']
    id = id.split('\n')[0]

    result_ls = []
    for elem in result:
        elem['value']['ID'] = id
        result_ls.append(elem['value'])

    df = pd.DataFrame(result_ls)
    return df


# RJ and TM
# df = pd.DataFrame()
# for i in range(5):
#     temp = generate_df(parsed_json, i)
#     df = pd.concat([df, temp])

# df.sort_values(by=['labels', 'ID'], inplace=True)

# ZH
file_list = [file_name for file_name in os.listdir('./Finished_labels/') if file_name.startswith('Zhi')]
print(file_list)

df = pd.DataFrame()

for file_name in file_list:
    with open("Finished_labels/"+file_name, 'r') as f:
        parsed_json = json.load(f)
    temp = generate_df(parsed_json, 0)
    df = pd.concat([df, temp])

df.to_csv('ZH_results.csv')

pprint(df)