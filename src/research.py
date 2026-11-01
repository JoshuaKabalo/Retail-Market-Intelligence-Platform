import json
from pathlib import Path
from scoring import calculate_profit

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "sample_products.json"

with DATA_FILE.open("r", encoding="utf-8") as file:
    products = json.load(file)

results = []

for product in products:
    analysis = calculate_profit(product)
    results.append(analysis)

results.sort(
    key=lambda product: product["estimated_monthly_profit"],
    reverse=True
)

print("\nVELTRIVO RETAIL INTELLIGENCE REPORT")
print("=" * 45)

for index, product in enumerate(results, start=1):
    print(f"\n{index}. {product['name']}")
    print(f"   Profit per unit: ${product['profit_per_unit']:.2f}")
    print(f"   Contribution margin: {product['profit_margin']:.2f}%")
    print(
        f"   Estimated monthly contribution: "
        f"${product['estimated_monthly_profit']:.2f}"
    )
