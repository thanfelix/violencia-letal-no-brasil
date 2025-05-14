import pandas as pd
import matplotlib.pyplot as plt

## Importando base do IDHM
df_idhm = pd.read_excel("IDMH-Brasil.xlsx", engine='openpyxl')

## Importando base taxa de homicídios
df_homicidios = pd.read_csv("taxa-de-homicidios-de-jovens.csv", sep=";", encoding='ISO-8859-1')

## Tratando nomes de colunas, se necessário
df_homicidios.columns = [col.strip().lower() for col in df_homicidios.columns]  # remove espaços e padroniza
df_homicidios = df_homicidios.rename(columns={
    'perã­odo': 'Ano',
    'valor': 'Taxa',
    'cod': 'cod',
    'nome': 'UF'
})

## Lista estados da Região Norte renomeando de UF para nome
ufs_norte = ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO']
uf_para_estado = {
    'AC': 'Acre', 'AP': 'Amapá', 'AM': 'Amazonas',
    'PA': 'Pará', 'RO': 'Rondônia', 'RR': 'Roraima', 'TO': 'Tocantins'
}
## Preparando taxa de homicídios 2021
df_homicidios['Ano'] = df_homicidios['Ano'].astype(int)
homicidios_2021 = df_homicidios[df_homicidios['Ano'] == 2021].copy()
homicidios_2021['Estado'] = homicidios_2021['UF'].map(uf_para_estado)

## Preparando IDHM
df_idhm = df_idhm.rename(columns={'Territorialidades': 'Estado'})

idhm_2021 = df_idhm[['Estado', 'IDHM Ajustado à Desigualdade 2021']].copy()
idhm_2021 = idhm_2021.rename(columns={'IDHM Ajustado à Desigualdade 2021': 'IDHM'})

## Filtrando Região Norte
estados_norte = list(uf_para_estado.values())
idhm_norte = idhm_2021[idhm_2021['Estado'].isin(estados_norte)]
homicidios_norte = homicidios_2021[homicidios_2021['Estado'].isin(estados_norte)]

## Juntando as bases e plotando
df_merged = pd.merge(idhm_norte, homicidios_norte, on='Estado')

## Gráfico
plt.figure(figsize=(10, 6))
plt.scatter(df_merged['IDHM'], df_merged['Taxa'], color='green')

for _, row in df_merged.iterrows():
    plt.text(row['IDHM'] + 0.001, row['Taxa'], row['Estado'])

plt.title("Correlação entre IDHM e Taxa de Homicídios de Jovens (2021) - Região Norte")
plt.xlabel("IDHM")
plt.ylabel("Taxa de Homicídios de Jovens (por 100 mil)")
plt.grid(True)
plt.show()

## Calculando Correlação de Pearson

correlacao = df_merged['IDHM'].corr(df_merged['Taxa'])
print(f'Correlação de Pearson: {correlacao:.2f}')

## Regressão Linear Simples
plot = sns.lmplot(x='IDHM', y='Taxa', data=df_merged)
plot.fig.suptitle("Regressão Linear Simples entre o IDHM e a Taxa de Homicídios de Jovens na Região Norte (2021)", fontsize=12)
plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()



