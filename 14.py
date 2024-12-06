import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('static\\titanic_train.csv')


print(data)
data.info()
print(data.describe(include='all'))
data['Age'].fillna(data['Age'].median(), inplace=True)
data['Embarked'].fillna('S', inplace=True)
data.info()


# 1
print('TASK 1:')
print(data.groupby('Sex').size())
print()
# 2
print('TASK 2:')
print(data.groupby('Sex')['Pclass'].describe())
print()
print(pd.crosstab(data['Pclass'], data['Sex']))
print()
# 3
print('TASK 3:')
anylize = pd.crosstab(data['Fare'], data['Sex'])
print(anylize['female'].mean())
print(anylize['male'].mean())
print()
# 4
print('TASK 4:')
print(data[data['Age'] < 30])
print(data[data['Age'] > 60])
print((data[data['Age'] < 30]['Survived'].sum() / 561) * 100, (data[data['Age'] > 60]['Survived'].sum() / 22) * 100)
print()
# 5
print('TASK 5:')
print(data.groupby('Sex')['Survived'].describe())
print()
# 6
print('TASK 6:')
names = data['Name'].apply(lambda x: x.split()[2])
print(names.value_counts().head())
print()
# 7 
print('TASK 7:')
print(data[data['Survived'] == 0]['Fare'].describe())
print(data[data['Survived'] == 1]['Fare'].describe())
print()
# 8
print('TASK 8:')
male = data[data['Sex'] == 'male']
female = data[data['Sex'] == 'female']
mean_male = male.pivot_table(['Age'], ['Pclass'], aggfunc='mean')
mean_female = female.pivot_table(['Age'], ['Pclass'], aggfunc='mean')
print(mean_male)
print(mean_female)
print()
#9 
# print('TASK 9:')
# sns.pairplot(data, hue='Survived',  vars=['Age'])
# sns.pairplot(data, hue='Survived',  vars=['Fare'])
# sns.pairplot(data, hue='Survived',  vars=['SibSp'])
# sns.pairplot(data, hue='Survived',  vars=['Parch'])
# sns.pairplot(data, hue='Embarked',  vars=['Survived'])
# plt.show()
# print()
# 10
# print('TASK 9:')
# sns.boxplot(x='Fare', y='Pclass', data=data)
# plt.show()
# print()
# 11
# print('TASK 10:')
# sns.countplot(hue='Survived', x='Pclass', data=data)
# plt.show()

# print()
# 12
# print('TASK 12:')

# sns.countplot(hue='Survived', x='Sex', data=data)
# plt.show()

# print()

#13
# print('TASK 11:')

# sns.pairplot(data, hue='Survived', vars=['Age'])
# plt.show()

# print()
