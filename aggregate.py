import pandas as pd
import numpy as np
import os

def aggregate_source_files(name):
    import os
    li = []
    path = os.getcwd()
    file_counter = 0
    for file in os.listdir(path):
        if "csv" in str(file.lower()):
            f = open(file, "r")
            if "|" in f.read():
                df = pd.read_csv(path+"/"+file, index_col=None, delimiter = "|", header=0, encoding = "ISO-8859-1")
            else:
                df = pd.read_csv(path+"/"+file, index_col=None, header=0)
            li.append(df)
            file_counter = file_counter+1
            print (file_counter)
        if "xls" in str(file.lower()):
            f = open(file, "r")
            df = pd.read_excel(path + "/" + file)
            li.append(df)
            file_counter = file_counter + 1
            print(file_counter)
        else:
            continue
    try:
        frame = pd.concat(li, axis=0, ignore_index=True, sort = False)
    except ValueError:
        print ("Empty DataFrame")
        frame = pd.DataFrame()
    frame.to_csv(path+"/"+name+".csv", index = False)
    # return frame

def camelCase(st):
    output = ''.join(x for x in st.title() if x.isalnum())
    return output[0].lower() + output[1:]

nickname = input ("file nickname?\n")
nickname = camelCase(nickname)

aggregate_source_files(nickname)
