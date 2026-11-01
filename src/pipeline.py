import json
import os

import boto3

from scoring import calculate_profit


def lambda_handler(event, context):
    bucket = os.environ["RESEARCH_BUCKET"]
    s3 = boto3.client("s3")

    response = s3.get_object(
        Bucket=bucket,
        Key="input/sample_products.json"
    )

    products = json.loads(
        response["Body"].read().decode("utf-8")
    )

    results = [
        calculate_profit(product)
        for product in products
    ]

    results.sort(
        key=lambda item: item["estimated_monthly_profit"],
        reverse=True
    )

    report = {
        "product_count": len(results),
        "products": results
    }

    s3.put_object(
        Bucket=bucket,
        Key="reports/research_report.json",
        Body=json.dumps(report, indent=2),
        ContentType="application/json"
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Research report generated",
            "products_processed": len(results)
        })
    }
