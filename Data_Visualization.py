
# importing the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


cancer = pd.read_csv(
    r"C:\Users\sandr\Documents\Assignment\Dataset\total-cancer-deaths-by-type.csv")

country = ['Sweden', 'Switzerland', 'Austria', 'Singapore', 'Finland']

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


cancer2010_19 = cancer[(cancer['Year'] >= 2010) & (cancer['Year'] <= 2019)]

cancer_df = cancer2010_19[cancer2010_19['Country'].isin(country)]

cancer_df = cancer_df.reset_index()


cancer_df['Total'] = cancer_df.loc[:, ['Liver', 'Mesothelioma']].sum(axis=1)

year = np.arange(2010, 2020)
year


def LinePlot(year):
    for c in country:
        year_total = list(cancer_df[cancer_df['Country'] == c]['Total'])
        plt.figure(1, figsize=(10, 6))
        plt.plot(year, year_total, label=c, marker='o')
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


cancer19 = cancer_df[cancer_df['Year'] == 2019]


def StackedBarPlot(xaxis, yaxis1, yaxis2):
    plt.figure(2)
    plt.bar(cancer19['Country'], cancer19['Breast'], label='Breast Cancer')
    plt.bar(cancer19['Country'], cancer19['Tracheal, bronchus, and lung'],
            bottom=cancer19['Breast'], label='Tracheal, bronchus and lung Cancer')
    # plt.legend(fontsize=10, loc=(0.5,0.5))
    plt.show()


cancer19 = cancer[cancer['Year'] == 2019]

cancer_types = cancer19.columns[3:]
cancer19.loc['Grand Total'] = cancer19[cancer_types].sum(axis=0)

values = list(cancer19.loc['Grand Total'][3:])
values

threshold = 1400000

grp_values = []
grp_types = []

low_values = 0
for i in range(len(cancer_types)):
    if values[i] < threshold:
        low_values += values[i]
    else:
        grp_values.append(values[i])
        grp_types.append(cancer_types[i])

grp_values.append(low_values)
grp_types.append('Others')


def PieChart(grp_values, grp_types):
    plt.figure(3, figsize=(10, 6))
    plt.pie(grp_values, labels=grp_types, autopct='%1.1f%%', pctdistance=0.8)
    plt.title('Global Distribution of Cancer-Caused Deaths and Cancer Types 2019',
              fontweight='bold')
    plt.axis('equal')
    plt.legend()
    plt.show()
