import yfinance as yf
import matplotlib.pyplot as plt

# Lista de empresas do setor de saúde
empresas_saude = [
    "HAPV3.SA", "QUAL3.SA", "RDOR3.SA", "ONCO3.SA", "DASA3.SA", "DASA11.SA", "AALR3.SA"
]

# Baixar dados históricos de todas as empresas
dados = yf.download(empresas_saude, start="2020-01-01", end="2024-12-31")

print(dados.head())

caminho_csv = r"C:\Users\User\Desktop\etl_acoes\dados_saude.csv"

dados.to_csv(caminho_csv)

print(f"Dados salvos em: {caminho_csv}")
