import numpy as np

x = np.genfromtxt('/users/deeps/datasets/iris_train.csv',delimiter=",")
print("ORIGINAL ARRAY")
print(x)
rqrd_train_set = np.array([row for row in x  if 2.0 == row[4] or 1.0 == row[4] ])
print("\n Only Rows having Class = 1 and 2")
print(rqrd_train_set)
print("No of Rows Originally :"+ str(x.shape[0]))
print("No of rows selected :" +str(rqrd_train_set.shape[0]))
