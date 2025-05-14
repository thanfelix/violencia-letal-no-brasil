import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

## Lista estados da Região Norte renomeando de UF para nome
estados_norte = ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO']
uf_para_estado = {
    'AC': 'Acre', 'AP': 'Amapá', 'AM': 'Amazonas',
    'PA': 'Pará', 'RO': 'Rondônia', 'RR': 'Roraima', 'TO': 'Tocantins'
}

## Importar a base de dados
df = pd.read_csv("homicidio-de-jovens-por-armas-de-fogo.csv", sep=";", encoding='ISO-8859-1')

## Tratamento de colunas com caracteres incorretos
df.rename(columns={'perÃ­odo': 'ano'}, inplace=True)

# Filtrar apenas os estados da região Norte
df_norte = df[df['nome'].isin(uf_para_estado)].copy()

# Mapear siglas para nomes completos dos estados
df_norte['nome'] = df_norte['nome'].map(uf_para_estado)

# Convertendo ano para inteiro
df_norte['ano'] = df_norte['ano'].astype(int)

# Plotando gráfico 
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_norte, x='ano', y='valor', hue='nome', marker="o")
plt.title('Homicídios de Jovens por Armas de Fogo – Região Norte (1979–2022)')
plt.xlabel('Ano')
plt.ylabel('Número de Homicídios')
plt.legend(title='Estado')
plt.grid(True)
plt.tight_layout()
plt.show()
