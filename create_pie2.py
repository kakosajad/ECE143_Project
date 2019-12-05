# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:48:24 2019

@author: nguye
"""

def create_pie2(csvfile,ckd=False):
    '''this function will create a pie chart for patients that are ckd+ and diabetes+.
    essentially, it will extract the ckd class values and then search for values where
    there are diabetes+ feature values. otherwise, it will generate and extract nockd class values
    and then plot the diabetes feature values into a pie chart
    
    param csvfile: this is the raw CKD csvfile
    param ckd: True to create pie for ckd classes. otherwise, create pie for nockd values
    
    type csvfile: pd.DataFrame
    type ckd: bool
    '''
    
    assert isinstance(csvfile,pd.DataFrame)
    assert isinstance(ckd,bool)
    assert 'class' in csvfile.columns
    assert 'diabetes' in csvfile.columns
    assert csvfile.shape==(400,25)
    assert ckd==False or ckd==True
    
    plt.rcParams['font.sans-serif'] = 'Arial'
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['text.color'] = '#383838'
    plt.rcParams['axes.labelcolor']= '#909090'
    plt.rcParams['xtick.color'] = '#909090'
    plt.rcParams['ytick.color'] = '#909090'
    plt.rcParams['font.size']=16
            
    color_palette_list = ['#ff7676','#76ffbb']
    
    alDataNaN=csvfile.replace('?',np.NaN)
    
    venn=alDataNaN[['class','diabetes']]
    venn=venn.dropna()
    
    if ckd==False:
        notckd=venn.loc[venn['class'] == 'notckd']
        num_no=notckd['diabetes'].value_counts()
        store=num_no['no']
        
        disease_counts=0
        #all are chosen to not have CKD
    
        fig, ax = plt.subplots()  
        labels = ['CKD- Diabetes+', 
                  'CKD- Diabetes-']
        percentages = [disease_counts, store/len(notckd) *100]
        explode=(0.1,0)
        ax.pie(percentages, explode=explode,  
               colors=color_palette_list[0:2], autopct='%1.0f%%', 
               shadow=False, startangle=0,   
               pctdistance=1.2,labeldistance=.4)
        ax.axis('equal')
        ax.set_title("100% of CKD- Patients are also Diabetes-")
        ax.legend(labels=labels,frameon=False, bbox_to_anchor=(.8,0.8))
    
    else:
        ckd=venn.loc[venn['class'] != 'notckd']
        num_no=ckd['diabetes'].value_counts()
        store=num_no['no']+num_no['\tno']
        
        fig, ax = plt.subplots()  
        labels = ['CKD+ Diabetes+', 
                  'CKD+ Diabetes-']
        percentages = [(len(ckd)-store)/len(ckd) *100, store/len(ckd) *100]
        explode=(0.1,0)
        ax.pie(percentages, explode=explode,  
               colors=color_palette_list[0:2], autopct='%1.0f%%', 
               shadow=False, startangle=0,   
               pctdistance=1.1,labeldistance=.2)
        ax.axis('equal')
        ax.set_title("55% of CKD+ Patients are also Diabetes+",pad=20)
        ax.legend(labels=labels,frameon=False, bbox_to_anchor=(.8,0.8))