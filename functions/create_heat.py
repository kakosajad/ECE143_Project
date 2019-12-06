# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:49:23 2019

@author: nguye
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager
from matplotlib_venn import venn2
#run in iPython shell or pip install matplotlib_venn into OS shell 
from sklearn.decomposition import PCA
import os
def create_heat(csvfile,overlay='ckd',outcome='pos'):
    '''generate heatmap for given csv file. this will generate a heatmap for either the ckd
    or diabetes data set. furthermore, it will create a heatmap for the diseased+ or diseased-
    feature values.
    
    param csvfile: this is the raw CKD csvfile/ raw diabetes csvfile
    param overlay: this is to specify whether it is the CSV or diabetes data file.
                   if anything but ckd is mentioned, it will generate for diabetes
    param outcome: generate figures for diseased+ if given pos, otherwise generate  
                    figures for diseased free (diseased-)
    
    type csvfile: pd.DataFrame
    type overlay: str
    type outcome: str
    '''
    
    assert isinstance(csvfile,pd.DataFrame)
    assert isinstance(overlay,str)
    assert isinstance(outcome,str)

    assert overlay=='ckd' or overlay=='d'
    assert outcome=='pos' or outcome=='neg'

    
    
    alDataNaN=csvfile.replace('?',np.NaN)
    
    if overlay=='ckd':
        if outcome=='pos':
        
            nockd=alDataNaN.loc[alDataNaN['class'] =='notckd']
            #only store nockd values
            
            cleanData=nockd.drop(alDataNaN.columns[5:9],axis=1)
            
        
            cleanData2=cleanData.drop(cleanData.columns[14:21],axis=1)
            #Hard coded to remove the columns that contain strings! These will later be 
            #written to binary values (e.g. normal is 0 and abnormal is 1). The reason
            #for this is that we do not want to perform data analysis on a mix of binary
            #and float values
            #https://stackoverflow.com/questions/45333530/pandas-drop-columns
        
    
            cleanData2=cleanData2.dropna()
            #dropNaN values
    
            corr=cleanData2.astype('float64').corr()
    
    

            sns.heatmap(corr)
    
       
        #create if else statement 
        else:
            dandckd=alDataNaN.loc[alDataNaN['class']!='notckd']
            dandckd=dandckd.loc[dandckd['diabetes'] !='no']
            dandckd=dandckd.loc[dandckd['diabetes'] !='\tno']  
    
            cleanData=dandckd.drop(alDataNaN.columns[5:9],axis=1)


            cleanData2=cleanData.drop(cleanData.columns[14:21],axis=1)
        #Hard coded to remove the columns that contain strings! These will later be 
        #written to binary values (e.g. normal is 0 and abnormal is 1). The reason
        #for this is that we do not want to perform data analysis on a mix of binary
        #and float values
        #https://stackoverflow.com/questions/45333530/pandas-drop-columns
        
    
            cleanData2=cleanData2.dropna()
    #dropNaN values
    
            corr=cleanData2.astype('float64').corr()
    
    
    else:
       #for diabetes data file
       
         remove_nan=csvfile.replace('?',np.NaN)
     
         remove_zero=remove_nan.loc[remove_nan['Glucose'] !=0]
         remove_zero=remove_zero.loc[remove_zero['BloodPressure']!=0]
         remove_zero=remove_zero.loc[remove_zero['SkinThickness']!=0]
         remove_zero=remove_zero.loc[remove_zero['Insulin']!=0]
         remove_zero=remove_zero.loc[remove_zero['BMI']!=0]
         remove_zero=remove_zero.loc[remove_zero['DiabetesPedigreeFunction']!=0]
         remove_zero=remove_zero.loc[remove_zero['Age']!=0]
     
    
         remove_zero2=remove_zero.iloc[:,:-1]
     
         wdiab=remove_zero2.loc[remove_zero['Outcome']==1]
         wodiab=remove_zero2.loc[remove_zero['Outcome']==0]
     
         if outcome=='pos':
            corr=wdiab.astype('float64').corr()
             
     
            mask = np.zeros_like(corr)
            mask[np.triu_indices_from(mask)] = True
            plt.figure(figsize=(10,10))
            sns.set(font_scale=1.5)
            with sns.axes_style("white"):
                ax=sns.heatmap(corr,mask=mask,xticklabels=corr.columns,yticklabels=corr.columns,annot=True,fmt='.3f',linewidths=.1,square=True,cmap='Reds')
            ax.collections[0].colorbar.set_label('Correlation Coefficient')
            ax.set_title('Diabetes+',fontsize=30)
             
         else:
             corr=wodiab.astype('float64').corr()
             
     
             mask = np.zeros_like(corr)
             mask[np.triu_indices_from(mask)] = True
             plt.figure(figsize=(10,10))
             sns.set(font_scale=1.5)
             with sns.axes_style("white"):
                ax=sns.heatmap(corr,mask=mask,xticklabels=corr.columns,yticklabels=corr.columns,annot=True,fmt='.3f',linewidths=.1,square=True,cmap='Greens')
             ax.collections[0].colorbar.set_label('Correlation Coefficient')
             ax.set_title('Diabetes-',fontsize=30)