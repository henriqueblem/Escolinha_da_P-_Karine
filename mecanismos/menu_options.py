from mecanismos.input_notas import escrever_notas
from mecanismos.ler_dados import leitor_arquivo
from mecanismos.calcular_notas import exibir_aprovados, exibir_reprovados


def exibir_menu():
    print("\n𝐌𝐄𝐍𝐔")
    print("1. Cadastrar notas")
    print("2. Exibir todas as notas")
    print("3. Exibir Aprovados")
    print("4. Exibir Reprovados")
    print("5. Sair")


def logica_menu():
    while True:
        exibir_menu()  # 👈 agora aparece toda vez
        try:
            opcao_escolhida = int(input("\nDigite a opção escolhida: "))
        except ValueError:
            print("Opção inválida. Digite um número de 1 a 5.")
            continue

        if opcao_escolhida == 1:
            escrever_notas()
        elif opcao_escolhida == 2:
            leitor_arquivo('notas.csv')
        elif opcao_escolhida == 3:
            exibir_aprovados()
        elif opcao_escolhida == 4:
            exibir_reprovados()
        elif opcao_escolhida == 5:
            print("\nENCERRANDO O PROGRAMA...\n")
            print('𝑬𝒔𝒄𝒐𝒍𝒊𝒏𝒉𝒂 𝒅𝒂 𝑷𝒓𝒐̂ 𝑲𝒂𝒓𝒊𝒏𝒆')
            break
        else:
            print("Opção inválida. Escolha entre 1 e 5.")