import pandas as pd
from pprint import pprint 

JR_csv = pd.read_csv("Finished_labels/Jeremy_5_abs_results.csv")
# pprint(JR_csv)

df = pd.DataFrame()
for index, row in JR_csv.iterrows():
    temp = row['Relationship']
    pprint(type(temp))
    temp = pd.DataFrame(temp)
    # id = row['text'].split("\n")[0]
    # for i in range(len(temp)):
    #     print(temp[i])
    #     # temp[i]['ID'] = id
    # df = pd.concat([df, temp])
    
pprint(df)
