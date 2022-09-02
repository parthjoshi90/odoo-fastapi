# -*- coding: utf-8 -*-

from fastapi import APIRouter, Depends
from service.product_service import get_products
from odoo.env import odoo_env
from odoo.api import Environment
router = APIRouter()


@router.get("/products", tags=["Product Variant"])
async def get_all_products(env: Environment = Depends(odoo_env)):
    products = get_products(env)
    return products
