import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('static/youth_smoking_drug_data_10000_rows_expanded.csv')
data['Age_Group'] = data['Age_Group'].apply(lambda x: 80 if x[-1] == '+' else int(x[-2:]))
data["Drug_Experimentation"] = data["Drug_Experimentation"].apply(lambda x: round(x))
data["Smoking_Prevalence"] = data["Smoking_Prevalence"].apply(lambda x: round(x))
data['Socioeconomic_Status'] = data['Socioeconomic_Status'].apply(lambda x: 3 if x == 'High' else 2 if x == 'Middle' else 1)
# Зависимость гендера и склонности к экспериментам с наркотиками
smoke = data.pivot_table(['Drug_Experimentation'], ['Gender'], aggfunc='mean')
print(smoke)


print('AAAAAA')
print(data['Smoking_Prevalence'].describe())
# Зависимость возрастной группы и склонности к экспериментам с наркотиками
sns.pairplot(data=data, hue = 'Drug_Experimentation',  vars = ['Age_Group'])
plt.show()


# Зависимость социально-экономического статуса и склонности к экспериментам с наркотиками
sns.histplot(x="Socioeconomic_Status", hue="Drug_Experimentation" ,data=data, legend=False)
plt.show()

# Зависимость родительского надзора и семейного прошлого
test = data[data['Parental_Supervision'].isin([1, 10])]
sns.pairplot(vars = ["Drug_Experimentation"], hue = 'Parental_Supervision',data=test)
plt.show()
sns.pairplot(vars = ["Smoking_Prevalence"], hue = 'Parental_Supervision',data=test)
plt.show()

# Зависимость социально-экономического статуса и склонности к экспериментам с наркотиками c выводом возрастной группы
sns.barplot(data=data, x = "Age_Group", y = "Drug_Experimentation", hue = "Socioeconomic_Status")
plt.show()

# Зависимость ментального здоровья и склонности к экспериментам с наркотиками
sns.lineplot(data=data, x = "Mental_Health", y = "Drug_Experimentation")
plt.show()

# Зависимость медиа-влияния и возрастной группы

# sns.pairplot(data=data,hue = "Media_Influence", vars=["Age_Group"])
# plt.show()


# Создание столбца типа зависимостей у группы лиц

new_d = data.copy()
new_d['Drug_Experimentation'] = new_d['Drug_Experimentation'].apply(lambda x: round(x * 5/7))

# Выясняем среднюю разницу между коэффициентами склонностей к наркотикам и к курению
new_d['Diff'] = new_d.apply(lambda x: abs(x['Smoking_Prevalence'] - x['Drug_Experimentation']), axis=1)
# print(new_d['Diff'].mean())

# Создаём новый столбец с типомами зависимостей, всего их - 4(Курение, наркотики, равные и преимущественно здоровые)
new_d["Addiction_Type"] = new_d.apply(lambda x: "Smoking" if ((x['Smoking_Prevalence'] - x['Drug_Experimentation']) > 15) else "Drugs" if ((x['Drug_Experimentation'] - x['Smoking_Prevalence']) > 15) else "Healty" if ((x['Smoking_Prevalence'] < 10) and (x['Drug_Experimentation'] < 10)) else "Equal", axis=1)
# print(new_d.groupby('Addiction_Type').size())
data["Addiction_Type"] = new_d["Addiction_Type"]

# sns.pairplot(hue = 'Addiction_Type', vars = ["Age_Group"], data=data)
# plt.show()

# Ещё один столбец - качество жизни
data['Quality_Of_Life'] = data.apply(lambda x: 'Excellent' if ((x['Mental_Health'] >= 8) and (x['School_Programs'] == 'Yes')) else 'Low' if ((x['Mental_Health'] < 5) and (x['School_Programs'] == 'No')) else 'Mid', axis=1)
print(data.groupby('Quality_Of_Life').size())

test1 = data[data['Quality_Of_Life'] == 'Low']
test2 = data[data['Quality_Of_Life'] == 'Excellent']
print(f'Low: Smoking_Prevalence {test1['Smoking_Prevalence'].mean()}, Drug_Experimentation {test1['Drug_Experimentation'].mean()}, Peer_Influence {test1['Peer_Influence'].mean()}, Parental_Supervision {test1['Parental_Supervision'].mean()}')
print(f'High: Smoking_Prevalence {test2['Smoking_Prevalence'].mean()}, Drug_Experimentation {test2['Drug_Experimentation'].mean()}, Peer_Influence {test2['Peer_Influence'].mean()}, Parental_Supervision {test2['Parental_Supervision'].mean()}')

