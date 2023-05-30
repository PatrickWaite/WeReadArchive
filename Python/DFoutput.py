import os
from datetime import datetime

def DFoutput(dataframe):
    #check to see if output path exists
    outputDir = '.\collection Volume\WRA_output' #define output folder, should it not exist it will be created 
    isExist = os.path.exists(outputDir)
    print(isExist)
    if not isExist:
        # Create a new directory because it does not exist 
        os.makedirs(outputDir)
        print("The new directory is created!")
#save dataframe outputs to output directory with a date
    date = datetime.now()
    dt = date.strftime("%d%m%Y")
    dataframe.to_csv(f'{outputDir}/DataFrameOutput_{dt}.csv', index=False)
    dataframe.to_excel(f'{outputDir}/DataFrameOutput_{dt}.xlsx', index=False)
    print(f'data has output to {outputDir}')