# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:49:42 2019

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
def do_pca(csvfile):
    '''this function will perform PCA on the input file, CKD raw data set. it will return 
    2 PCs and a scatter plot of the projected data points. it will also return a heatmap
    that informs the user how the principal component is distributed across features
    
    param csvfile: this is the raw csv for CKD data
    type csvfile: pd.DataFrame
    '''
    
    assert isinstance(csvfile,pd.DataFrame)
    
    assert 'class' in csvfile.columns
    assert 'diabetes' in csvfile.columns
    assert csvfile.shape==(400,25)

    
    alDataNaN=csvfile.replace('?',np.NaN)
    cleanData=alDataNaN.drop(alDataNaN.columns[5:9],axis=1)
    cleanData2=cleanData.drop(cleanData.columns[14:21],axis=1)
    #Hard coded to remove the columns that contain strings! These will later be 
    #written to binary values (e.g. normal is 0 and abnormal is 1). The reason
    #for this is that we do not want to perform data analysis on a mix of binary
    #and float values
    #https://stackoverflow.com/questions/45333530/pandas-drop-columns
    cleanwCKD=cleanData.drop(cleanData.columns[14:20],axis=1)

    new_data = cleanData2
    
    #append ckd information to new_data, this will be used to overlay data
    cleanwCKD_drop=cleanwCKD.dropna().values



    pca=PCA(n_components=2)
    pca.fit(new_data.dropna().values)
    #new_data is 400x14 (removed binary features)

    #Project onto 2 PCs
    projected=pca.transform(new_data.dropna().values)
    top2var=pca.explained_variance_ratio_[:2]

    print("original shape:   ", new_data.dropna().values.shape)
    print("transformed shape:", projected.shape)
    print(pca.explained_variance_ratio_)
    #Abnormally high variance captured in first PC.... Could be explained by
    #the very small number of features and the looking at histograms
    #show that a lot of the features are kind of useless

    #append class ckd to new_data2
    plt.figure(figsize=(14,7))
    #Overlay with CKD vs no CKD
    for i in range(len(new_data.dropna().values)):
        #go along the rows, checking if that row has ckd or no ckd
        if cleanwCKD_drop[i,-1] == 'ckd':  
            s1=plt.scatter(projected[i,0],projected[i,1],c='r',label = 'ckd',alpha=0.45,s=40)
        if cleanwCKD_drop[i,-1] == 'notckd':
            s2=plt.scatter(projected[i,0],projected[i,1],c='g',label = 'no ckd',alpha=0.45,s=40)

    plt.xlabel('First Principal Component',fontsize=20)
    plt.ylabel('Second Principal Component',fontsize=20)
    plt.legend((s1,s2),('CKD+','CKD-'),prop={'size':20})
    #plt.xticks([])
    #plt.yticks([])
    plt.box(False)
    plt.show()

#Find the top eigenvalues/features that capture most of the variance
#Compare to clear cut with histogram

#Find top 5 alleles for PC1
    num_genes=10
    v_sk=pca.components_.T
    top_PC=v_sk[:,0]
    abs_weight=np.abs(top_PC)
    weight_cutoff=sorted(abs_weight)[-num_genes]
    gene_positions=np.where(abs_weight>=weight_cutoff)[0]

    for position in gene_positions:
        gene_tag=new_data.columns[position]
        gene_weight=top_PC[position]
        print (gene_tag, gene_weight)
    

    #make sure to capture correct names -> strings for column titles
    plt.matshow(pca.components_,cmap='Greens')
    plt.yticks([0,1],['1st Comp','2nd Comp'],fontsize=16)
    plt.colorbar()
    plt.xticks(range(len(cleanData2.columns)),cleanData2.columns
    ,rotation=65,ha='left')
    #plt.tight_layout()
    plt.show()
