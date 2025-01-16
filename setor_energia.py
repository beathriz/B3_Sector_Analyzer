import yfinance as yf
import matplotlib.pyplot as plt

# Lista de empresas do setor de energia
empresas_energia = [
    "PETR4.SA", "PETR3.SA", "CMIG4.SA", "CMIG3.SA", "EQTL3.SA", "ENGI11.SA", "ENGI3.SA", "ENGI4.SA", 
    "CPLE6.SA", "CPLE3.SA", "CPLE5.SA", "ELET3.SA", "ELET6.SA", "ELET5.SA", "TAEE11.SA", "TAEE4.SA", 
    "TAEE3.SA", "VBBR3.SA", "RNEW3.SA", "RNEW4.SA", "RNEW11.SA", "PRIO3.SA", "RAIZ4.SA", "BRAV3.SA", 
    "AURE3.SA", "EQPA3.SA", "EQMA3B.SA", "GEPA3.SA", "GEPA4.SA", "CEBR6.SA", "CEBR3.SA", "CEBR5.SA", 
    "COCE5.SA", "ENMT3.SA", "ENEV3.SA", "LOGN3.SA", "REDE3.SA"
]

# Baixar dados históricos de todas as empresas
dados = yf.download(empresas_energia, start="2020-01-01", end="2024-12-31")

print(dados.head())

caminho_csv = r"C:\Users\User\Desktop\etl_acoes\dados_energia.csv"

dados.to_csv(caminho_csv)

print(f"Dados salvos em: {caminho_csv}")