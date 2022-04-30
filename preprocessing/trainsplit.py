import pandas as pd

import sys
import os
from functools import reduce
from sklearn.model_selection import train_test_split

from tqdm import tqdm



for prefix in tqdm(range(5,41,5)):
    dir_path = 'data/dataset/bpic/bpic2017'
    df = pd.read_csv(dir_path+'/prefix'+str(prefix)+'/BPICinput_preprocessed.csv')
    for rndst in range(0,1):
        df_train,df_test = train_test_split(df,test_size=0.3,random_state=rndst) #Random State 0,1,2,3,4,5,6,7,8,9 10 numbers
        filename = dir_path+'/prefix'+str(prefix)+'/'
        df_train.to_csv(filename+'train_rndst'+str(rndst)+'.csv',index=False)
        df_test.to_csv(filename+'test_rndst'+str(rndst)+'.csv',index=False)

