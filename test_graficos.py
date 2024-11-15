import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Datos de ejemplo
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Gráfico simple con matplotlib
plt.plot(x, y)
plt.title("Gráfico de prueba con matplotlib")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()

# Gráfico con seaborn
sns.set(style="darkgrid")
tips = sns.load_dataset("tips")
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")
plt.title("Gráfico de prueba con seaborn")
plt.show()
