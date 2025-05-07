# Classe que representa uma tarefa
class Tarefa:
    def __init__(self, descricao):  # Inicializa a tarefa com uma descrição e um status de concluída
        sel.descricao = descricao
        self.concluida = False

    def marcar_concluida(self):  # Marca a tarefa como concluída
        self.concluida = True


tarefas = []
# Função para adicionar uma tarefa


def adicionar_tarefa(descricao):  # Adiciona uma nova tarefa à lista de tarefas
    nova_tarefa = Tarefa(descricao)
    tarefas.append(nova_tarefa)


def listar_tarefas():  # Lista todas as tarefas
    # Itera sobre as tarefas e imprime a descrição e o status
    for i, tarefa in enumerate(tarefas):
        # Exibe o número da tarefa, a descrição e se está concluída ou pendente
        status = "[Feita] Feita" if tarefa.concluida else "[Pendente] Pendente"
        # Exibe o número da tarefa, a descrição e se está concluída ou pendente
        print(f"{i + 1}. {tarefa.descricao} - {status}")
        # Exibe o número da tarefa, a descrição e se está concluída ou pendente
    print()


def concluir_tarefa(indice):

    if 0 <= indice < len(tarefas):

        tarefas[indice].marcar_concluida()
        print("Tarefa marcada como concluída.")
    else:
        print("Índice inválido.")


def remover_tarefa(indice):

    if 0 <= indice < len(tarefas):
        removida = tarefas.pop(indice)
        print(f"Tarefa '{removida.descricao}' removida.")
    else:
        print("Índice inválido.")


def mostrar_menu():

    print("\n----- MENU -----")
    print("1 - Adicionar Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Concluir Tarefa")
    print("4 - Remover Tarefa")
    print("5 - Sair")


while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        desc = input("Digite a descrição da tarefa: ")
        adicionar_tarefa(descricao)
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        listar_tarefas()
        try:
            num = int(input("Digite o número da tarefa para concluir: ")) - 1
            concluir_tarefa(num)
        except ValueError:
            print("Por favor, digite um número válido.")
    elif opcao == "4":
        listar_tarefas()
        try:
            num = int(input("Digite o número da tarefa para remover: ")) - 1
            remover_tarefa(num)
        except ValueError:
            print("Por favor, digite um número válido.")
    elif opcao == "5":
        print("Saindo... Até logo!")
    break
else:
    print("Opção inválida. Tente novamente.")
