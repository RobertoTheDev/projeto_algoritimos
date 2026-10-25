import sys
import unittest
from pathlib import Path


sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "projeto_algoritimos"),
)

from domain.entities.corredor import Corredor


class TestCorredor(unittest.TestCase):
    def test_cria_corredor_valido(self):
        corredor = Corredor(
            "Roberto",
            "15/05/2002",
            "88999999999",
            10,
        )

        self.assertEqual(corredor.nome, "Roberto")
        self.assertEqual(corredor.percurso, 10)

    def test_rejeita_nome_vazio(self):
        with self.assertRaises(ValueError):
            Corredor("", "15/05/2002", "88999999999", 10)

    def test_rejeita_data_invalida(self):
        with self.assertRaises(ValueError):
            Corredor(
                "Roberto",
                "31/02/2002",
                "88999999999",
                10,
            )

    def test_rejeita_data_futura(self):
        with self.assertRaises(ValueError):
            Corredor(
                "Roberto",
                "15/05/2099",
                "88999999999",
                10,
            )

    def test_rejeita_telefone_com_letras(self):
        with self.assertRaises(ValueError):
            Corredor(
                "Roberto",
                "15/05/2002",
                "88999abc999",
                10,
            )

    def test_rejeita_percurso_nao_permitido(self):
        with self.assertRaises(ValueError):
            Corredor(
                "Roberto",
                "15/05/2002",
                "88999999999",
                7,
            )

    def test_rejeita_percurso_nao_numerico(self):
        with self.assertRaises(ValueError):
            Corredor(
                "Roberto",
                "15/05/2002",
                "88999999999",
                "dez",
            )

    def test_carrega_registro_valido(self):
        corredor = Corredor.de_linha(
            "Roberto;15/05/2002;88999999999;10"
        )

        self.assertIsNotNone(corredor)
        self.assertEqual(corredor.percurso, 10)

    def test_ignora_registro_corrompido(self):
        corredor = Corredor.de_linha(
            "Roberto;15/05/2002;88999999999;abc"
        )

        self.assertIsNone(corredor)

    def test_ignora_registro_com_campos_insuficientes(self):
        corredor = Corredor.de_linha("Roberto;15/05/2002")

        self.assertIsNone(corredor)


if __name__ == "__main__":
    unittest.main()