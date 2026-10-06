import csv
from pathlib import Path

# Defina o caminho até a pasta raiz do projeto
projeto_estrutura = Path(__file__).parent.parent

def escrever_notas():
    print()
    nomes_notas = []
    while True:
        nome = input('Digite o nome do aluno (ou "sair" para terminar): ')
        if nome.lower() == 'sair':
            break
        nota = input('Insira a nota do Aluno: ')
        nomes_notas.append((nome, nota))

    # Defina o caminho completo da pasta "dados"
    dados_path = projeto_estrutura / "dados"

    # Crie a pasta "dados" se ela não existir
    dados_path.mkdir(parents=True, exist_ok=True)

    # Defina o caminho do arquivo
    arquivo = dados_path / "notas.csv"

    if arquivo.is_file():
        with open(arquivo, 'a', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            for nome, nota in nomes_notas:
                escritor.writerow([nome, nota])
    else:
        with open(arquivo, 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            for nome, nota in nomes_notas:
                escritor.writerow([nome, nota])