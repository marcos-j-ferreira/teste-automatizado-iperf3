# Nome do arquivo de entrada e saída
input_file = './data/resultados.txt'  # Altere para o nome do seu arquivo de entrada
output_file = 'resultados.txt'  # Nome do arquivo de saída

# Lê o arquivo de entrada
with open(input_file, 'r', encoding='utf-8') as f:
    linhas = f.readlines()

# Processa as linhas e extrai os resultados
resultados = []
for linha in linhas:
    if 'Exe:' in linha:
        # Extrai a parte que contém os dados
        parte_dados = linha.split(': ', 2)[2].strip()  # Divide em até 3 partes e pega a terceira
        resultados.append(parte_dados)

# Escreve os resultados em um novo arquivo
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("Resultados processados:\n")
    for i, resultado in enumerate(resultados, start=1):
        f.write(f"Execução {i}: {resultado}\n")

print(f"Resultados foram escritos em {output_file}.")