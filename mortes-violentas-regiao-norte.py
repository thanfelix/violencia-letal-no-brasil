import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

## Lista de estados da Região Norte
estados_norte = ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO']
uf_para_estado = {
    'AC': 'Acre', 'AP': 'Amapá', 'AM': 'Amazonas',
    'PA': 'Pará', 'RO': 'Rondônia', 'RR': 'Roraima', 'TO': 'Tocantins'
}

## Importando base de dados
df = pd.read_csv("mortes-violentas.csv", sep=";", encoding='ISO-8859-1')

## Tratando colunas
df.rename(columns={'perÃ­odo': 'ano'}, inplace=True)

## Filtrando apenas estados da região Norte
df_norte = df[df['nome'].isin(estados_norte)].copy()  # <-- agora sim o df_norte existe

## Trocando UF pelo nome completo
df_norte['nome'] = df_norte['nome'].map(uf_para_estado)

## Convertendo ano para inteiro
df_norte['ano'] = df_norte['ano'].astype(int)

## Plotar gráfico de linha
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_norte, x='ano', y='valor', hue='nome', marker="o")
plt.title('Mortes Violentas – Região Norte (1989–2022)')
plt.xlabel('Ano')
plt.ylabel('Número de Mortes')
plt.grid(True)
plt.tight_layout()
plt.show()
