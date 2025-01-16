import yfinance as yf
import matplotlib.pyplot as plt

# Lista de empresas de outros setores
empresas_outros_setores = [
    "B3SA3.SA", "CVCB3.SA", "CCRO3.SA", "RAIL3.SA", "MOVI3.SA", "RENT3.SA", "ECOR3.SA", 
    "STBP3.SA", "TPIS3.SA", "JSLG3.SA", "SIMH3.SA", "VAMO3.SA", "AMBP3.SA", "DESK3.SA", 
    "AERI3.SA", "TCSA3.SA", "ATMP3.SA", "MNPR3.SA"
]

# Baixar dados históricos de todas as empresas
dados = yf.download(empresas_outros_setores, start="2020-01-01", end="2024-12-31")

print(dados.head())

caminho_csv = r"C:\Users\User\Desktop\etl_acoes\dados_outros_setores.csv"

dados.to_csv(caminho_csv)

print(f"Dados salvos em: {caminho_csv}")
