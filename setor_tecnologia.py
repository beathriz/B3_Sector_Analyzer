import yfinance as yf
import matplotlib.pyplot as plt

# Lista de empresas do setor de tecnologia
empresas_tecnologia = [
    "WEGE3.SA", "POSI3.SA", "TOTS3.SA", "LWSA3.SA", "BMOB3.SA", "INTB3.SA", "GETN3.SA", 
    "NGRD3.SA", "ALLD3.SA", "SYNE3.SA", "ENJU3.SA", "TRAD3.SA", "VSTE3.SA", "NEXP3.SA", "DTCY3.SA"
]

# Baixar dados históricos de todas as empresas
dados = yf.download(empresas_tecnologia, start="2020-01-01", end="2024-12-31")

print(dados.head())

caminho_csv = r"C:\Users\User\Desktop\etl_acoes\dados_tecnologia.csv"

dados.to_csv(caminho_csv)

print(f"Dados salvos em: {caminho_csv}")
