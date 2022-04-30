import pandas as pd
from sklearn.model_selection import train_test_split
import wittgenstein as lw
from sklearn.metrics import precision_score, recall_score


prefix = 20
rip_df = pd.read_csv('data/dataset/bpic/bpic2017/prefix'+str(prefix)+'/BPICinput_preprocessed.csv')
rip_df = rip_df.sample(n=5000)
#rip_df = rip_df.drop('Variant index', axis = 1)

rip_df_train, rip_df_test = train_test_split(rip_df,test_size=0.3,random_state=rndst)

rip_X_train = rip_df_train.drop(['Case ID', 'Accepted'], axis = 1)
rip_y_train = rip_df_train['Accepted']
rip_X_test = rip_df_test.drop(['Case ID', 'Accepted'], axis = 1)
rip_y_test = rip_df_test['Accepted']


ripper_clf = lw.RIPPER() # Or irep_clf = lw.IREP() to build a model using IREP


a = []
p = []
r = []
f = []

for rndst in range(0,5):

    ripper_clf.fit(rip_df_train, class_feat = 'Accepted') # Or pass X and y data to .fit
    
    rule = ripper_clf.ruleset_
    print('Rule : ', rule)
        
    acc = ripper_clf.score(rip_X_test, rip_y_test)
    precision = ripper_clf.score(rip_X_test, rip_y_test, precision_score)
    recall = ripper_clf.score(rip_X_test, rip_y_test, recall_score)
    f1 = 2*precision*recall/(precision+recall)
    
    a.append(acc)
    p.append(precision)
    r.append(recall)
    f.append(f1)
    
print(f'precision: {sum(p)/len(p)} recall: {sum(r)/len(r)} f1 score: {sum(f)/len(f)} accuracy: {sum(a)/len(a)}')
