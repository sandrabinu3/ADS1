
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cancer=pd.read_csv(r"C:\Users\sandr\Documents\Assignment\Dataset\total-cancer-deaths-by-type.csv")

country=['Sweden','Switzerland', 'Austria', 'Singapore', 'Finland']  

cancer1=cancer.rename(columns={'Entity':'Country', 'Code':'Code',
                                'Year':'Year',
    'Deaths - Liver cancer - Sex: Both - Age: All Ages (Number)':'Liver',
    'Deaths - Kidney cancer - Sex: Both - Age: All Ages (Number)':'Kidney',
    'Deaths - Lip and oral cavity cancer - Sex: Both - Age: All Ages (Number)':'Lip and Oral',
    'Deaths - Tracheal, bronchus, and lung cancer - Sex: Both - Age: All Ages (Number)':'Tracheal, bronchus, and lung',
    'Deaths - Larynx cancer - Sex: Both - Age: All Ages (Number)':'Larynx',
    'Deaths - Gallbladder and biliary tract cancer - Sex: Both - Age: All Ages (Number)':'Gallbladder and biliary tract',
    'Deaths - Malignant skin melanoma - Sex: Both - Age: All Ages (Number)':'Malignant skin melanoma',
    'Deaths - Leukemia - Sex: Both - Age: All Ages (Number)':'Leukemia',
    'Deaths - Hodgkin lymphoma - Sex: Both - Age: All Ages (Number)':'Hodgkin lymphoma',
    'Deaths - Multiple myeloma - Sex: Both - Age: All Ages (Number)':'Multiple myeloma',
    'Deaths - Other neoplasms - Sex: Both - Age: All Ages (Number)':'Other neoplasms',
    'Deaths - Breast cancer - Sex: Both - Age: All Ages (Number)':'Breast',
    'Deaths - Prostate cancer - Sex: Both - Age: All Ages (Number)':'Prostate',
    'Deaths - Thyroid cancer - Sex: Both - Age: All Ages (Number)':'Thyroid',
    'Deaths - Stomach cancer - Sex: Both - Age: All Ages (Number)':'Stomach',
    'Deaths - Bladder cancer - Sex: Both - Age: All Ages (Number)':'Bladder',
    'Deaths - Uterine cancer - Sex: Both - Age: All Ages (Number)':'Uterine',
    'Deaths - Ovarian cancer - Sex: Both - Age: All Ages (Number)':'Ovarian',
    'Deaths - Cervical cancer - Sex: Both - Age: All Ages (Number)':'Cervical',
    'Deaths - Brain and central nervous system cancer - Sex: Both - Age: All Ages (Number)':'Brain and central nervous system',
    'Deaths - Non-Hodgkin lymphoma - Sex: Both - Age: All Ages (Number)':'Non-Hodgkin lymphoma',
    'Deaths - Pancreatic cancer - Sex: Both - Age: All Ages (Number)':'Pancreatic cancer',
    'Deaths - Esophageal cancer - Sex: Both - Age: All Ages (Number)':'Esophageal cancer',
    'Deaths - Testicular cancer - Sex: Both - Age: All Ages (Number)':'Testicular',
    'Deaths - Nasopharynx cancer - Sex: Both - Age: All Ages (Number)':'Nasopharynx',
    'Deaths - Other pharynx cancer - Sex: Both - Age: All Ages (Number)':'Other pharynx',
    'Deaths - Colon and rectum cancer - Sex: Both - Age: All Ages (Number)':'Colon and rectum',
    'Deaths - Non-melanoma skin cancer - Sex: Both - Age: All Ages (Number)':'Non-melanoma skin',
    'Deaths - Mesothelioma - Sex: Both - Age: All Ages (Number)':'Mesothelioma'}, inplace='True')


cancer2010_19=cancer[(cancer['Year']>=2010) & (cancer['Year']<=2019)]

cancer_df=cancer2010_19[cancer2010_19['Country'].isin(country)]

cancer_df=cancer_df.reset_index()

types=['Liver', 'Kidney', 'Lip and Oral',
    'Tracheal, bronchus, and lung', 'Larynx',
    'Gallbladder and biliary tract', 'Malignant skin melanoma', 'Leukemia',
    'Hodgkin lymphoma', 'Multiple myeloma', 'Other neoplasms', 'Breast',
    'Prostate', 'Thyroid', 'Stomach', 'Bladder', 'Uterine', 'Ovarian',
    'Cervical', 'Brain and central nervous system', 'Non-Hodgkin lymphoma',
    'Pancreatic cancer', 'Esophageal cancer', 'Testicular', 'Nasopharynx',
    'Other pharynx', 'Colon and rectum', 'Non-melanoma skin',
    'Mesothelioma']

cancer_df['Total'] = cancer_df.loc[:,['Liver','Mesothelioma']].sum(axis = 1)

year=np.arange(2010,2020)
year

for c in country:
    year_total=list(cancer_df[cancer_df['Country']==c]['Total'])
    plt.figure(1,figsize=(10, 6))
    plt.plot(year,year_total,label=c,marker='o')
    plt.xlim([2010,2019])
    plt.ylim([486,980])
    plt.xticks(np.arange(2010,2020))
    plt.yticks(np.arange(450,1000,50))
    plt.title('Cancer attributed Deaths of 5 Countries (2010-2019)')
    plt.xlabel('Year')
    plt.ylabel('Total Cancer Deaths')

plt.legend(loc='best')
plt.show()

