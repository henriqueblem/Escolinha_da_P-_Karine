from mecanismos.input_notas import escrever_notas
from mecanismos.ler_dados import leitor_arquivo
from mecanismos.calcular_notas import exibir_aprovados, exibir_reprovados
from mecanismos.buscar_aluno import buscar_por_nome


def exibir_menu():
    print("\n𝐌𝐄𝐍𝐔")
    print("1. Cadastrar notas")
    print("2. Exibir todas as notas")
    print("3. Exibir Aprovados")
    print("4. Exibir Reprovados")
    print("5. Buscar aluno por nome")
    print("6. Sair")


def logica_menu():
    while True:
        exibir_menu()
        try:
            opcao = int(input("\nDigite a opção escolhida: "))
        except ValueError:
            print("Opção inválida. Digite um número de 1 a 6.")
            continue

        if opcao == 1:
            escrever_notas()
        elif opcao == 2:
            leitor_arquivo('notas.csv')
        elif opcao == 3:
            exibir_aprovados()
        elif opcao == 4:
            exibir_reprovados()
        elif opcao == 5:
            buscar_por_nome()
        elif opcao == 6:
            print("\nENCERRANDO O PROGRAMA\n")
            print('𝑬𝒔𝒄𝒐𝒍𝒊𝒏𝒉𝒂 𝒅𝒂 𝑷𝒓𝒐̂ 𝑲𝒂𝒓𝒊𝒏𝒆')
            break
        else:
            print("Opção inválida. Escolha entre 1 e 6.")