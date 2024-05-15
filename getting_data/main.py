import pandas as pd
# data sets
# https://grouplens.org/datasets/movielens/

users = pd.read_csv('ml-100k/u.user', sep = "|", names = ['user_id', 'age', 'gender', 'occupation', 'zip_code'])
# print(users.head())
# print(users.tail(50))

print(users[:])
print()

data_col = ['gender','zip_code']
print(users[data_col].head())

print(users.age > 50)
print()

print(users[(users.gender == "M") & (users.age > 50)].head())
print(users[(users.gender == "F") | (users.occupation == "writer")].head(10))
print()

print(users.dtypes)
print(users.describe())
print()

users.set_index('user_id',inplace=True)
print(users[0:5])
print()

print(users.iloc[[3,4,5]])

print()
data_let = pd.DataFrame({'user_id':['A','B','C'],'age':[20,40,60]}, index=['a','b','c'])
print(data_let.loc['a'])
print()
print(data_let[:'b'])

print("joining")

# left join, right join, inner join, outer join
data_set_one = pd.DataFrame({'key': range(5), 'element':['a','b','c','d','e']})
data_set_two = pd.DataFrame({'key': range(3,7), 'element':['g','h','i','j']})
# riht is to keep the values of the left untouched
print(pd.merge(data_set_one,data_set_two,on='key',how='left'))

print(pd.concat([data_set_one,data_set_two]))
print(pd.concat([data_set_one,data_set_two],axis=1))