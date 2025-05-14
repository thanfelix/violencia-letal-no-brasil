import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


dadosHomicidiosHomens = pd.read_csv("homicidios-de-jovens-homens.csv", sep=";", encoding='ISO-8859-1') # Importação do arquivo

dadosHomicidiosHomens.head() # Mostrar apenas as primeiras 5 entradas
dadosHomicidiosHomens # Mostrar apenas as 5 primeiras e 5 ultimas entradas

df.rename(columns={'perÃ­odo': 'ano'}, inplace=True)

## Lista estados da Região Norte renomeando de UF para nome
estados_norte = ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO']
uf_para_estado = {
    'AC': 'Acre', 'AP': 'Amapá', 'AM': 'Amazonas',
    'PA': 'Pará', 'RO': 'Rondônia', 'RR': 'Roraima', 'TO': 'Tocantins'
}

## Filtrando para mostrar apenas estados do Norte
df_norte['nome'] = df_norte['nome'].map(uf_para_estado)

## Plotando o gráfico
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_norte, x='ano', y='valor', hue='nome', marker="o")

plt.title('Homicídios de Homens Jovens na Região Norte (1979–2022)')
plt.xlabel('Ano')
plt.ylabel('Número de Homicídios')
plt.legend(title='Estado')
plt.grid(True)
plt.tight_layout()
plt.show()
