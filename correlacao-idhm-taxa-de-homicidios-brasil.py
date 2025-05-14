import pandas as pd
import matplotlib.pyplot as plt

## Importar base IDHM
df_idhm = pd.read_excel("IDMH-Brasil.xlsx", engine='openpyxl')

## Importar base taxa de homicídios
df_homicidios = pd.read_csv("taxa-de-homicidios-de-jovens.csv", sep=";", encoding='ISO-8859-1')

## Tratando colunas
df_homicidios.columns = [col.strip().lower() for col in df_homicidios.columns]
df_homicidios = df_homicidios.rename(columns={
    'perã­odo': 'Ano',
    'valor': 'Taxa',
    'cod': 'cod',
    'nome': 'UF'
})

# Mapeando de todos os estados
uf_para_estado = {
    'AC': 'Acre', 'AL': 'Alagoas', 'AP': 'Amapá', 'AM': 'Amazonas',
    'BA': 'Bahia', 'CE': 'Ceará', 'DF': 'Distrito Federal', 'ES': 'Espírito Santo',
    'GO': 'Goiás', 'MA': 'Maranhão', 'MT': 'Mato Grosso', 'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais', 'PA': 'Pará', 'PB': 'Paraíba', 'PR': 'Paraná',
    'PE': 'Pernambuco', 'PI': 'Piauí', 'RJ': 'Rio de Janeiro', 'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul', 'RO': 'Rondônia', 'RR': 'Roraima', 'SC': 'Santa Catarina',
    'SP': 'São Paulo', 'SE': 'Sergipe', 'TO': 'Tocantins'
}

## Preparando taxa de homicídios 2021
df_homicidios['Ano'] = df_homicidios['Ano'].astype(int)
homicidios_2021 = df_homicidios[df_homicidios['Ano'] == 2021].copy()
homicidios_2021['Estado'] = homicidios_2021['UF'].map(uf_para_estado)

## Preparando IDHM
df_idhm = df_idhm.rename(columns={'Territorialidades': 'Estado'})
idhm_2021 = df_idhm[['Estado', 'IDHM Ajustado à Desigualdade 2021']].copy()
idhm_2021 = idhm_2021.rename(columns={'IDHM Ajustado à Desigualdade 2021': 'IDHM'})

## Juntar os dados de todos os estados
df_merged = pd.merge(idhm_2021, homicidios_2021, on='Estado')

## Criando gráfico de dispersão
plt.figure(figsize=(12, 8))
plt.scatter(df_merged['IDHM'], df_merged['Taxa'], color='purple')

for _, row in df_merged.iterrows():
    plt.text(row['IDHM'] + 0.001, row['Taxa'], row['Estado'], fontsize=9)

plt.title("Correlação entre IDHM e Taxa de Homicídios de Jovens por Estado (2021)")
plt.xlabel("IDHM")
plt.ylabel("Taxa de Homicídios de Jovens (por 100 mil)")
plt.grid(True)
plt.tight_layout()
plt.show()


## Correlação de Pearson 
correlacao = df_merged['IDHM'].corr(df_merged['Taxa'])
print(f'Correlação de Pearson: {correlacao:.2f}')

## Regressão Linear
plot = sns.lmplot(x='IDHM', y='Taxa', data=df_merged)
plot.fig.suptitle("Regressão Linear Simples entre o IDHM e a Taxa de Homicídios de Jovens por Estado (2021)", fontsize=12)
plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()

