import json
import datetime
projetos = []
# 🔎 função para buscar projeto
def buscar_projeto(projetos, nome):
    for projeto in projetos:
        if projeto["nome"].lower() == nome.lower():
            return projeto
    return None
# funçao para carregar dados
def carregar_dados():
    try:
        with open("projetos.json", "r") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        print("Arquivo não encontrado. Criando novo portifólio.")
        return []

    except json.decoder.JSONDecodeError:
        print("Arquivo corrompido ou vazio. Iniciando novo portfólio.")
        return []
# função para salvar dados
def salvar_dados(projetos):
    with open("projetos.json", "w") as arquivo:
        json.dump(projetos, arquivo, indent=4)

# 📋 listar projetos
def listar_projetos(projetos):
    if not projetos:
        print("Não há jogos cadastrados.")
        return

    for projeto in projetos:
        print("\nDetalhes do projeto:")
        print(f"nome: {projeto['nome']}")
        print(f"concluido: {projeto['concluido']}")
        print("historico:")

        if projeto["historico"]:
            for registro in projeto["historico"]:
                data, nome, status = registro
                print(f" - {data.strftime('%d/%m/%Y %H:%M:%S')} | {nome} | {status}")
        else:
            print(" - Sem histórico.")


# 🔄 atualizar projeto
def atualizar_projeto(projetos):
    nome = input("Digite o nome do projeto que deseja atualizar: ")
    projeto = buscar_projeto(projetos, nome)

    if projeto is None:
        print("Projeto não encontrado.")
        return

    novo_nome = input("Digite o novo nome do projeto: ")

    try:
        status = bool(int(input("Finalizou? (1 = sim | 0 = não): ")))
    except ValueError:
        print("Entrada inválida.")
        return

    projeto["nome"] = novo_nome
    projeto["concluido"] = status

    projeto["historico"].append((
        datetime.datetime.now(),
        novo_nome,
        status
    ))

    print("Projeto atualizado com sucesso.")

projetos = carregar_dados()

while True:
    comando = input("Digite um comando.").upper()

    if comando == "ABOUT":
        print("boas-vindas ao software de Vitor Miguel R Albano.")
        continue

    elif comando == "QUIT":
        print("obrigado pela visita ao nosso software")
        break

    elif comando == "ADD":
        quantidade_projetos = int(input("quantos jogos deseja adicionar."))

        if quantidade_projetos < 0:
            print("Opa! a quantidade adicionada parece invalida digite um numero maior que zero")
            continue

        for i in range(quantidade_projetos):
            nome_projeto = input("Digite o nome do projeto.")
            cadastro_jogos = {
                "nome": nome_projeto,
                "concluido": False,
                "historico": []
            }
            projetos.append(cadastro_jogos)
            print(f"Parabéns! cadastramos o projeto {nome_projeto}.")


        salvar_dados(projetos)
        continue

    elif comando == "LIST":
        listar_projetos(projetos)
        continue

    elif comando == "ATUALIZAR":
        atualizar_projeto(projetos)
        continue

    elif comando == "REMOVER":
        nome_projeto_para_remover = input("Digite o nome do projeto que deseja modificar.")
        projeto_para_remover = buscar_projeto(projetos, nome_projeto_para_remover)

        if projeto_para_remover is not None:
            projetos.remove(projeto_para_remover)
            print(f"projeto: {nome_projeto_para_remover} removido com sucesso.")
            salvar_dados(projetos)
        else:
            print("Não encontrei o projeto.")
        continue

    else:
        print("comando não reconhecido. tente novamente.")
        print("Ate a proxima (;")