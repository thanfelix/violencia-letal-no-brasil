import pandas as pd

# Caminho para o arquivo Excel
arquivo = 'IDMH-Brasil.xlsx'

# Importando 
df = pd.read_excel(arquivo, sheet_name='Worksheet')

# Remove a linha "Brasil" mantendo apenas os estados
df_estados = df[df["Territorialidades"] != "Brasil"]

# Selecionando os valores de IDHM do ano de 2021
idhm_2021 = df_estados["IDHM Ajustado à Desigualdade 2021"]

# Calculando a moda, média e mediana
moda = idhm_2021.mode().values
media = idhm_2021.mean()
mediana = idhm_2021.median()

# Exibindo os resultados
print("Moda:", moda)
print("Média:", round(media, 4))
print("Mediana:", mediana)
