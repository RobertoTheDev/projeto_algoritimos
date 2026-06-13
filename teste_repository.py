from projeto_algoritimos.domain.entities.corredor import Corredor

from projeto_algoritimos.infrastructure.persistence.arquivo_manager import (
    ArquivoManager
)

from projeto_algoritimos.infrastructure.repositories.txt_corredor_repository import (
    TxtCorredorRepository
)

arquivo_manager = ArquivoManager(
    "projeto_algoritimos/data/corredores.txt"
)

repository = TxtCorredorRepository(
    arquivo_manager
)

corredor = Corredor(
    "Roberto",
    "15/05/2002",
    "88999999999",
    10
)

repository.salvar(corredor)

for corredor in repository.listar():
    print(corredor)