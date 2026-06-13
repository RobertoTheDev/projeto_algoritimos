class RemoverCorredor:

    def __init__(self, repository):
        self.repository = repository

    def executar(self, nome):
        self.repository.remover(nome)