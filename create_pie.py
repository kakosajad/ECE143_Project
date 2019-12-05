# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:47:33 2019

@author: nguye
"""

def create_pie(csvfile,classv='ckd'):
    '''this function will create a pie chart from raw file modified with str
    as heading names. the csvfile is specifically for the CKD dataset (alData variable). the dataset contains
    features diabetes and class variable CKD. this function is generating pie charts with information from the
    class or CKD column only. otherwise, it will create a pie chart along the diabetes column
    
    param csvfile: this is the raw CKD csvfile
    param classv: 'ckd' to create pie for ckd classes. otherwise, create pie for diabetes
    
    type csvfile: pd.DataFrame
    type classv: str
    '''
    
    assert isinstance(csvfile,pd.DataFrame)
    assert isinstance(classv,str)
    assert 'class' in csvfile.columns
    assert 'diabetes' in csvfile.columns
    assert csvfile.shape==(400,25)
    assert classv=='ckd' or classv=='nockd'
    
    
    
    plt.rcParams['font.sans-serif'] = 'Arial'
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['text.color'] = '#383838'
    plt.rcParams['axes.labelcolor']= '#909090'
    plt.rcParams['xtick.color'] = '#909090'
    plt.rcParams['ytick.color'] = '#909090'
    plt.rcParams['font.size']=16
            
    color_palette_list = ['#ff7676','#76ffbb']
    
    if classv=='ckd':
        counts=csvfile['class'].value_counts()
    
        disease_counts=(sum(counts)-counts['notckd'])/(sum(counts))*100
        #calculate percentage of disease counts

        fig, ax = plt.subplots()     
           
        labels = ['Chronic Kidney Disease ', 
         'Non Chronic Kidney Disease']
        percentages = [disease_counts, 100-disease_counts]
        explode=(0.1,0)
        ax.pie(percentages, explode=explode,  
               colors=color_palette_list[0:2], autopct='%1.0f%%', 
               shadow=False, startangle=0,   
               pctdistance=1.2,labeldistance=.4)
        ax.axis('equal')
        ax.set_title("62% of Sampled Patients are CKD+",pad=20)
        ax.legend(labels=labels,frameon=False, bbox_to_anchor=(.8,0.8))
        
    else:
        counts=csvfile['diabetes'].value_counts()
        disease_counts=(sum(counts)-counts['no']-counts['\tno']-counts['?'])/(sum(counts)-counts['?'])*100
        fig, ax = plt.subplots()  
        labels = ['Diabetes', 
         'No Diabetes']
        percentages = [disease_counts, 100-disease_counts]
        explode=(0.1,0)
        ax.pie(percentages, explode=explode,  
               colors=color_palette_list[0:2], autopct='%1.0f%%', 
               shadow=False, startangle=0,   
               pctdistance=1.2,labeldistance=.4)
        ax.axis('equal')
        ax.set_title("34% of Sampled Patients are also Diabetes+",pad=20)
        ax.legend(labels=labels,frameon=False, bbox_to_anchor=(.8,0.8))
