
import sys
import unittest
from pathlib import Path
from unittest.mock import Mock

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "projeto_algoritimos"),
)

from application.use_cases.inscrever_corredor import InscreverCorredor
from application.use_cases.listar_corredores import ListarCorredores
from application.use_cases.listar_por_percurso import ListarPorPercurso
from application.use_cases.remover_corredor import RemoverCorredor
from domain.entities.corredor import Corredor


class TestInscreverCorredor(unittest.TestCase):
    def setUp(self):
        self.repository = Mock()
        self.caso_de_uso = InscreverCorredor(self.repository)

    def test_inscreve_corredor_valido(self):
        corredor = self.caso_de_uso.executar(
            "Roberto",
            "15/05/2002",
            "88999999999",
            10,
        )

        self.assertIsInstance(corredor, Corredor)
        self.assertEqual(corredor.nome, "Roberto")
        self.assertEqual(corredor.percurso, 10)

        self.repository.salvar.assert_called_once_with(corredor)

    def test_nao_persiste_corredor_com_nome_vazio(self):
        with self.assertRaises(ValueError):
            self.caso_de_uso.executar(
                "",
                "15/05/2002",
                "88999999999",
                10,
            )

        self.repository.salvar.assert_not_called()

    def test_nao_persiste_corredor_com_percurso_invalido(self):
        with self.assertRaises(ValueError):
            self.caso_de_uso.executar(
                "Roberto",
                "15/05/2002",
                "88999999999",
                7,
            )

        self.repository.salvar.assert_not_called()


class TestListarCorredores(unittest.TestCase):
    def setUp(self):
        self.repository = Mock()
        self.caso_de_uso = ListarCorredores(self.repository)

    def test_lista_corredores_em_ordem_alfabetica(self):
        corredores = [
            Corredor("Roberto", "15/05/2002", "88999999999", 10),
            Corredor("Ana", "10/03/2001", "88988888888", 5),
            Corredor("Bruno", "20/07/2000", "88977777777", 21),
        ]

        self.repository.listar.return_value = corredores

        resultado = self.caso_de_uso.executar()

        self.assertEqual(
            [corredor.nome for corredor in resultado],
            ["Ana", "Bruno", "Roberto"],
        )
        self.repository.listar.assert_called_once_with()

    def test_lista_vazia_quando_nao_ha_corredores(self):
        self.repository.listar.return_value = []

        resultado = self.caso_de_uso.executar()

        self.assertEqual(resultado, [])


class TestRemoverCorredor(unittest.TestCase):
    def setUp(self):
        self.repository = Mock()
        self.caso_de_uso = RemoverCorredor(self.repository)

    def test_solicita_remocao_pelo_nome(self):
        self.caso_de_uso.executar("Roberto")

        self.repository.remover.assert_called_once_with("Roberto")

    def test_encaminha_nome_sem_alteracao(self):
        self.caso_de_uso.executar("roberto")

        self.repository.remover.assert_called_once_with("roberto")


class TestListarPorPercurso(unittest.TestCase):
    def setUp(self):
        self.repository = Mock()
        self.caso_de_uso = ListarPorPercurso(self.repository)

    def test_retorna_apenas_corredores_do_percurso(self):
        corredores = [
            Corredor("Roberto", "15/05/2002", "88999999999", 10),
            Corredor("Ana", "10/03/2001", "88988888888", 5),
            Corredor("Bruno", "20/07/2000", "88977777777", 10),
        ]

        self.repository.listar.return_value = corredores

        resultado = self.caso_de_uso.executar(10)

        self.assertEqual(
            [corredor.nome for corredor in resultado],
            ["Roberto", "Bruno"],
        )

    def test_retorna_lista_vazia_quando_nao_ha_corredores_no_percurso(self):
        corredores = [
            Corredor("Ana", "10/03/2001", "88988888888", 5),
        ]

        self.repository.listar.return_value = corredores

        resultado = self.caso_de_uso.executar(42)

        self.assertEqual(resultado, [])


if __name__ == "__main__":
    unittest.main()
