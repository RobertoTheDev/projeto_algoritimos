import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "projeto_algoritimos"),
)

from domain.entities.corredor import Corredor
from infrastructure.persistence.arquivo_manager import ArquivoManager
from infrastructure.repositories.txt_corredor_repository import (
    TxtCorredorRepository,
)


class TestTxtCorredorRepository(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)

        self.caminho = Path(self.temp_dir.name) / "corredores.txt"
        self.arquivo_manager = ArquivoManager(self.caminho)
        self.repository = TxtCorredorRepository(self.arquivo_manager)

    def criar_corredor(
        self,
        nome="Roberto",
        data_nascimento="15/05/2002",
        telefone="88999999999",
        percurso=10,
    ):
        return Corredor(
            nome,
            data_nascimento,
            telefone,
            percurso,
        )

    def test_lista_vazia_quando_arquivo_nao_existe(self):
        resultado = self.repository.listar()

        self.assertEqual(resultado, [])

    def test_salva_corredor_no_arquivo(self):
        corredor = self.criar_corredor()

        self.repository.salvar(corredor)

        self.assertEqual(
            self.caminho.read_text(encoding="utf-8"),
            "Roberto;15/05/2002;88999999999;10\n",
        )

    def test_lista_corredores_salvos(self):
        primeiro = self.criar_corredor()
        segundo = self.criar_corredor(
            nome="Ana",
            data_nascimento="10/03/2001",
            telefone="88988888888",
            percurso=5,
        )

        self.repository.salvar(primeiro)
        self.repository.salvar(segundo)

        resultado = self.repository.listar()

        self.assertEqual(
            [corredor.nome for corredor in resultado],
            ["Roberto", "Ana"],
        )

    def test_ignora_linhas_invalidas_ao_listar(self):
        self.caminho.write_text(
            "Roberto;15/05/2002;88999999999;10\n"
            "registro inválido\n"
            "Ana;10/03/2001;88988888888;5\n"
            "Bruno;data-inválida;88977777777;10\n",
            encoding="utf-8",
        )

        resultado = self.repository.listar()

        self.assertEqual(
            [corredor.nome for corredor in resultado],
            ["Roberto", "Ana"],
        )

    def test_remove_corredor_sem_diferenciar_maiusculas(self):
        self.repository.salvar(self.criar_corredor("Roberto"))
        self.repository.salvar(
            self.criar_corredor(
                nome="Ana",
                data_nascimento="10/03/2001",
                telefone="88988888888",
                percurso=5,
            )
        )

        self.repository.remover("roberto")

        resultado = self.repository.listar()

        self.assertEqual(
            [corredor.nome for corredor in resultado],
            ["Ana"],
        )

    def test_preserva_outros_corredores_ao_remover(self):
        for nome, data, telefone, percurso in [
            ("Roberto", "15/05/2002", "88999999999", 10),
            ("Ana", "10/03/2001", "88988888888", 5),
            ("Bruno", "20/07/2000", "88977777777", 21),
        ]:
            self.repository.salvar(
                self.criar_corredor(nome, data, telefone, percurso)
            )

        self.repository.remover("Ana")

        resultado = self.repository.listar()

        self.assertEqual(
            [corredor.nome for corredor in resultado],
            ["Roberto", "Bruno"],
        )

    def test_remover_nome_inexistente_preserva_corredores(self):
        self.repository.salvar(self.criar_corredor())

        self.repository.remover("Pessoa inexistente")

        resultado = self.repository.listar()

        self.assertEqual(
            [corredor.nome for corredor in resultado],
            ["Roberto"],
        )

    def test_salva_corredor_quando_ultima_linha_nao_tem_quebra(self):
        self.caminho.write_text(
            "Ana;10/03/2001;88988888888;5",
            encoding="utf-8",
        )

        self.repository.salvar(self.criar_corredor())

        linhas = self.caminho.read_text(encoding="utf-8").splitlines()

        self.assertEqual(len(linhas), 2)
        self.assertEqual(
            linhas[0],
            "Ana;10/03/2001;88988888888;5",
        )
        self.assertEqual(
            linhas[1],
            "Roberto;15/05/2002;88999999999;10",
        )


if __name__ == "__main__":
    unittest.main()
