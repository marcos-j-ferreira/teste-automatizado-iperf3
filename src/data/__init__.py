import subprocess
import os

def run_command(command):
    """Executa um comando e exibe a saída."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Se o código de retorno for diferente de zero, houve erro
        if result.returncode != 0:
            print("Erro ao executar o comando:", result.stderr)
            return False
        
        print("Saída do comando:", result.stdout)
        return True
    
    except Exception as e:
        print("Erro inesperado:", e)
        return False

# Caminho absoluto do script
script_path = os.path.abspath("data/run.py")  # Ajuste se necessário

# Executa o comando com aspas duplas para lidar com espaços no caminho
command = f'python "{script_path}"'  

if run_command(command):
    print("Comando executado com sucesso.")
else:
    print("Falha ao executar o comando.")
