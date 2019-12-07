**ECE143 Project Group 5 - Chronic Kidney Disease & Diabetes**
----
The goal of the project is to predict whether a patient is at risk of developing chronic
kidney disease, given certain biological information. Furthermore, we are interested in
seeing relationships between chronic kidney disease and other diseases due to similar
variables or factors. Based on the given data, our algorithm will 1. Assess their relative
risk of disease progression and 2. Recommend combative measures to decrease their
risk of disease development, if they are at risk. An example would be to have a patient
data inputted, then have our code assess whether they are at risk, which factors are
most likely contributing to disease progression and then propose a solution to mitigate
disease development.

**Members**

 -  Alexander Nguyen
 - Mohammad Zarei
 - Yangwenyi Jing
 - Donghwi Park
 
 **File Structure**
 - data/ - all raw csv files
 - functions/ - all function .py files
 - presentation/ - .pdf and .ppt of final presentation
 - ECE143_Group5_Jupyter.ipynb - Jupyter notebook containing how to produce visualizations
 - Project Proposal.pdf - .pdf of submmited project proposal

 
 

**Data**
----
Access data online

    UCI ML Repository: (https://archive.ics.uci.edu/ml/datasets/Chronic_Kidney_Disease)
    Dataset containing multiple variables e.g. blood pressure, age, glucose levels 
    and whether or not the patient has chronic kidney disease
    
    National Institute of Diabetes and Digestive Kidney Diseases:
    (https://www.kaggle.com/uciml/pima-indians-diabetes-database#diabetes.csv)
    Dataset collected from women in India. Measures certain variables 
    such as age, pregnancies, glucose levels and whether or not they have diabetes
     
    NYS Patient Characteristics Survey (PCS) - 2015:
    (https://www.kaggle.com/new-york-state/nys-patient-characteristics-survey-pcs-2015?fbclid=IwAR2TH9VdNzOyBEZWJdjzZyp69rNbEvk9unsW267QoWLQyfLw6c2yZ6Ky6-U)
    Dataset collected from patients in NYS. Listed living habits and diseases (diabetes, kidney diseases etc.), 
    age group (adult or child) etc.

    -> description: links given provide access to raw data

**Presentation**
------------

    -> location: ECE_143_project/presentations
    -> description: final presentation in both .ppt and .pdf format. open ppt format to access full animations (not shown via .pdf)


**Jupyter**
-------
	-> location: ECE143_Group5_Presentation_Jupyter.ipynb
    -> description: complete annotation of how user ran codes to generate figures in and out of presentation. 

**Proposal**
--------

    -> location: Project Proposal.pdf
    -> description: original proposal submitted for project description and goals

    

 

**3rd Party Modules**
-----------------

    Pandas
    NumPy
    Seaborn
    Matplotlib
    Sklearn

Import 3rd party modules in command line. For venn2, use pip install on Python shell or command shell.
    
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import matplotlib.font_manager
    from matplotlib_venn import venn2
    from sklearn.decomposition import PCA
    import os



**Visualization & How to run code**
-------------

Download data via github

    -> location:  ECE143_project/data/data1_ckd.csv 
    -> location:  ECE143_project/data/diabetes.csv
    -> location: ECE143_project/data/data3final.csv

	-> run code: read csv files with pd.read_csv('your directory with csv file')
	
	For CKD data set, modify column from object to str type

	e.g) your_variable.columns=['age','blood pressure','specific gravity','albumin','sugar','red blood cells','pus cell','pus cell clumps','bacteria','blood glucose','blood urea','serum creatinine','sodium','potassium','hemoglobin','packed cell volume','white blood cell count','red blood cell count','hypertension','diabetes','coronary artery disease','appetite','edema','anemia','class'] 

Run the following  on the diabetes data set to clean out the illogical data values. diab_data is the variable you chose to store the diabetes csv file.

    remove_nan = diab_data.replace('?', np.NaN)
    
    remove_zero = remove_nan.loc[remove_nan['Glucose'] != 0]
    remove_zero = remove_zero.loc[remove_zero['BloodPressure'] != 0]
    remove_zero = remove_zero.loc[remove_zero['SkinThickness'] != 0]
    remove_zero = remove_zero.loc[remove_zero['Insulin'] != 0]
    remove_zero = remove_zero.loc[remove_zero['BMI'] != 0]
    remove_zero = remove_zero.loc[remove_zero['DiabetesPedigreeFunction'] != 0]
    remove_zero = remove_zero.loc[remove_zero['Age'] != 0]
    
    remove_zero2 = remove_zero.iloc[:, :-1]
    
  Download all required functions  and import and unpackage all downloaded py files for future use. All created functions are located in ECE143_Project/functions folder in Git repository
  

    -> location: ECE143_Project/functions/
    -> run command: import function
				    from function, import*
				    

   Pie charts
   

    -> location: ECE143_Project/functions/create_pie.py
    -> run command: create_pie(your variable storing cleaned up CKD csv file, example above)
    -> description: this function takes the cleaned CKD data file (strs as columns) and generates pie charts given the input


Pie charts 2

    -> location: ECE143_Project/functions/create_pie2.py
    -> run command: create_pie2(your variable storing cleaned up CKD csv file, example above)
    -> description: this function takes the cleaned CKD data file (strs as columns) and generates pie charts given the input. What makes this function different is that it uses the diabetes feature in conjunction with observed ckd feature

Venn

    -> location: ECE143_Project/functions/create_venn.py
    -> run command: create_venn(your variable storing cleaned up CKD csv file, example above)
    -> description: this function takes the cleaned CKD data file (strs as columns) and generates a venn diagram between hypertension counts and diabetes counts

Heatmap

    -> location: ECE143_Project/functions/create_heat.py
    -> run command: create_heat(your variable storing cleaned up diabetes csv file, example above)
    -> description: this function takes the cleaned diabetes data file and generates heatmaps based on given input

PCA

    -> location: ECE143_Project/functions/do_pca.py
    -> run command: do_pca(your variable storing cleaned up CKD csv file, example above)
    -> description: this function takes the cleaned CKD data file (strs as columns) performs PCA to reduce dimensions for visualization and to observe clustering via scatter plots


Diabetes Percentages

    -> location: ECE143_Project/functions/gen_percentage_diab.py
    -> run command: 
    age_diab = gen_percentage_diab(data, object='Age', window=6)
    
    pregnancies_diab = gen_percentage_diab(data, object='Pregnancies', window=1)
    
    insulin_diab = gen_percentage_diab(data, object='Insulin', window=100)
        
    glucose_diab = gen_percentage_diab(data, object='Glucose', window=30)

    plot_diab_bar(age_diab, title='Diabetes vs Age', object='Age')
    
    plot_diab_bar(pregnancies_diab, title='Diabetes vs Pregnancies', object='Pregnancies')
    
    plot_diab_bar(insulin_diab, title='Diabetes vs Insulin', object='Insulin')
    
    plot_diab_bar(glucose_diab, title='Diabetes vs Glucose', object='Glucose')
                
    -> description: this function takes the cleaned diabetes data file and generates histograms with percentages between groups for age, glucose, insulin and pregnancies 
