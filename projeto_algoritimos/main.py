from infrastructure.persistence.arquivo_manager import ArquivoManager
from infrastructure.repositories.txt_corredor_repository import TxtCorredorRepository

from application.use_cases.inscrever_corredor import InscreverCorredor
from application.use_cases.remover_corredor import RemoverCorredor
from application.use_cases.listar_corredores import ListarCorredores
from application.use_cases.listar_por_percurso import ListarPorPercurso
from application.use_cases.listar_percursos import ListarPercursos
from application.use_cases.listar_faixas_etarias import ListarFaixasEtarias


arquivo_manager = ArquivoManager("data/corredores.txt")
repository = TxtCorredorRepository(arquivo_manager)

inscrever = InscreverCorredor(repository)
remover = RemoverCorredor(repository)
listar = ListarCorredores(repository)
listar_por_percurso = ListarPorPercurso(repository)
listar_percursos = ListarPercursos(repository)
listar_faixas_etarias = ListarFaixasEtarias(repository)


while True:
    print("\n=== SISTEMA DE CORRIDAS ===")
    print("1 - Inscrever corredor")
    print("2 - Remover corredor")
    print("3 - Listar corredores")
    print("4 - Listar por percurso")
    print("5 - Listar percursos")
    print("6 - Listar faixas etárias")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":

        nome = input("Nome: ")
        data_nascimento = input(
            "Data de nascimento (dd/mm/aaaa): "
        )
        telefone = input("Telefone: ")
        percurso = int(
            input("Percurso (3, 5, 10, 15, 21 ou 42): ")
        )

        inscrever.executar(
            nome,
            data_nascimento,
            telefone,
            percurso
        )

        print("\nCorredor inscrito com sucesso!")

    elif opcao == "2":

        nome = input(
            "Digite o nome do corredor para remover: "
        )

        remover.executar(nome)

        print("\nCorredor removido com sucesso!")

    elif opcao == "3":

        corredores = listar.executar()

        if not corredores:
            print("\nNenhum corredor cadastrado.")
        else:
            print("\n=== CORREDORES ===")
            for corredor in corredores:
                print(corredor)

    elif opcao == "4":

        percurso = int(
            input("Digite o percurso: ")
        )

        corredores = listar_por_percurso.executar(
            percurso
        )

        if not corredores:
            print(
                "\nNenhum corredor encontrado nesse percurso."
            )
        else:
            print(
                f"\n=== CORREDORES DO PERCURSO {percurso} KM ==="
            )

            for corredor in corredores:
                print(corredor)

    elif opcao == "5":

        percursos = listar_percursos.executar()

        print("\n=== INSCRITOS POR PERCURSO ===")

        for percurso, quantidade in percursos.items():
            print(
                f"{percurso} km -> {quantidade} inscrito(s)"
            )

    elif opcao == "6":

        faixas = listar_faixas_etarias.executar()

        print("\n=== FAIXAS ETÁRIAS ===")

        for faixa, quantidade in faixas.items():
            print(
                f"{faixa}: {quantidade} inscrito(s)"
            )

    elif opcao == "0":

        print("\nEncerrando sistema...")
        break

    else:

        print("\nOpção inválida!")