import os
import pandas as pd

"""
Write a program that on input k and XXXX, returns the top k names from year XXXX starting with the letter “s”.
"""
def func1(k, year):
    file_url = f"yob{year}.txt"
    df = pd.read_csv(file_url, ',')
    df.columns = ['Name', 'Gender', 'Freq']
    filtered_df = df[df['Name'].str[0] == 'S']
    res = filtered_df.sort_values(by='Freq', ascending=False).head(k)
    print(res['Name'].tolist())

"""
Write a program that on input Name returns the frequency for men and women of the name Name.
Also find the most common first letter in names for men and women respectively across all years.
"""
def func2(name):
    dfs = []
    for file in os.listdir():
        df = pd.read_csv(file, ',')
        df.columns = ['Name', 'Gender', 'Freq']
        dfs.append(df)
    combined_df = pd.concat(dfs)
    men_freq = combined_df[
        (combined_df['Name'] == name) & (combined_df['Gender'] == 'M')
    ]['Freq'].sum()
    women_freq = combined_df[
        (combined_df['Name'] == name) & (combined_df['Gender'] == 'F')
    ]['Freq'].sum()

    print(f"There are {men_freq} men named {name}.")
    print(f"There are {women_freq} women named {name}.")

    # Create a new column for the first letter
    combined_df['First_Char'] = combined_df['Name'].str[0]
    men_common = combined_df[combined_df['Gender'] == 'M']['First_Char'].value_counts().idxmax()
    women_common = combined_df[combined_df['Gender'] == 'F']['First_Char'].value_counts().idxmax()
    print(f"The most common first letter among men is {men_common}.")
    print(f"The most common first letter among women is {women_common}.")

"""
It could be that names are more diverse now than they were in 1880, so that a name may be
relatively the most popular, though its frequency may have been decreasing over the years.
Modify the above to return the relative frequency. Note that in the next coming lectures we
will learn how to quantify diversity using entropy.
"""
def func3(name):
    for file in os.listdir():
        df = pd.read_table(file, delimiter=',', header=None)
        df.columns = ['Name', 'Gender', 'Freq']
        name_freq = df[df['Name'] == name]['Freq'].sum()
        total_freq = df['Freq'].sum()
        print(f"The relative frequency for the name {name} in the year {file[3:7]} is {name_freq / total_freq}.")

"""
Find all the names that used to be more popular for one gender, but then became more
popular for another gender.
"""
def func4():
    df = pd.DataFrame(columns=['Name', 'Gender', 'Frequency'])

    i = 0
    for file in os.listdir():
        year = file[3:7]
        data = pd.read_csv(file, delimiter=',', names=['Name', 'Gender', 'Frequency'], header=None)
        data['Year'] = year
        """
        for name, group in data.groupby(['Name', 'Year']):
            print(group['Frequency'].max().reset_index())
        """
        res = data.loc[
            data.groupby(['Name'])['Frequency'].idxmax()
        ]
        df = df.append(res, ignore_index=True)
    
    name_counts = df.groupby('Name')['Gender'].nunique()
    changed_names = name_counts[name_counts > 1].index.tolist()
    print(changed_names)


"""
For a given year Y Y Y Y , identify the name with the highest surge in popularity compared to
the previous year. Define ”surge” as the largest percentage increase in frequency.
"""

os.chdir('Names')
