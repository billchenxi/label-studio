import pandas as pd
from pprint import pprint
import json

JR_csv = pd.read_csv("Finished_labels/Jeremy_5_abs_results.csv")
# pprint(JR_csv)

output = []
for index, row in JR_csv.iterrows():
    temp = json.loads(row['Relationship'])
    temp_dict = {}
    temp_dict["completions"] = [{"result": []}]
    for elem in temp:
        temp_input = {
                "from_name": "Relationship",
                "source": "$text",
                "to_name": "text",
                "type": "labels",
                "value": elem}

        temp_dict["completions"][0]["result"].append(temp_input)

    temp_dict["data"] = {"text": row['text']}

    output.append(temp_dict)

    # temp = pd.DataFrame(temp)
    # id = row['text'].split("\n")[0]
    # for i in range(len(temp)):
    #     print(temp[i])
    #     # temp[i]['ID'] = id
    # df = pd.concat([df, temp])
with open("../JO_results_processed.json", 'w') as jf:
    json.dump(output, jf)
pprint(output)
