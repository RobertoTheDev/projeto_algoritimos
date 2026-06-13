from projeto_algoritimos.application.use_cases.inscrever_corredor import (
    InscreverCorredor
)

from projeto_algoritimos.application.use_cases.remover_corredor import (
    RemoverCorredor
)

from projeto_algoritimos.application.use_cases.listar_corredores import (
    ListarCorredores
)

from projeto_algoritimos.application.use_cases.listar_por_percurso import (
    ListarPorPercurso
)

from projeto_algoritimos.application.use_cases.listar_percursos import (
    ListarPercursos
)

from projeto_algoritimos.application.use_cases.listar_faixas_etarias import (
    ListarFaixasEtarias
)

from projeto_algoritimos.infrastructure.persistence.arquivo_manager import (
    ArquivoManager
)

from projeto_algoritimos.infrastructure.repositories.txt_corredor_repository import (
    TxtCorredorRepository
)


# Configuração
arquivo = ArquivoManager(
    "projeto_algoritimos/data/corredores.txt"
)

repository = TxtCorredorRepository(arquivo)

# Limpa o arquivo para o teste começar do zero
arquivo.escrever_linhas([])

# Use Cases
inscrever = InscreverCorredor(repository)
remover = RemoverCorredor(repository)
listar = ListarCorredores(repository)
listar_por_percurso = ListarPorPercurso(repository)
listar_percursos = ListarPercursos(repository)
listar_faixas = ListarFaixasEtarias(repository)

# Cadastra corredores
inscrever.executar(
    "Roberto",
    "15/05/2002",
    "88999999999",
    10
)

inscrever.executar(
    "Maria",
    "10/08/1998",
    "88988888888",
    5
)

inscrever.executar(
    "Carlos",
    "20/03/1975",
    "88977777777",
    21
)

inscrever.executar(
    "Ana",
    "05/11/1960",
    "88966666666",
    5
)

print("\n=== TODOS OS CORREDORES ===")

for corredor in listar.executar():
    print(corredor)

print("\n=== PERCURSO 5 KM ===")

for corredor in listar_por_percurso.executar(5):
    print(corredor)

print("\n=== QUANTIDADE POR PERCURSO ===")

for percurso, quantidade in listar_percursos.executar().items():
    print(f"{percurso} km -> {quantidade}")

print("\n=== FAIXAS ETÁRIAS ===")

for faixa, quantidade in listar_faixas.executar().items():
    print(f"{faixa}: {quantidade}")

print("\n=== REMOVENDO MARIA ===")

remover.executar("Maria")

print("\n=== LISTA APÓS REMOÇÃO ===")

for corredor in listar.executar():
    print(corredor)