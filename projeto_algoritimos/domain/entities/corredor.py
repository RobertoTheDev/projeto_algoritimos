from datetime import datetime


class Corredor:
    def __init__(self, nome, data_nascimento, telefone, percurso):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        self.percurso = int(percurso)

    def calcular_idade(self):
        nascimento = datetime.strptime(
            self.data_nascimento,
            "%d/%m/%Y"
        )

        hoje = datetime.today()

        idade = hoje.year - nascimento.year

        if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
            idade -= 1

        return idade

    def para_linha(self):
        return (
            f"{self.nome};"
            f"{self.data_nascimento};"
            f"{self.telefone};"
            f"{self.percurso}"
        )

    @classmethod
    def de_linha(cls, linha):
        nome, data_nascimento, telefone, percurso = linha.strip().split(";")

        return cls(
            nome,
            data_nascimento,
            telefone,
            int(percurso)
        )

    def __str__(self):
        return (
            f"Nome: {self.nome} | "
            f"Idade: {self.calcular_idade()} | "
            f"Telefone: {self.telefone} | "
            f"Percurso: {self.percurso} km"
        )