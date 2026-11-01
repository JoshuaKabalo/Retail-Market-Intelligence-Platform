import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from scoring import calculate_profit


class TestProductScoring(unittest.TestCase):

    def test_profit_calculation(self):
        product = {
            "name": "Test Product",
            "price": 30.00,
            "manufacturing_cost": 6.00,
            "shipping_cost": 2.00,
            "amazon_fees": 9.00,
            "estimated_monthly_sales": 100
        }

        result = calculate_profit(product)

        self.assertEqual(result["profit_per_unit"], 13.00)
        self.assertEqual(result["profit_margin"], 43.33)
        self.assertEqual(
            result["estimated_monthly_profit"], 1300.00
        )

    def test_zero_price(self):
        product = {
            "name": "Invalid Product",
            "price": 0,
            "manufacturing_cost": 0,
            "shipping_cost": 0,
            "amazon_fees": 0,
            "estimated_monthly_sales": 100
        }

        with self.assertRaises(ValueError):
            calculate_profit(product)


if __name__ == "__main__":
    unittest.main()
