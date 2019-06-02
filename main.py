from oop import *
from Dados do Menu import *

def menu_principal():

    while True:
        escolha = int(input("Escolha a opção desejada: "))
        if escolha == 1:
            dados = informaçoes_funcionario()
            funcionario_a = funcionario(dados.get('nome'),dados.get('rg'),dados.get('cpf'),
            dados.get('dataNascimento'),dados.get('sexo'), dados.get('matricula'),dados.get('setor'),
            dados.get('nivel'))
            dados.cadastrar_funcionario()
        elif escolha == 2:
            dados = informacoes_professor()
            professor_a = professor(dados.get('nome'),dados.get('rg'),dados.get('cpf'),
            dados.get('dataNascimento'),dados.get('sexo'), dados.get('matricula'),dados.get('setor'),
            dados.get('nivel'), dados.get('formacao'), dados.get('disciplina'))
            dados.cadastrar_professor()
        elif escolha == 3:
            funcionario.exibir_todos()
            
        elif escolha == 0:
            break

def mostrar_indice():
    print(20 * "-=")
    print("       Menu")
    print(20 * "-=")

    print("--------------------\n"
          "1 - Cadastrar \n"
          "2 - Listar \n"
          "--------------------")

    if __name__ == '__main__':
        menu_principal()



