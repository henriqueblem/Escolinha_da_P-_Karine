import csv
from pathlib import Path

# Caminho até a pasta raiz do projeto
projeto_estrutura = Path(__file__).parent.parent

def _ler_notas():
    """Lê o CSV e devolve uma lista de (nome, nota)."""
    arquivo = projeto_estrutura / "dados" / "notas.csv"
    alunos = []
    try:
        with open(arquivo, 'r', newline='', encoding='utf-8') as f:
            leitor = csv.reader(f)
            for linha in leitor:
                if len(linha) < 2:
                    continue
                nome, nota = linha[0], float(linha[1])
                alunos.append((nome, nota))
    except FileNotFoundError:
        print("Arquivo não encontrado!")
    return alunos


def exibir_aprovados():
    print("\n--- APROVADOS ---")
    for nome, nota in _ler_notas():
        if nota >= 7:
            print(f"{nome}: {nota}")

def exibir_reprovados():
    alunos = _ler_notas()
    print("\n--- REPROVADOS ---")
    for nome, nota in alunos:
        if nota < 7:
            print(f"{nome}: {nota}")