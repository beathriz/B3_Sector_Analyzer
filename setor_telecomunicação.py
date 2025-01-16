import yfinance as yf
import matplotlib.pyplot as plt

# Lista de empresas do setor de telecomunicações
empresas_telecomunicacoes = [
    "TIMS3.SA", "VIVT3.SA", "OIBR3.SA", "OIBR4.SA", "TELB4.SA", "TELB3.SA"
]

# Baixar dados históricos de todas as empresas
dados = yf.download(empresas_telecomunicacoes, start="2020-01-01", end="2024-12-31")

print(dados.head())

caminho_csv = r"C:\Users\User\Desktop\etl_acoes\dados_telecomunicacoes.csv"

dados.to_csv(caminho_csv)

print(f"Dados salvos em: {caminho_csv}")
