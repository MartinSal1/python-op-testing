import pandas as pd

headers = ['name', 'title', 'department','A','B','C', 'salary','D' ]
chicago_data = pd.read_csv('chicago-salaries/data-salaries.csv', header=0,names=headers)
""" Name,Job Titles,Department,A,B,C,Annual Salary,D """
chicago_data.drop(['A','B','C','D'],axis=1,inplace=True)
print(chicago_data.head())