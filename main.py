from oop import *
from Dados do Menu import *

def menu_principal():
    print(20 * "-=")
    print("       Menu")
    print(20 * "-=")

    print("--------------------\n"
          "1 - Cadastrar \n"
          "2 - Listar \n"
          "--------------------")

    while True:
        escolha = int(input("Escolha a opção desejada: "))
        if escolha == 1:
            dados.cadastrar_pessoas()
        if escolha == 2:
            dados.listar_pessoas()
        if escolha == 3:
            break
        else:
            print("Opção inválida!\n")

menu_principal()



