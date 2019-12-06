
'''
This function reads the 3rd data, and split this data into two group,
people who have CKD, and don't.
Final bar graph that this code is printing is about the realationships between other diseases
which could possibly realted with CKD
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager
from matplotlib_venn import venn2
#run in iPython shell or pip install matplotlib_venn into OS shell 
from sklearn.decomposition import PCA
import os
df = pd.read_csv('data3final.csv')

#emove all rows which contains unknown data.
data = df.replace(['UNKNOWN'], [None]).dropna(axis=0) 

#'Kidney Disease'?
Men_w_Kdis = data[(data['Age Group'] == 'ADULT') & (data['Sex'] == 'MALE') & (data['Kidney Disease'] == 'YES')]
Men_w_Kdis = Men_w_Kdis.append(Men_w_Kdis.eq('YES').mean(), ignore_index=True) # add new row : YES ratio
Men_w_Kdis = Men_w_Kdis.drop(columns=['Kidney Disease','Unnamed: 0', 'Age Group', 'Sex', 'Mental Illness' , 'Serious Mental Illness', 'Criminal Justice Status', 'Intellectual Disability', 'Autism Spectrum', 'Alcohol Related Disorder','Heart Attack','Stroke','Pulmonary Asthma','Alzheimer or Dementia','Liver Disease','Cancer','Smokes']) # remove unrealated column

Men_wo_Kdis = data[(data['Age Group'] == 'ADULT') & (data['Sex'] == 'MALE') & (data['Kidney Disease'] == 'NO')]
Men_wo_Kdis = Men_wo_Kdis.append(Men_wo_Kdis.eq('YES').mean(), ignore_index=True)
Men_wo_Kdis = Men_wo_Kdis.drop(columns = ['Kidney Disease','Unnamed: 0', 'Age Group', 'Sex', 'Mental Illness' , 'Serious Mental Illness', 'Criminal Justice Status', 'Intellectual Disability', 'Autism Spectrum', 'Alcohol Related Disorder','Heart Attack','Stroke','Pulmonary Asthma','Alzheimer or Dementia','Liver Disease','Cancer','Smokes'])




Women_w_Kdis = data[(data['Age Group'] == 'ADULT') & (data['Sex'] == 'FEMALE') & (data['Kidney Disease'] == 'YES')]
Women_w_Kdis = Women_w_Kdis.append(Women_w_Kdis.eq('YES').mean(), ignore_index=True)
Women_w_Kdis = Women_w_Kdis.drop(columns=['Kidney Disease','Unnamed: 0', 'Age Group', 'Sex', 'Mental Illness' , 'Serious Mental Illness', 'Criminal Justice Status', 'Intellectual Disability', 'Autism Spectrum', 'Alcohol Related Disorder','Heart Attack','Stroke','Pulmonary Asthma','Alzheimer or Dementia','Liver Disease','Cancer','Smokes'])

Women_wo_Kdis = data[(data['Age Group'] == 'ADULT') & (data['Sex'] == 'FEMALE') & (data['Kidney Disease'] == 'NO')]
Women_wo_Kdis = Women_wo_Kdis.append(Women_wo_Kdis.eq('YES').mean(), ignore_index=True)
Women_wo_Kdis = Women_wo_Kdis.drop(columns=['Kidney Disease','Unnamed: 0', 'Age Group', 'Sex', 'Mental Illness' , 'Serious Mental Illness', 'Criminal Justice Status', 'Intellectual Disability', 'Autism Spectrum', 'Alcohol Related Disorder','Heart Attack','Stroke','Pulmonary Asthma','Alzheimer or Dementia','Liver Disease','Cancer','Smokes'])


#read average YES rate from the dataframe.
Men_data = pd.concat([Men_w_Kdis.tail(1), Men_wo_Kdis.tail(1)], keys = ['with Kidney Disease','w/o Kidney Disease'])
Women_data =  pd.concat([Women_w_Kdis.tail(1), Women_wo_Kdis.tail(1)],keys = ['with Kidney Disease','w/o Kidney Disease'])







####Graphing code######
width = 0.45  # the width of the bars



Men_label = list(Men_data.columns)

x = np.arange(len(Men_label))  # the label locations


fig, ax = plt.subplots(figsize = (16,10))
rects1 = ax.bar(x - width/2, Men_data.iloc[0], width ,label='CKD Positive', color = '#ff7676')
rects2 = ax.bar(x + width/2, Men_data.iloc[1], width , label='CKD Negative',color = '#76ffbb') 



ax.set_ylabel('Disease percentage', fontsize = 20)
#ax.set_title('Diseases percentages of Men')
ax.set_xticks(x)
ax.set_xticklabels(Men_label)
plt.xticks(rotation='vertical', fontsize = 20)
ax.legend()

fig.tight_layout()
plt.box(False)
plt.show()
#plt.savefig('Men Diseases.png')
###########################


Women_label = list(Women_data.columns)

x = np.arange(len(Women_label))  # the label locations
#width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize = (16,10))
rects1 = ax.bar(x - width/2, Women_data.iloc[0], width, label='CKD Positive', color = '#ff7676')
rects2 = ax.bar(x + width/2, Women_data.iloc[1] ,width, label='CKD Negative', color = '#76ffbb') 

ax.set_ylabel('Disease percentage', fontsize = 20)

#ax.set_title('Diseases percentages of Women')
ax.set_xticks(x)
ax.set_xticklabels(Men_label)
plt.xticks(rotation='vertical', fontsize = 20)
ax.legend()

fig.tight_layout()
plt.legend(fontsize=30)
plt.box(False)
plt.show()