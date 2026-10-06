import csv
from pathlib import Path

projeto_estrutura = Path(__file__).parent.parent
CABECALHO = ["nome", "nota"]


def _carregar_alunos(arquivo):
    """Lê o CSV e devolve um dict {nome: nota}, pulando o cabeçalho."""
    alunos = {}
    if not arquivo.is_file():
        return alunos

    with open(arquivo, 'r', newline='', encoding='utf-8') as f:
        leitor = csv.reader(f)
        next(leitor, None)  # pula o cabeçalho
        for linha in leitor:
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

    # Detecta se o arquivo é novo (pra decidir se escreve cabeçalho)
    arquivo_novo = not arquivo.is_file()
    alunos = _carregar_alunos(arquivo)

    while True:
        nome = input("Digite o nome do aluno: ").strip()
        if not nome:
            print("Nome não pode ficar vazio.")
            continue

        if nome in alunos:
            print(f"    {nome} já cadastrado (nota {alunos[nome]}). A nota será atualizada.")

        try:
            nota = float(input("Insira a nota do aluno: ").replace(",", "."))
        except ValueError:
            print("Nota inválida. Digite um número (ex: 7.5).")
            continue

        if nota < 0 or nota > 10:
            print("Nota fora do intervalo permitido. Digite um valor entre 0 e 10.")
            continue

        alunos[nome] = nota

        if not _perguntar_continuar():
            break

    # Reescreve o arquivo com cabeçalho
    with open(arquivo, 'w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        escritor.writerow(CABECALHO)
        for nome, nota in alunos.items():
            escritor.writerow([nome, nota])

    print(f"\n{len(alunos)} aluno(s) no arquivo.")