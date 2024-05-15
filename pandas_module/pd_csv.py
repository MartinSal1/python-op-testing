import pandas as pd

data = pd.read_csv('pandas_module/sample.csv')
# print(data)

data2 = pd.read_csv('pandas_module/sample.csv', names=["FirstName","Dept","Job", "pay"],header=0)
# print(data2)
data3 = pd.read_csv('pandas_module/sample.csv',usecols=[0,1])
# print(data3)

new_CSV_file = pd.read_csv('pandas_module/sample.csv', usecols=[0,1,2,3])
new_CSV_file.to_csv("pandas_module/SampleTwo.csv")
print(new_CSV_file)
