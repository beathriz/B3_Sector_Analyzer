import yfinance as yf
import matplotlib.pyplot as plt

# Lista de empresas do setor de serviços públicos
empresas_servicos_publicos = [
    "SBSP3.SA", "SAPR4.SA", "SAPR11.SA", "SAPR3.SA", "CSMG3.SA", "CEBR6.SA", "CEBR3.SA", 
    "CEBR5.SA", "COCE5.SA", "ENMT3.SA", "ENEV3.SA", "LOGN3.SA", "REDE3.SA"
]

# Baixar dados históricos de todas as empresas
dados = yf.download(empresas_servicos_publicos, start="2020-01-01", end="2024-12-31")

print(dados.head())

caminho_csv = r"C:\Users\User\Desktop\etl_acoes\dados_servicos_publicos.csv"

dados.to_csv(caminho_csv)

print(f"Dados salvos em: {caminho_csv}")
