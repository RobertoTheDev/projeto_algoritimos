class ListarFaixasEtarias:

    def __init__(self, repository):
        self.repository = repository

    def executar(self):

        faixas = {
            "18 a 29": 0,
            "30 a 39": 0,
            "40 a 49": 0,
            "50 a 59": 0,
            "60+": 0
        }

        for corredor in self.repository.listar():

            idade = corredor.calcular_idade()

            if 18 <= idade <= 29:
                faixas["18 a 29"] += 1

            elif 30 <= idade <= 39:
                faixas["30 a 39"] += 1

            elif 40 <= idade <= 49:
                faixas["40 a 49"] += 1

            elif 50 <= idade <= 59:
                faixas["50 a 59"] += 1

            elif idade >= 60:
                faixas["60+"] += 1

        return faixas