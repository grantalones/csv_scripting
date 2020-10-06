import os
import pandas as pd
import datetime

def fix_UMMC_date(filename):
    
    UMMC_file = pd.read_csv(filename)
    UMMC_file.dropna(thresh = 2, inplace = True)
    UMMC_file['new_admin_time'] = UMMC_file['ADMIN_DATE_TIME'].apply(lambda x: datetime.datetime.strptime(str(x), '%Y/%m/%d %H:%M:%S'))
    UMMC_file['Admin_day'] = UMMC_file['new_admin_time'].apply(lambda x: x.strftime('%d'))
    UMMC_file['ADMIN_DATE_TIME'] = UMMC_file['new_admin_time'].apply(lambda x: x.strftime('%d')+"-"+x.strftime('%b').upper()+"-"+x.strftime('%y')+" "+x.strftime('%H:%M:%S'))
    UMMC_file = UMMC_file.loc[UMMC_file['Admin_day'] == UMMC_file['Admin_day'].mode()[0]]
    UMMC_file.to_csv(filename+'_mod.csv', index = False)
    
name = input ("input_file?\n")
name_array = name.split(".")
name = name_array[0] + ".csv"


fix_UMMC_date(name)
