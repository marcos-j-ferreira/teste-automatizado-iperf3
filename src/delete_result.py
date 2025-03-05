import os

# Caminho do arquivo que você deseja deletar


caminho_arquivo = [
    "./data/resultados.txt",
    "./up/resultados.txt",
    "./down/resultados.txt",
    "./resultados.txt"
]

for i in range(0,4):
    if os.path.exists(caminho_arquivo[i]):
        os.remove(caminho_arquivo[i])
        print(f" file delete: {True}")
    else:
        print(f" file delete: {False}")
