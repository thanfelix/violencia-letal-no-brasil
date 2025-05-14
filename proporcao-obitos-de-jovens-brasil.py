import pandas as pd
import matplotlib.pyplot as plt

## Importando a base
arquivo = 'proporcao-bitos-por-arma-de-fogo-de-jovens-ao-total-de-bitos-por-arma-de-fogo.csv'
df = pd.read_csv(arquivo, sep=';', encoding='utf-8')

## Tratando colunas
df = df.rename(columns={
    'período': 'Ano',
    'valor': 'Proporção',
    'cod': 'cod',
    'nome': 'UF'
})

## Filtrando apenas o ano de 2021
df_2021 = df[df['Ano'] == 2021]

## Colocando em ordem decrescente
df_2021 = df_2021.sort_values(by='Proporção', ascending=False)

## Plotando o gráfico
plt.figure(figsize=(12, 6))
plt.bar(df_2021['UF'], df_2021['Proporção'], color='turquoise')
plt.title('Proporção de Óbitos de Jovens por arma de fogo \nem Relação ao Total - Brasil (2021)', fontsize=14)
plt.xlabel('Estado (UF)')
plt.ylabel('Proporção (%)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()