""" for data analysis like mysql, excel"""
import pandas as pd #one dimensional

s = pd.Series([1, 3, 5, 7, 9])
s2 = pd.Series([1, 3, 5, 7, 9], index=['a', 'b', 'c', 'd', 'e'])
# print(s2['a'])

dic = {"Houston": 1000, "NH": 2000, "Washington": 3000, "DC":8999}
s3 = pd.Series(dic)
# print(dic)
print(dic["Houston"])
print(s3[s3 > 1000])
print(s3 < 1000)
s3["Houston"] = 30000
s3[s3 > 1000] = 99900

# print("Houston" in dic)
print()
print(s3/100)

print(s3.isnull())

print("data framing")
data = {'Books': ["A","B","C","D"],
        'Authors': ["F","G","H","I"],
        'Price': [100, 200, 300, 400],
        'BookMark': [100, 200, 300, 40]}

info = pd.DataFrame(data, columns=['Books', 'Authors', 'Price', 'BookMark'])
print(info)



a = True
value = 1 if a else 0
# print(value)

name = "marty"
age = 44
# print('Name: {name} Age: {age}')
# print('Name: {name} Age: {age}'.format())#formatting strings
