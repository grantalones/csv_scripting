import pandas as pd
import numpy as np
import sys
import os

def day_split_files(name):
    import os
    li = []
    path = "/Users/grantpemberton/Desktop/daysplitter/"
    day_counter = 0

    for file in os.listdir(path):
        if "csv" in str(file.lower()):
            day_split(file)
        else:
            continue
        if "csv" in str(file.lower()):
            df = pd.read_csv(path+file, index_col=None, header=0)
            li.append(df)
            file_counter = file_counter+1
            print (file_counter)
        else:
            continue
    try:
        frame = pd.concat(li, axis=0, ignore_index=True, sort = False)
    except ValueError:
        print ("Empty DataFrame")
        frame = pd.DataFrame()
    frame.to_csv(path+name+".csv", index = False)
    # return frame

def camelCase(st):
    output = ''.join(x for x in st.title() if x.isalnum())
    return output[0].lower() + output[1:]

nickname = input ("file nickname?\n")
nickname = camelCase(nickname)

day_split_source_file(nickname)
