from domain.entities.corredor import Corredor

class InscreverCorredor:
    def __init__(self, repository):
        self.repository = repository

    def executar(
            self,
            nome,
            data_nascimento,
            telefone,
            percurso
    ):
        
        corredor = Corredor(
            nome,
            data_nascimento,
            telefone,
            percurso
        )

        self.repository.salvar(corredor)

        return corredor