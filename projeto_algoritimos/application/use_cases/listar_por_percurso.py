class ListarPorPercurso:

    def __init__(self, repository):
        self.repository = repository

    def executar(self, percurso):
        corredores = self.repository.listar()

        return [
            corredor
            for corredor in corredores
            if corredor.percurso == percurso
        ]