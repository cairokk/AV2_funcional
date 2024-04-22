import unittest
from unittest.mock import patch
import io
import contextlib
import concurrent.futures
from q1_CairoQueiros import (
    create_transaction_debit,
    create_transaction_credit,
    create_cash_payment,
)


class TestPaymentScenarios(unittest.TestCase):
    simulate_transaction = lambda self, inputs, tipo: (
        lambda: self._run_transaction(inputs, tipo)
    )

    def _run_transaction(self, inputs, tipo):
        @patch("builtins.input", side_effect=inputs)
        def inner(mock_input):
            with contextlib.redirect_stdout(io.StringIO()) as f:
                {
                    "credito": create_transaction_credit,
                    "debito": create_transaction_debit,
                    "dinheiro": create_cash_payment,
                }[tipo]()
            return f.getvalue().strip()

        return inner()

    def test_stress_scenario(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = []
            [futures.append(executor.submit(self.simulate_transaction(["1", "100"], "credito"))) for _ in range(10)]
            [futures.append(executor.submit(self.simulate_transaction(["1", "2", "300"], "debito"))) for _ in range(10)]
            [futures.append(executor.submit(self.simulate_transaction(["200"], "dinheiro"))) for _ in range(10)]

            results = [future.result() for future in concurrent.futures.as_completed(futures)]

            transacao_concluida = lambda results: any(
                "Complete Transaction" in result or "Recibo" in result for result in results
            )

            self.assertTrue(
                transacao_concluida(results),
                "Transação falhou ou incompleta",
            )


if __name__ == "__main__":
    unittest.main()
