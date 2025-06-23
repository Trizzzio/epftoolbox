from epftoolbox.data import read_data
from epftoolbox.data import DataScaler

PJM_train, PJM_test=read_data('.','PJM', begin_test_date='01-01-2016', end_test_date='01-10-2016')
NP_train, NP_test=read_data('.','NP', begin_test_date='01-01-2016', end_test_date='01-10-2016')


print(PJM_train.head())
print(PJM_test.head())
print(PJM_train.shape)


print(NP_train.head())
print(NP_test.head())
print(NP_train.shape)

scaler = DataScaler('Norm')


