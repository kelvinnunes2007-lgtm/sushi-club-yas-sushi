
import unittest

from sushi_club import (
    clientes,
    solicitacoes,
    cadastrar_cliente,
    registrar_compra,
    solicitar_recompensa
)


class TestRecompensas(unittest.TestCase):

    def setUp(self):
        clientes.clear()
        solicitacoes.clear()

        cadastrar_cliente(
            "Cliente Teste",
            "teste@exemplo.com"
        )

        registrar_compra(
            "teste@exemplo.com", 1120
        )

    def test_recompensa_disponivel(self):
        pedido = solicitar_recompensa(
            "teste@exemplo.com",
            "Temaki Promocional"
        )

        self.assertEqual(
            pedido["status"],
            "aguardando aprovacao"
        )
        self.assertEqual(
            clientes["teste@exemplo.com"]["pontos"],
            112
        )

    def test_saldo_insuficiente(self):
        resultado = solicitar_recompensa(
            "teste@exemplo.com",
            "Combinado Especial"
        )

        self.assertEqual(
            resultado["status"],
            "saldo insuficiente"
        )


if __name__ == "__main__":
    unittest.main()
