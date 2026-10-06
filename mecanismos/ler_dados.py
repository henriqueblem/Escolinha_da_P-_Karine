import csv
from pathlib import Path

projeto_estrutura = Path(__file__).parent.parent


def leitor_arquivo(arquivo):
    """Lê o CSV e imprime todos os alunos cadastrados."""
    dados_path = projeto_estrutura / "dados" / arquivo

    try:
        with open(dados_path, 'r', newline='', encoding='utf-8') as f:
            leitor = csv.reader(f)

            print("\n--- TODAS AS NOTAS ---")
            encontrou = False

            for linha in leitor:
                if len(linha) < 2:
                    continue  # pula linhas vazias/malformadas

                nome = linha[0].strip()
                try:
                    nota = float(linha[1])
                except ValueError:
                    continue  # pula se a nota não for número

                print(f"{nome}: {nota}")
                encontrou = True

            if not encontrou:
                print("Nenhum aluno cadastrado ainda.")

    except FileNotFoundError:
        print("Arquivo não encontrado! Cadastre alunos primeiro.")