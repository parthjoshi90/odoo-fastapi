# -*- coding: utf-8 -*-

from typing import List
from schema.product import Product
from odoo.api import Environment


def get_products(env: Environment) -> List[Product]:
    products = env["product.product"].search([])
    return [Product.from_product_product(p) for p in products]
