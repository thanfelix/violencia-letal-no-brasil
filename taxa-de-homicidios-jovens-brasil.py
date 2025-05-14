import pandas as pd
import matplotlib.pyplot as plt



## Importar o base 
df_homicidios = pd.read_csv("taxa-de-homicidios-de-jovens.csv", sep=";", encoding='ISO-8859-1')

## Tratar colunas
df_homicidios.columns = [col.strip().lower() for col in df_homicidios.columns]  # remove espaços e padroniza
df_homicidios = df_homicidios.rename(columns={
    'perã­odo': 'Ano',
    'valor': 'Taxa',
    'cod': 'cod',
    'nome': 'UF',
    'uf_para_estado': {
    'AC': 'Acre', 'AL': 'Alagoas', 'AP': 'Amapá', 'AM': 'Amazonas',
    'BA': 'Bahia', 'CE': 'Ceará', 'DF': 'Distrito Federal', 'ES': 'Espírito Santo',
    'GO': 'Goiás', 'MA': 'Maranhão', 'MT': 'Mato Grosso', 'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais', 'PA': 'Pará', 'PB': 'Paraíba', 'PR': 'Paraná',
    'PE': 'Pernambuco', 'PI': 'Piauí', 'RJ': 'Rio de Janeiro', 'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul', 'RO': 'Rondônia', 'RR': 'Roraima', 'SC': 'Santa Catarina',
    'SP': 'São Paulo', 'SE': 'Sergipe', 'TO': 'Tocantins'}

})

## Definindo ano de análise
df_homicidios['Ano'] = df_homicidios['Ano'].astype(int)
homicidios_2021 = df_homicidios[df_homicidios['Ano'] == 2021].copy()

## Filtrando apenas o ano de 2021
df_2021 = df_homicidios[df_homicidios['Ano'] == 2021]

## Colocando em ordem decrescente
df_2021 = df_2021.sort_values(by='Taxa', ascending=False)

## Criando o gráfico de barras
plt.figure(figsize=(14, 6))
plt.bar(df_2021['UF'], df_2021['Taxa'], color='tomato')

## Títulos e rótulos
plt.title('Taxa de Homicídios de Jovens por 100 mil Habitantes – Brasil (2021)', fontsize=14)
plt.xlabel('Estados (UF)', fontsize=12)
plt.ylabel('Taxa de Homicídios', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)

## Mostrando o gráfico
plt.tight_layout()
plt.show()
