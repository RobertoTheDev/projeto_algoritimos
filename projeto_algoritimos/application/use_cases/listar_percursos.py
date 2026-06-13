class ListarPercursos:

    def __init__(self, repository):
        self.repository = repository

    def executar(self):

        percursos = {
            3: 0,
            5: 0,
            10: 0,
            15: 0,
            21: 0,
            42: 0
        }

        for corredor in self.repository.listar():
            percursos[corredor.percurso] += 1

        return percursos