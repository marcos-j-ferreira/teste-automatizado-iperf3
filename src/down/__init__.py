import subprocess
import os
import time

def run_script(script_name):
    """
    Executa um script Python e aguarda sua conclusão.
    Retorna a saída do script.
    """
    result = subprocess.run(["python", script_name], capture_output=True, text=True)
    return result.stdout


def clear():

    os.system('cls')

def main():
    # Lista para armazenar os resultados de cada execução
    resultados = []

    for i in range(1, 4):  # Executa três vezes
        clear()
        print("|||_______")
        time.sleep(0.5)
        #print(f"Iniciando execução {i}...")
        clear()

        # Executa o script i.py (inserir dados)
        #print("Executando i.py... (pode demorar cerca de 30 segundos)")
        run_script("i.py")  # Aguarda a conclusão automática
        clear()

        print("||||_____")
        time.sleep(0.5)



        # Executa o script r.py (ler dados)
        #print("Executando r.py...")
        clear()

        print("|||||||___")
        time.sleep(0.5)


        resultado = run_script("r.py")
        time.sleep(5)  # Aguarda 5 segundos

        # Executa o script d.py (deletar arquivo)
        #print("Executando d.py...")
        clear()

        print("||||||||||")
        time.sleep(0.5)

        run_script("d.py")

        # Processa a saída do script r.py
        try:
            # Converte a saída (um número) para inteiro
            maior_bandwidth = int(resultado.strip())
            resultados.append(maior_bandwidth)  # Adiciona o resultado à lista
        except ValueError:
            # Caso a saída não seja um número válido
            resultados.append(False)

    # Exibe os resultados finais
    clear()
    print("\nResultados finais:")
    for i, resultado in enumerate(resultados, start=1):
        print(f"Exe {i}: {resultado}")

if __name__ == "__main__":
    main()