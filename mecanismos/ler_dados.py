import csv
from pathlib import Path

projeto_estrutura = Path(__file__).parent.parent

def leitor_arquivo(arquivo):
    # Defina o caminho do arquivo
    dados_path = projeto_estrutura / "dados" / arquivo
    
    # Abre o arquivo para leitura
    try:
        with open(dados_path, 'r', newline='') as f:
            # Cria um leitor de CSV
            leitor = csv.reader(f)
            
            # Exibe os dados do arquivo
            for row in leitor:
                print("-" * 20)
                for i, valor in enumerate(row):
                    if valor.startswith('Aluno '):
                        nome = valor[6:]
                        nota = row[i + 1]
                        print(f"{nome}: {nota}")
    except FileNotFoundError:
        print("Arquivo não encontrado!")