import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "category": ["A", "B", "C", "D"] * 25,
    "x": np.random.rand(100),
    "y": np.random.rand(100),
    "value": np.random.randint(1, 100, 100)
})


# 7. Heatmap (тепловая карта)
plt.figure(figsize=(6, 4))
# Создание корреляционной матрицы для тепловой карты
corr_matrix = data.pivot_table(values="value", index="category", columns="category", aggfunc="mean")
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", cbar=True)
plt.title("Heatmap (Тепловая карта)")
plt.show()

# 8. Pairplot (матрица парных графиков)
pairplot_data = data[["x", "y", "value"]].assign(category=data["category"])
sns.pairplot(pairplot_data, hue="category", palette="husl")
plt.suptitle("Pairplot (Матрица парных графиков)", y=1.02)
plt.show()

# 9. Jointplot (график с комбинацией)
sns.jointplot(x="x", y="y", data=data, kind="scatter", hue="category", palette="coolwarm")
plt.suptitle("Jointplot (График с комбинацией)", y=1.02)
plt.show()