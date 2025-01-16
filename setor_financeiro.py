import yfinance as yf
import matplotlib.pyplot as plt

# Lista de empresas do setor financeiro
empresas_financeiras = [
    "BBDC4.SA", "BBDC3.SA", "ITUB4.SA", "ITUB3.SA", "BBAS3.SA", "BPAC11.SA",
    "BPAC3.SA", "BPAC5.SA", "SANB11.SA", "SANB3.SA", "SANB4.SA", "ABCB4.SA",
    "BRSR6.SA", "BRSR3.SA", "BRSR5.SA", "BMGB4.SA", "PINE4.SA", "PINE3.SA",
    "PINE11.SA", "BMEB4.SA", "BMEB3.SA", "BMIN3.SA", "BMIN4.SA", "BAZA3.SA",
    "BEES3.SA", "BEES4.SA", "RPAD3.SA", "RPAD5.SA", "RPAD6.SA", "BRBI11.SA",
    "CXSE3.SA", "BBSE3.SA"
]

# Baixar dados históricos de todas as empresas
dados = yf.download(empresas_financeiras, start="2020-01-01", end="2024-12-31")

print(dados.head())

caminho_csv = r"C:\Users\User\Desktop\etl_acoes\dados_financeiros.csv"

dados.to_csv(caminho_csv)

print(f"Dados salvos em: {caminho_csv}")