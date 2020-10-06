# agg_then_split for sentara stations

import pandas as pd
import numpy as np
import os
import shutil

def aggregate_source_files(name):
    import os
    li = []
    path = os.getcwd()
    print (path)
    file_counter = 0
    for file in os.listdir(path):
        if ".csv" in str(file.lower()):
            df = pd.read_csv(path+"/"+file, index_col=None, header=0, encoding="ISO-8859-1")
            li.append(df)
            file_counter = file_counter+1
            print (file, file_counter, "csv")
        # elif ".xls" in str(file.lower()):
        #     df = pd.read_excel(path+"/"+file)
        #     li.append(df)
        #     file_counter = file_counter+1
        #     print (file, file_counter, "xls")
        else:
            continue
    try:
        frame = pd.concat(li, axis=0, ignore_index=True, sort = False)
    except ValueError:
        print ("Empty DataFrame")
        frame = pd.DataFrame()
    frame.to_csv(path+"/"+name+".csv", index = False)

def camelCase(st):
    output = ''.join(x for x in st.title() if x.isalnum())
    return output[0].lower() + output[1:]

def split_locations():
    path = os.getcwd()

    if "split_file" in os.listdir(path):
        shutil.rmtree(path+"/split_file/")

    file_count_start = len(os.listdir(path))

    os.mkdir(path+"/split_file/")
    for file in os.listdir(path):
        if "agged.csv" in str(file.lower()):
            filename = file[:-4]
            df = pd.read_csv(file, index_col=None, header=0, encoding="ISO-8859-1")
            df["location"] = df["omni_stid"].str[:2]
            for location in df.location.unique():
                print(path, location, filename)

                sub_df = df.loc[df.location == location]

                sub_df.to_csv(path+"/split_file/"+location.replace(" ", "_")+".csv", index = False)

        else:
            continue
    file_count_end = len(os.listdir(path))
    shutil.copy("agged.csv", path+"/split_file/agged.csv")
    os.remove("agged.csv")

    checksum = file_count_end - file_count_start
    try:
        assert (checksum > 0)
    except AssertionError as error:
        print (error)
        print ("No .csv file detected! what the heck!")


aggregate_source_files("agged")
split_locations()
