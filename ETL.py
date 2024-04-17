import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime 

log_file = "log_file.txt" 
target_file = "transformed_data.csv" 

def extract_from_csv(filename):
    dataframe = pd.read_csv(filename)
    print('extracting csv')
    return dataframe

def extract_from_json(filename):
    dataframe = pd.read_json(filename)
    print('extracting json')
    return dataframe

def extract_from_xml(filename):
    print("extracting xml")
    dataframe = pd.Dataframe(columns=["name", "height", "weight"])
    tree = ET.parse(filename)
    root = tree.getroot
    for person in root:
        name = person.find("name").text
        height = person.find("height").text
        weight = person.find("weight").text
        dataframe = pd.concat([dataframe, pd.Dataframe([{"name":name, "height":height, "weight":weight}])], ignore_index=True)
       
    return dataframe

def extract(): 
    extracted_data = pd.DataFrame(columns=['name','height','weight']) # create an empty data frame to hold extracted data 
     
    # process all csv files 
    for csvfile in glob.glob("*.csv"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True) 
         
    # process all json files 
    for jsonfile in glob.glob("*.json"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True) 
     
    # process all xml files 
    for xmlfile in glob.glob("*.xml"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True) 
         
    return extracted_data 

