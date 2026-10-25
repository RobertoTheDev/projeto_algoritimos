
from datetime import datetime

from shared.validators import validar_corredor


class Corredor:
    def __init__(self, nome, data_nascimento, telefone, percurso):
        percurso_validado = validar_corredor(
            nome,
            data_nascimento,
            telefone,
            percurso,
        )

        self.nome = nome.strip()
        self.data_nascimento = data_nascimento
        self.telefone = telefone.strip()
        self.percurso = percurso_validado

    def calcular_idade(self):
        nascimento = datetime.strptime(
            self.data_nascimento,
            "%d/%m/%Y",
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
        partes = linha.strip().split(";")

        if len(partes) != 4:
            return None

        nome, data_nascimento, telefone, percurso = partes

        try:
            return cls(
                nome,
                data_nascimento,
                telefone,
                percurso,
            )
        except (ValueError, TypeError):
            # Ignora registros inválidos sem interromper a listagem.
            return None

    def __str__(self):
        return (
            f"Nome: {self.nome} | "
            f"Idade: {self.calcular_idade()} | "
            f"Telefone: {self.telefone} | "
            f"Percurso: {self.percurso} km"
        )
