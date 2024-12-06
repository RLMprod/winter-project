import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('static/youth_smoking_drug_data_10000_rows_expanded.csv')

smoke = data.pivot_table(['Drug_Experimentation'], ['Gender'], aggfunc='mean')
print(smoke)

age_an = data.copy()
age_an['Age_Group'] = age_an['Age_Group'].apply(lambda x: 80 if x[-1] == '+' else int(x[-2:]))
print(age_an)

sns.pairplot(data=age_an, hue = 'Drug_Experimentation',  vars = ['Age_Group'])

print()


sns.pairplot(data, hue='Gender',  vars=['Peer_Influence'])
plt.show()