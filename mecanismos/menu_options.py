from mecanismos.input_notas import escrever_notas
from mecanismos.ler_dados import leitor_arquivo



def exibir_menu():
    print('𝐌𝐄𝐍𝐔')
    print('1. Cadastrar notas')
    print('2. Exibir todas as notas')
    print('3. Exibir Aprovados')
    print('4. Exibir Reprovados')
    print('5. Sair')
    print()

def logica_menu():
    while True:
        try:
            exibir_menu()
            opcao_escolhida = int(input('Digite a opção escolhida: '))
        except ValueError:
            print('Opção inválida. Digite um número de 1 a 5')
            continue

        if opcao_escolhida == 1:
            escrever_notas()
        elif opcao_escolhida == 2:
            leitor_arquivo('notas.csv')
        elif opcao_escolhida == 3:
            pass
        elif opcao_escolhida == 4:
            pass
        elif opcao_escolhida == 5:
            print('\nENCERRANDO O PROGRAMA\n')
            break