from modelos.restaurante import Restaurante
import os

def main():
    exibir_subtitulo("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
    exibir_opcoes()
    escolher_opcao()



def voltar_ao_menu_principal():
    input("\nPressione qualquer tecla para continuar... ")
    main()
def exibir_subtitulo(subtitulo):
    os.system('cls')
    linha=("*"*len(subtitulo))
    print (linha)
    print(subtitulo)
    print (linha)
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar situação do restaurante')
    print('4. Sair\n')
def finalizar_app():
    exibir_subtitulo("Finalizando o app")
def opcao_invalida():
    input('Opção inválida escolhida, pressione qualquer tecla para voltar')
    main()
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            exibir_subtitulo('Cadastro de restaurantes. ')
            nome_restaurante = input('Digite o nome do restaurante: ')  
            if  not Restaurante.verifica_contido(nome_restaurante):              
                Restaurante(nome_restaurante,input('Digite a categoria do Restaurante: '))
                print(f'O restaurante {Restaurante.restaurantes[-1]._nome} foi cadastrado com sucesso.')
            else:
                print('Nome já contido no banco de dados. ')
            voltar_ao_menu_principal()
        elif opcao_escolhida == 2: 
            exibir_subtitulo('Lista de restaurantes. ')
            Restaurante.listar_restaurantes()
            voltar_ao_menu_principal()
        elif opcao_escolhida == 3: 
            exibir_subtitulo('Alterar situação do restaurante. ')
            Restaurante.alterar_situacao_restaurante(input('Digite o nome do restaurante: '))
            voltar_ao_menu_principal()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except Exception as error:
        print (error)
        opcao_invalida()

if __name__ == '__main__':
    main()