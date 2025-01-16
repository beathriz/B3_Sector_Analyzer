import yfinance as yf
import matplotlib.pyplot as plt

# Lista de empresas do setor industrial
empresas_industrial = [
    "GGBR4.SA", "GGBR3.SA", "GOAU4.SA", "GOAU3.SA", "CSNA3.SA", "USIM5.SA", "USIM3.SA", "EMBR3.SA", 
    "RAPT4.SA", "RAPT3.SA", "TUPY3.SA", "ROMI3.SA", "FRAS3.SA", "MYPK3.SA", "WHRL4.SA", "WHRL3.SA", 
    "TKNO4.SA", "TKNO3.SA", "MWET4.SA", "MWET3.SA", "EALT4.SA", "EALT3.SA", "SHUL4.SA", "RSUL4.SA", 
    "MTSA4.SA"
]

# Baixar dados históricos de todas as empresas
dados = yf.download(empresas_industrial, start="2020-01-01", end="2024-12-31")

print(dados.head())

caminho_csv = r"C:\Users\User\Desktop\etl_acoes\dados_industrial.csv"

dados.to_csv(caminho_csv)

print(f"Dados salvos em: {caminho_csv}")
