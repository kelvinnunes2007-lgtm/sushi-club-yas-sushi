
import unittest
from sushi_club import (
    clientes,
    cadastrar_cliente,
    consultar_pontos,
    registrar_compra
)


class TestSushiClub(unittest.TestCase):

    def setUp(self):
        clientes.clear()
        cadastrar_cliente(
            "Cliente Teste",
            "teste@exemplo.com"
        )

    def test_cadastro(self):
        self.assertEqual(
            consultar_pontos("teste@exemplo.com"),
            0
        )

    def test_pontos_compra(self):
        resultado = registrar_compra(
            "teste@exemplo.com", 80
        )
        self.assertEqual(resultado["pontos_gerados"], 8)
        self.assertEqual(resultado["saldo_atual"], 8)

    def test_compra_invalida(self):
        with self.assertRaises(ValueError):
            registrar_compra(
                "teste@exemplo.com", -10
            )


if __name__ == "__main__":
    unittest.main()
