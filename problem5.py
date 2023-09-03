import numpy as np
import pandas as pd

def problem5():
    # Read in the data
    df = pd.read_csv('PatientData.csv', header=None)
    data = df.values
    
    # Number of rows
    #print("Number of Patients: ", len(df.index))

    # Number of columns
    #print("Number of Features: ",len(data[0]))

    # Feature 1 is the age of the patient (avg of about 46.5)
    # Feature 2 is the gender of the patient (avg of about 0.5 implying half male and half female)
    # Feature 3 is the height of the patient in cm (avg of about 166 cm, a reasonable avg height)
    # Feature 4 is the weight of the patient in kg (avg of about 68 kg, a reasonable avg weight)
    #print(df.head())
    #print(df.describe())
    # Determined features using the describe function

    # Replace missing values with the mean of the column
    df = df.replace('?', np.NaN)
    df = df.fillna(df.mean(numeric_only=True))


    print(df.head())

    # Part D
    # Use correlation matrix to determine which features are correlated
    # Lower correlation values for features imply they are more independent and influence the outcome more

    # Find the correlation matrix
    corr = df.corr()
    print(corr)






    

 



problem5()