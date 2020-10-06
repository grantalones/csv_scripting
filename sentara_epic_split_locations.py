import pandas as pd
import numpy as np
import os
import shutil


def split_locations():
    path = os.getcwd()

    if "split_file" in os.listdir(path):
        shutil.rmtree(path+"/split_file/")

    file_count_start = len(os.listdir(path))


    sentara_locations = {
        "SENTARA ALBEMARLE MEDICAL CENTER": "Sentara_Albemarle-748",
        "SENTARA CAREPLEX HOSPITAL": "Sentara_Careplex_Hospital-746" ,
        "SENTARA PORT WARWICK": "Sentara_Careplex_Hospital-746",
        "SENTARA LEIGH HOSPITAL": "Sentara_Leigh_Hospital-308",
        "AIC HEART HOSPITAL": "Sentara_Norfolk_General_Hospital-43",
        "AMBULATORY CARE CENTER": "Sentara_Norfolk_General_Hospital-43",
        "SENTARA HEART HOSPITAL": "Sentara_Norfolk_General_Hospital-43",
        "SENTARA NORFOLK GENERAL HOSPITAL": "Sentara_Norfolk_General_Hospital-43",
        "SENTARA BELLEHARBOUR": "Sentara_Obici_Hospital-36",
        "SENTARA OBICI HOSPITAL": "Sentara_Obici_Hospital-36",
        "SENTARA PRINCESS ANNE HOSPITAL": "Sentara_Princess Anne Hospital-42",
        "HOSPITAL FOR EXTENDED RECOVERY": "Sentara_Virginia Beach General Hospital-29" ,
        "SENTARA INDEPENDENCE": "Sentara_Virginia Beach General Hospital-29" ,
        "SENTARA VIRGINIA BEACH GENERAL HOSPITAL": "Sentara_Virginia Beach General Hospital-29",
        "SENTARA WILLIAMSBURG REGIONAL MEDICAL CENTER": "Sentara_Williamsburg_Regional_Medical_Center-749",
        "SENTARA GEDDY OCC": "Sentara_Williamsburg_Regional-Medical-Center-749",
        "Sentara Orthopedics East Rockingham": "Sentara_Rockingham-559",
        "Sentara Orthopedics James Madison": "Sentara_Rockingham-559",
        "SENTARA RMH MEDICAL CENTER": "Sentara_Rockingham-559",
        "SENTARA LAKE RIDGE": "Sentara_Northern_Virginia-39",
        "SENTARA NORTHERN VIRGINIA MEDICAL CENTER": "Sentara_Northern_Virginia-39",
        "PROFFIT ROAD 29N" : "Sentara_Martha_Jefferson-741",
        "SENTARA MARTHA JEFFERSON HOSPITAL": "Sentara_Martha_Jefferson-741"
    }



    os.mkdir(path+"/split_file/")
    for file in os.listdir(path):
        if ".txt" in str(file.lower()):
            filename = file[:-4]#get rid of .txt
            df = pd.read_csv(file, index_col=None, header=0, delimiter="|", encoding="ISO-8859-1")
            df["Sentara_hospital"] = df["Location"].map(sentara_locations)
            nan_locations = {'Sentara_hospital': "Not_Audited"}
            df.fillna(value=nan_locations, inplace = True)
            print (df.Sentara_hospital.unique())
            for location in df.Sentara_hospital.unique():
                print(path, location, filename)

                # sub_df = df.loc[df.Sentara_Hospital == location]

                # sub_df.to_csv(path+"/split_file/"+location.replace(" ", "_")+"_"+filename+".csv", index = False)

        else:
            continue
    file_count_end = len(os.listdir(path))

    checksum = file_count_end - file_count_start
    try:
        assert not ("E+" in str(df))
    except AssertionError:
        print ("Scientific Notation in CSV")
    try:
        assert (checksum > 0)
    except AssertionError as error:
        print (error)
        print ("No .txt file detected! what the heck!")
split_locations()
