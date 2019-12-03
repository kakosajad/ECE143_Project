import pandas as pd
from collections import defaultdict

def split_count(x):
    """
    This function returns counts the reasons for using python in the dataset
    and shows in a data frame
    
    """
    assert isinstance(x, pd.core.series.Series) or isinstance(x, pd.core.frame.DataFrame)
    x=x['Is there anything in particular you want to use Python for?']

    dic=defaultdict(int)

    for row in x: 
        subjList = row.split(',')
        
        
        for subj in subjList:
            dic[subj.strip()] +=1
    df=pd.DataFrame.from_dict(dic,orient='index')
    df.columns= (['count'])
    return df.sort_values(by=['count'])



#if __name__ == "__main__":
#    ""
#    data = pd.read_csv("survey_data.csv")
#    print(split_count(data))
