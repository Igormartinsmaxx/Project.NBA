"""Project NBA"""

import os
import pandas as pd

# Caminho para o diretório onde os arquivos estão localizados
directory_path = r"C:\\Users\\silva\\Downloads\\archive"

# Listar todos os arquivos no diretório
print("Arquivos encontrados no diretório:")
for file_name in os.listdir(directory_path):
    print(file_name)

# Ler um arquivo específico (por exemplo, um arquivo CSV)
# Substitua 'nome_do_arquivo.csv' pelo nome do arquivo que deseja carregar
file_to_load = os.path.join(directory_path, "boxscore.csv")  # Substitua pelo arquivo correto
if os.path.isfile(file_to_load) and file_to_load.endswith(".csv"):
    data = pd.read_csv(file_to_load)
    print("\nDados carregados com sucesso:")
    print(data.head())  # Exibe as primeiras linhas do DataFrame
else:
    print("\nO arquivo especificado não foi encontrado ou não é um CSV.")


