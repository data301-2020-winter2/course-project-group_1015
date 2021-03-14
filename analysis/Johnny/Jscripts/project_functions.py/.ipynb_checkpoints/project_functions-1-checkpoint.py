import pandas as pd
import numpy as np

def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and rename the column)

    df1 = (
           pd.read_csv('Medical_Cost.csv')
          .rename(columns={"charges": "Medical Costs per region"})
          .rename(columns={"sex": "Gender"})
          .rename(columns={"smoker": "Tobacco User"})
          .rename(columns={"age": "Age"})
          .rename(columns={"region": "Region"})
          .rename(columns={"children": "Children"})
          .rename(columns={"bmi": "BMI"})
        
        )
    
    # Method Chain 2 ( Cleaning the costs and BMI by riunding them into 2 decimal places)


    def format(x):
        return "${:0.2f}".format(x)
    
    df1['Medical Costs per region'] = (df1['Medical Costs per region'].apply(format)
                                       )
      

    df1['BMI'] = ( round(df1['BMI'])
                  
                 ) 
    # Method Chain  3(Sorting the data )
    df4 = (
           df1.sort_values(by=['Age'], ascending = True)
          )
     # Method Chain  3(Organizing the order of the columns )
    df5 = (
           df4[['Age','Gender','Children','BMI','Tobacco User','Medical Costs per region','Region']]
          )    
    
    return df5
