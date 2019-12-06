# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:48:42 2019

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
def create_venn(csvfile):
    '''this function will create a venn diagram between the two classes, hypertension and diabetes
    CKD class is not chosen because there exists no instances of values of no ckd with values of
    diabetes +. furthermore hypertension is a common condition in conjunction with ckd
    prognosis
    
    param csvfile: this is the raw CKD csvfile
 
    type csvfile: pd.DataFrame
    
    '''
    
    assert isinstance(csvfile,pd.DataFrame)
    assert 'class' in csvfile.columns
    assert 'diabetes' in csvfile.columns
    assert 'hypertension' in csvfile.columns
    assert csvfile.shape==(400,25)
    
    alDataNaN=csvfile.replace('?',np.NaN)
    
    venn=alDataNaN[['hypertension','diabetes']]
    venn=venn.dropna()
    
    ht_neg=venn.loc[venn['hypertension'] != 'yes']
    #separate/extract patients that are ht-   
    ht_neg_counts=ht_neg['diabetes'].value_counts()
    #count # of results in diabetes column
    ht_neg_d_pos=ht_neg_counts['yes']
    ## of ht-,d+ patients
    
    ht_pos=venn.loc[venn['hypertension'] == 'yes']
    ht_pos_counts=ht_pos['diabetes'].value_counts()
    ht_pos_d_neg=ht_pos_counts['no']
    
    ht_pos_d_pos=sum(ht_pos_counts)-ht_pos_d_neg
    
    plt.figure(figsize=(14,7))
    v=venn2(subsets=(ht_neg_d_pos,ht_pos_d_neg,ht_pos_d_pos))
    
    v.get_patch_by_id('100').set_color('#ff7676')
    v.get_patch_by_id('010').set_color('#2aff96')
    
    plt.title("Diabetes+ and Hypertension+ Relationship")
    plt.annotate('Diabetes+ Only', xy=v.get_label_by_id('100').get_position() - np.array([0, 0.05]), xytext=(-70,-70),
             ha='center', textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5', fc='gray', alpha=0.1),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5',color='gray'))
    plt.annotate('Hypertension+ Only', xy=v.get_label_by_id('010').get_position() - np.array([0, -0.1]), xytext=(70,70),
         ha='center', textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5', fc='gray', alpha=0.1),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5',color='gray'))   
    
    plt.show()