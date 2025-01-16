import yfinance as yf
import matplotlib.pyplot as plt

# Lista de empresas do setor de materiais básicos
empresas_materiais_basicos = [
    "VALE3.SA", "KLBN11.SA", "KLBN4.SA", "KLBN3.SA", "SUZB3.SA", "CMIN3.SA", "BRKM5.SA", 
    "BRKM3.SA", "BRKM6.SA", "FESA4.SA", "FESA3.SA", "UNIP6.SA", "UNIP3.SA", "UNIP5.SA", 
    "RANI3.SA", "NUTR3.SA", "AGRO3.SA", "SOJA3.SA", "FHER3.SA", "CRPG5.SA", "CRPG6.SA", "AGXY3.SA"
]

# Baixar dados históricos de todas as empresas
dados = yf.download(empresas_materiais_basicos, start="2020-01-01", end="2024-12-31")

print(dados.head())

caminho_csv = r"C:\Users\User\Desktop\etl_acoes\dados_materiais_basicos.csv"

dados.to_csv(caminho_csv)

print(f"Dados salvos em: {caminho_csv}")
