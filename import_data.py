from weddingapp.models import Product
import logging
import json

logging.basicConfig(format="[%(asctime)s] %(levelname)s Imports: %(message)s",
                    filename="imports.log",
                    level=logging.INFO)

with open("products.json") as f:
    data = json.load(f)


def import_data(products=data):
    """
    Import products.json to database.
    """
    for prod in products:
        Product.objects.get_or_create(
            name=prod["name"],
            brand=prod["brand"],
            price="".join(filter(lambda i: not i.isalpha(), prod["price"])),
            stock=prod["in_stock_quantity"],
        )


logging.info("Data imported.")
