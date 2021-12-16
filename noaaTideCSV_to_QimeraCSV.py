import pandas as pd
import glob2

# =============================================================================
# This script, when run inside the directory of the desired files, will convert a NOAA tide CSV to one that is compatible with QPS ASCII file import.
# Outputted from this file is a .csv with one header line. Columns are Timestamp and Verified Water Level in the units on the input file.
# Alter the filename below, then run the script.
# =============================================================================
#filename = 'hp4_tide.csv'

#use glob2 to get .csv files
files = glob2.glob("./*.csv")
print(files)

#DO NOT ALTER BELOW THIS LINE
#######################################
counter = 0
for i in files:
    
    df = pd.read_csv(i, header =0) #csv must be inside the directory of this python script
    
    print(df)
    print('num of rows = ', df.shape[0])
    #print(df.columns)
    #print(df.loc[:,'Date'])
    
    newdf = pd.DataFrame([], columns = ['Timestamp', 'Verified Water Level'], index = range(int(df.shape[0])))
    newdf.loc[:,'Timestamp'] = df.loc[:, 'Date'] + ' '+df.loc[:, 'Time (GMT)']
    newdf.loc[:, 'Verified Water Level']= df.loc[:,'Verified (ft)']
    print(newdf)
    
    def timestamp_to_date_string(timestamp):
        date = timestamp[0:4]+timestamp[5:7]+timestamp[8:10]
        return date
    
    date = timestamp_to_date_string(str(newdf.loc[0,'Timestamp']))
    print(date)
    newfilename = date+'_tide_QPSCompatible_'+'job'+ str(counter) + '.csv'
    newfilepath = ".\\converted_files\\"
    newdf.to_csv(newfilepath+newfilename)
    print(newfilename)
    counter+=1