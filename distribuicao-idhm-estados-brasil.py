import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importando
df = pd.read_excel('IDMH-Brasil.xlsx', sheet_name='Worksheet')
df_estados = df[df["Territorialidades"] != "Brasil"]
idhm_2021 = df_estados["IDHM Ajustado à Desigualdade 2021"]

# Calculando média e mediana
media = idhm_2021.mean()
mediana = idhm_2021.median()

# plotando
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.histplot(idhm_2021, kde=True, bins=10, color="skyblue", edgecolor="black")

# Linhas de média e mediana
plt.axvline(media, color='red', linestyle='--', label=f'Média: {media:.3f}')
plt.axvline(mediana, color='green', linestyle='-.', label=f'Mediana: {mediana:.3f}')

# Títulos e rótulos
plt.title("Distribuição do IDHM Ajustado à Desigualdade - Estados do Brasil (2021)")
plt.xlabel("IDHM")
plt.ylabel("Frequência")
plt.legend()
plt.tight_layout()
plt.show()