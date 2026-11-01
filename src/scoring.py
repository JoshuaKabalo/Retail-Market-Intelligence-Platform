def calculate_profit(product):
    required_fields = [
        "name",
        "price",
        "manufacturing_cost",
        "shipping_cost",
        "amazon_fees",
        "estimated_monthly_sales"
    ]

    for field in required_fields:
        if field not in product:
            raise ValueError(f"Missing required field: {field}")

    price = product["price"]

    if not isinstance(price, (int, float)) or isinstance(price, bool) or price <= 0:
        raise ValueError("Product price must be a positive number")

    for field in [
        "manufacturing_cost",
        "shipping_cost",
        "amazon_fees",
        "estimated_monthly_sales"
    ]:
        value = product[field]
        if not isinstance(value, (int, float)) or isinstance(value, bool) or value < 0:
            raise ValueError(f"{field} must be a non-negative number")

    manufacturing = product["manufacturing_cost"]
    shipping = product["shipping_cost"]
    amazon_fees = product["amazon_fees"]

    profit = price - manufacturing - shipping - amazon_fees
    margin = (profit / price) * 100

    return {
        "name": product["name"],
        "profit_per_unit": round(profit, 2),
        "profit_margin": round(margin, 2),
        "estimated_monthly_profit": round(
            profit * product["estimated_monthly_sales"], 2
        )
    }
