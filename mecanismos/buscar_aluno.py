import csv
from pathlib import Path

projeto_estrutura = Path(__file__).parent.parent
_NOME_ARQUIVO = "notas.csv"


def buscar_por_nome():
    print()
    termo = input("Digite o nome (ou parte do nome) do aluno: ").strip().lower()
    if not termo:
        print("Nome não pode ficar vazio.")
        return

    arquivo = projeto_estrutura / "dados" / _NOME_ARQUIVO

    try:
        with open(arquivo, 'r', newline='', encoding='utf-8') as f:
            leitor = csv.reader(f)
            next(leitor, None)  # pula cabeçalho

            encontrados = []
            for linha in leitor:
                if len(linha) < 2:
                    continue
                nome = linha[0].strip()
                if termo in nome.lower():  # busca parcial, case-insensitive
                    try:
                        encontrados.append((nome, float(linha[1])))
                    except ValueError:
                        continue

    except FileNotFoundError:
        print("Arquivo não encontrado! Cadastre alunos primeiro.")
        return

    if not encontrados:
        print(f"Nenhum aluno encontrado com '{termo}'.")
        return

    print(f"\n--- RESULTADOS PARA '{termo}' ---")
    for nome, nota in encontrados:
        status = "Aprovado" if nota >= 7 else "Reprovado"
        print(f"{nome}: {nota}  {status}")