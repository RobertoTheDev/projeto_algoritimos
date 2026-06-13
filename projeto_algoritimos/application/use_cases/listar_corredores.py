from domain.entities.corredor import Corredor

class ListarCorredores:

    def __init__(self, repository):
        self.repository = repository

    def executar(self):
        corredores = self.repository.listar()

        return sorted(
            corredores,
            key=lambda corredor: corredor.nome.lower()
        )