import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn import datasets, linear_model

# ['data', 'target', 'frame', 'DESCR', 'feature_names',
# 'data_filename', 'target_filename', 'data_module']

diabetes=datasets.load_diabetes()
# print(diabetes.data)

# # to convert datasets into dataframe
df=pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
# print(df)

# # to make csv file from dataframe
# df.to_csv(r'C:\Users\utkarsh gupta\OneDrive\Desktop\data.csv')

# dia=diabetes.DESCR
# print(dia)
# print(diabetes.feature_names)
# print(type(df))
# print(diabetes.keys())
# dia=diabetes.data
# print(diabetes.target)

diax=diabetes.data
print(type(diax))
# diax=diabetes.data[:,np.newaxis,2]
# here function of np.newaxis is to represent data in new line

# diax=diabetes.data[:, 2]
# here data will store in the form of 1-D array

'''
print(diax)
print(len(diax))
print(diabetes,'\n')
print(dia)
'''

dia_x_train=diax[:]
# print(dia_x_train)
# dia_x_train=diax[:30]
dia_x_test=diax[-30:]
# print(dia_x_test)

# print(diax[:-10])

diay=diabetes.target
# print(diay)

# print(diay)
# print(len(diay))

dia_y_train=diay[:]
# dia_y_train=diay[:30]
dia_y_test=diay[-30:]

model1=linear_model.LinearRegression()
model1.fit(dia_x_train,dia_y_train)

diabetes_pridict=model1.predict(dia_x_test)

print("mean square error is:",mean_squared_error(dia_y_test,
                                                 diabetes_pridict))

print("weights:", model1.coef_)
print("intercept:", model1.intercept_)

# plt.scatter(dia_x_test,dia_y_test)
# plt.plot(dia_x_test,diabetes_pridict)
# plt.show()

# ean square error is: 3563.5259785449803
# weights: [[458.15762507]]
# intercept: [144.70176785]