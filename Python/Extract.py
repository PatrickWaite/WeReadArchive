#imports 
from traceback import print_tb
from dbConnect import get_connectionString
from queries import marcTabPull
from DFoutput import DFoutput
from sqlalchemy import create_engine, text
import pandas as pd
from tkinter import filedialog as fd

#in DFoutput.py
####import os
####from datetime import datetime



def connAndCall(query):
    try:
        # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
        engine = create_engine(
            url=get_connectionString()) #pull connection string from dbConnect.py so that connection isn't hard coded in main file
        print(
            f"Connection created successfully.")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

#create connection and execute query from quries.py
    with engine.connect() as conn: 
            #Note call the text() from sqlachemy to turn the text string result from get_inventoryQuery() into an executable SQL
        df = pd.DataFrame(conn.execute(text(query)))
        return df

def pullWeReadData():
   FileString = fd.askopenfilename()
   fileDataframe = pd.read_csv(FileString)
   return fileDataframe

def bindFrames(driver,queryFrame):
    mergebind = driver.merge(queryFrame,how='outer',left_on='ISBN',right_on='ISBN')
    return mergebind

def main():
    #pull data in from csv file that contains isbn numbers
    WRAD = pullWeReadData()
    #cast the isbn column as type string
    list = WRAD.ISBN.astype('str')
    #as the inital values in the datafile are float64 we need to remove the .0 from all the records in the list of isbns after it is changed to string value
    hapslist =  [s.replace(".0","") for s in list]
    WRAD['ISBN'] = hapslist
    #we assign the entire list as as string variable this allows us to further refine and format the ISBN data for insert into the query call
    x = str(hapslist)
    #formatting the list of strings to remove the preceeding and ending double quotations as well as the square bracket list indicatators. 
    #this should leave us with a string of comma seperated values formated for postgresql to process as part of the query needed to extract the data in FOLIO
    x = x.replace('"','').replace('[','').replace(']','').replace('"','')
    #call the query to pull marctab data based on the records loaded from the isbn file
    frameCall = connAndCall(marcTabPull(x))
    mergecat = bindFrames(WRAD,frameCall)
    #push DataFrame to the DFoutput process to output dataframe as a CSV and XLSX file. 
    DFoutput(mergecat)
    

if __name__ == '__main__':
    main()
    