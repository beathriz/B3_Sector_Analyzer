import yfinance as yf
import matplotlib.pyplot as plt

# Lista de empresas do setor de consumo
empresas_consumo = [
    "ABEV3.SA", "MGLU3.SA", "LREN3.SA", "PCAR3.SA", "PETZ3.SA", "GMAT3.SA", "AMER3.SA", 
    "ALPA4.SA", "ALPA3.SA", "VIVA3.SA", "CEAB3.SA", "HYPE3.SA", "RADL3.SA", "PFRM3.SA", 
    "POMO4.SA", "POMO3.SA", "UGPA3.SA", "LWSA3.SA", "LPSB3.SA", "LIGT3.SA", "LAVV3.SA", 
    "LUPA3.SA", "LUXM4.SA"
]

# Baixar dados históricos de todas as empresas
dados = yf.download(empresas_consumo, start="2020-01-01", end="2024-12-31")

print(dados.head())

caminho_csv = r"C:\Users\User\Desktop\etl_acoes\dados_consumo.csv"

dados.to_csv(caminho_csv)

print(f"Dados salvos em: {caminho_csv}")
