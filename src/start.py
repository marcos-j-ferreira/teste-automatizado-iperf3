import subprocess

def run_command(command):
    """Executa um comando e salva a saída em um arquivo."""
    try:
        result = subprocess.run(["python", command], capture_output=True, text=True)
        # if not result :
        #     print("Erro ao executar o comando:", result.stderr)
        #     return False
        
        return True
    
    except  Exception as e:
        print("Erro inesperado:", e)
        return False

# Comando a ser executado
command =  " ./data/__init__.py"



# Executa o comando e salva a saída
if run_command(command):
    print("Comando executado com sucesso.")
else:
    print("Falha ao executar o comando.")