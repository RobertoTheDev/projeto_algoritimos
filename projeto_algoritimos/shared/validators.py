
from datetime import date, datetime


PERCURSOS_PERMITIDOS = {3, 5, 10, 15, 21, 42}


def validar_nome(nome):
    if not isinstance(nome, str) or not nome.strip():
        raise ValueError("O nome do corredor é obrigatório.")

    if len(nome.strip()) < 2:
        raise ValueError("O nome deve ter pelo menos 2 caracteres.")


def validar_data_nascimento(data_nascimento):
    if not isinstance(data_nascimento, str):
        raise ValueError("A data de nascimento deve ser um texto.")

    try:
        nascimento = datetime.strptime(
            data_nascimento,
            "%d/%m/%Y",
        ).date()
    except ValueError as erro:
        raise ValueError(
            "Data de nascimento inválida. Use o formato DD/MM/AAAA."
        ) from erro

    # Garante que a data informada corresponde ao formato esperado.
    if nascimento.strftime("%d/%m/%Y") != data_nascimento:
        raise ValueError(
            "Data de nascimento inválida. Use o formato DD/MM/AAAA."
        )

    if nascimento > date.today():
        raise ValueError("A data de nascimento não pode estar no futuro.")


def validar_telefone(telefone):
    if not isinstance(telefone, str) or not telefone.strip():
        raise ValueError("O telefone é obrigatório.")

    if not telefone.strip().isdigit():
        raise ValueError("O telefone deve conter apenas números.")


def validar_percurso(percurso):
    try:
        percurso_convertido = int(percurso)
    except (ValueError, TypeError) as erro:
        raise ValueError(
            "O percurso deve ser um número inteiro."
        ) from erro

    if percurso_convertido not in PERCURSOS_PERMITIDOS:
        raise ValueError(
            "Percurso inválido. Escolha entre 3, 5, 10, 15, 21 e 42 km."
        )

    return percurso_convertido


def validar_corredor(nome, data_nascimento, telefone, percurso):
    validar_nome(nome)
    validar_data_nascimento(data_nascimento)
    validar_telefone(telefone)

    return validar_percurso(percurso)
