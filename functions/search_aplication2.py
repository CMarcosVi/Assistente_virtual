import subprocess
import time
import os

def abrir_aplicacao(file_path,aplication_name):
    def is_installed():
        return os.path.exists(file_path)
    
    if is_installed():
        subprocess.run(file_path, check=True)
        time.sleep(1)
    else:
        print("${aplication_name} não está instalado no Windows.")