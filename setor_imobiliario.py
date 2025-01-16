import yfinance as yf
import matplotlib.pyplot as plt

# Lista de empresas do setor imobiliário
empresas_imobiliario = [
    "MRVE3.SA", "CYRE3.SA", "EZTC3.SA", "DIRR3.SA", "HBOR3.SA", "MTRE3.SA", "JHSF3.SA", 
    "TRIS3.SA", "TEND3.SA", "EVEN3.SA", "MULT3.SA", "SCAR3.SA", "HBRE3.SA", "LOGG3.SA", 
    "RSID3.SA", "ALPK3.SA", "AVLL3.SA", "JOPA3.SA", "JOPA4.SA"
]

# Baixar dados históricos de todas as empresas
dados = yf.download(empresas_imobiliario, start="2020-01-01", end="2024-12-31")

print(dados.head())

caminho_csv = r"C:\Users\User\Desktop\etl_acoes\dados_imobiliario.csv"

dados.to_csv(caminho_csv)

print(f"Dados salvos em: {caminho_csv}")
