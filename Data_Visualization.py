
# importing the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def LinePlot(xaxis):
    for c in country:
        # Total cancer deaths of each year
        yaxis = list(cancer_df[cancer_df['Country'] == c]['Total'])
        plt.figure(1, figsize=(10, 6))
        plt.plot(xaxis, yaxis, label=c, marker='o')
        plt.xlim([2010, 2019])
        plt.ylim([486, 980])
        plt.xticks(np.arange(2010, 2020))
        plt.yticks(np.arange(450, 1000, 50))
        plt.title('Cancer attributed Deaths of 5 Countries (2010-2019)',
                  fontsize=15, fontweight='bold')
        plt.xlabel('Year', fontsize=12)
        plt.ylabel('Total Cancer Deaths', fontsize=12)

    plt.legend(loc='best')
    plt.savefig('CancerVsCountry.png')
    plt.show()


def StackedBarPlot(xaxis, yaxis1, yaxis2):
    plt.figure(2, figsize=(10, 6))
    plt.bar(xaxis, yaxis1, label='Breast Cancer')
    plt.bar(xaxis, yaxis2,
            bottom=yaxis1, label='Tracheal, bronchus and lung Cancer')
    plt.title('Comparison of Breast and Tracheal, bronchus, and lung Cancer'+'\n'
              + 'Caused Deaths of 5 Countries in 2019', fontweight='bold')
    plt.xlabel('Countries', fontsize=12)
    plt.ylabel('Cancer Death Count', fontsize=12)
    plt.legend(loc=(0.210, 0.8))
    plt.savefig('Breast_cancer_Vs_Lung_cancer.png')
    plt.show()


def PieChart(grp_values, grp_types):
    plt.figure(3, figsize=(12, 6))
    plt.pie(grp_values, labels=grp_types, autopct='%1.1f%%', pctdistance=0.8)
    plt.title(
        'Global Distribution of Cancer-Caused Deaths and Cancer Types 2019' +
        '\n', fontweight='bold')
    plt.axis('equal')
    plt.legend(loc=(0.8, 0.01))
    plt.savefig('Global_Distribution_of_Cancer-Caused_Deaths')
    plt.show()


# Reading the csv file
cancer = pd.read_csv(
    r"C:\Users\sandr\Documents\Assignment\Dataset\total-cancer-deaths-by-type.csv")

# Renamed the column names for easy access
cancer.columns = ['Country', 'Code', 'Year', 'Liver', 'Kidney',
                  'Lip and Oral', 'Tracheal, bronchus, and lung',
                  'Larynx', 'Gallbladder and biliary tract',
                  'Malignant skin melanoma', 'Leukemia',
                  'Hodgkin lymphoma', 'Multiple myeloma',
                  'Other neoplasms', 'Breast', 'Prostate',
                  'Thyroid', 'Stomach', 'Bladder', 'Uterine',
                  'Ovarian', 'Cervical', 'Brain and central nervous system',
                  'Non-Hodgkin lymphoma', 'Pancreatic cancer',
                  'Esophageal cancer', 'Testicular', 'Nasopharynx',
                  'Other pharynx', 'Colon and rectum',
                  'Non-melanoma skin', 'Mesothelioma']

# Creating a new Dataframe with cancer record from 2010 to 2019
cancer2010_19 = cancer[(cancer['Year'] >= 2010) & (cancer['Year'] <= 2019)]

# Selecting 5 Countries randomly and forming a list
country = ['Sweden', 'Switzerland', 'Austria', 'Singapore', 'Finland']

# Filtering the dataframe into these 5 countries records
cancer_df = cancer2010_19[cancer2010_19['Country'].isin(country)]

# Reseting the index for the filtered dataframe cancer_df
cancer_df = cancer_df.reset_index()

# Creating a new column 'Total' which adds up the values
#                     of all cancer types of these 5 countries
# This is done for drawing the line plot of the total cancer deaths of
#            these 5 countries in the given years
cancer_df['Total'] = cancer_df.loc[:, ['Liver', 'Mesothelioma']].sum(axis=1)

# list of selected years ie., 2010 to 2019
year = np.arange(2010, 2020)

# Filtering the dataframe cancer_df for the year 2019
cancer19 = cancer_df[cancer_df['Year'] == 2019]

# Creating a new Dataframe with data of all countries and all
#                  cancer type deaths of a single year(2019)
cancer_19 = cancer[cancer['Year'] == 2019]

# List of cancer types
cancer_types = cancer_19.columns[3:]

# Creating a new row 'Grand Total' which gives the type wise total
#                      deaths in the year 2019
cancer_19.loc['Grand Total'] = cancer_19[cancer_types].sum(axis=0)

# list of total deaths caused by each cancer type
values = list(cancer_19.loc['Grand Total'][3:])

# setting a threshold for creating a pie 'others' so that the cancer
#      types causing deaths less than 1400000 comes under this pie
threshold = 1400000

grp_values = []  # creating an empty list for grouped values
grp_types = []   # creating an empty list for grouped types

low_values = 0  # setting a variable low_value as 0

# starting a for loop to loop through the list of cancer types
#              and its values to compare it with the threshold set
for i in range(len(cancer_types)):
    if values[i] < threshold:  # to check the condition of death count and threshold
        low_values += values[i]  # if less then added with low_values
    else:
        # else added to the list of grouped values
        grp_values.append(values[i])
        grp_types.append(cancer_types[i])  # and types

grp_values.append(low_values)   # the newly created set of low values
grp_types.append('Others')  # appended to the list as 'Others'

# calling line plot function
LinePlot(year)

# calling stacked bar plot function
StackedBarPlot(cancer19['Country'], cancer19['Breast'],
               cancer19['Tracheal, bronchus, and lung'])

# calling pie plot function
PieChart(grp_values, grp_types)
