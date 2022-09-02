from pydantic import BaseModel
from schema.res_company import ResCompany
from typing import List, Optional, ForwardRef
from odoo.models import Model


ParentCategory = ForwardRef('ProductCategory')

class ProductCategory(BaseModel):
    id: str
    name: str
    parent_id: Optional[ParentCategory] = None
    parent_path: str

    @classmethod
    def from_product_category(cls, category : Model) -> "ProductCategory":
        return ProductCategory (
            id=category.id,
            name=category.name,
            parent_path=category.parent_path,
            parent_id=ProductCategory.from_product_category(category.parent_id) if category.parent_id else None
        )

ProductCategory.update_forward_refs()

class Product(BaseModel):
    id: str
    name: str
    default_code: str
    list_price: float
    categ_id: ProductCategory

    @classmethod
    def from_product_product(cls, product : Model) -> "Product":
        return Product(
            id=product.id,
            name=product.display_name,
            default_code=product.default_code,
            list_price=product.lst_price,
            categ_id=ProductCategory.from_product_category(product.categ_id)
        )