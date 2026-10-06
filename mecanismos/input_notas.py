import csv
from pathlib import Path

projeto_estrutura = Path(__file__).parent.parent


def _carregar_alunos(arquivo):
    """Lê o CSV e devolve um dict {nome: nota}."""
    alunos = {}
    if not arquivo.is_file():
        return alunos

    with open(arquivo, 'r', newline='', encoding='utf-8') as f:
        for linha in csv.reader(f):
            if len(linha) < 2:
                continue
            try:
                alunos[linha[0].strip()] = float(linha[1])
            except ValueError:
                continue
    return alunos


def _perguntar_continuar():
    while True:
        opcao = input("Cadastrar outro aluno? (1-Sim / 2-Não): ").strip()
        if opcao == "1":
            return True
        if opcao == "2":
            return False
        print("Opção inválida. Digite 1 ou 2.")


def escrever_notas():
    print()
    dados_path = projeto_estrutura / "dados"
    dados_path.mkdir(parents=True, exist_ok=True)
    arquivo = dados_path / "notas.csv"

    # Carrega o que já existe (dict nome -> nota)
    alunos = _carregar_alunos(arquivo)

    while True:
        nome = input("Digite o nome do aluno: ").strip()
        if not nome:
            print("Nome não pode ficar vazio.")
            continue

        if nome in alunos:
            print(f"⚠️  {nome} já cadastrado (nota {alunos[nome]}). A nota será atualizada.")

        try:
            nota = float(input("Insira a nota do aluno: ").replace(",", "."))
        except ValueError:
            print("Nota inválida. Digite um número (ex: 7.5).")
            continue

        alunos[nome] = nota

        if not _perguntar_continuar():
            break

    # Reescreve o arquivo inteiro (substitui duplicatas)
    with open(arquivo, 'w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        for nome, nota in alunos.items():
            escritor.writerow([nome, nota])

    print(f"\n{len(alunos)} aluno(s) no arquivo.")