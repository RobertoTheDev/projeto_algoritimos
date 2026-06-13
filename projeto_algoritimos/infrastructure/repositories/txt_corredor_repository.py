from application.interfaces.corredor_repository import (
    CorredorRepository
)

from domain.entities.corredor import Corredor

class TxtCorredorRepository(CorredorRepository):

    def __init__(self, arquivo_manager):
        self.arquivo_manager = arquivo_manager

    def salvar(self, corredor):
        linhas = self.arquivo_manager.ler_linhas()

        linhas.append(
            corredor.para_linha() + "\n"
        )
        
        self.arquivo_manager.escrever_linhas(linhas)

    def listar(self):
        linhas = self.arquivo_manager.ler_linhas()

        corredores = []

        for linhas in linhas:
            corredores.append(
                Corredor.de_linha(linhas)
            )

        return corredores
    
    def remover(self, nome):
        corredores = self.listar()

        corredores_filtrados = [
            corredor
            for corredor in corredores
            if corredor.nome.lower() != nome.lower()
        ]

        linhas = [
            corredor.para_linha() + "\n"
            for corredor in corredores_filtrados
        ]

        self.arquivo_manager.escrever_linhas(linhas)