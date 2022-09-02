
from pydantic import BaseModel
from typing import List,Optional
from odoo.models import Model

class ResCurrency(BaseModel):
    id:int
    name:str

    @classmethod
    def from_res_currency(cls, currency: Model) -> "ResCurrency":
        return ResCurrency (
            id = currency.id,
            name = currency.name
        )


class ResCompany(BaseModel):
    id: int
    name: str
    partner_id: int
    currency_id: ResCurrency = None
    phone: Optional[str]
    email: Optional[str]
    mobile: Optional[str]

    @classmethod
    def from_res_company(cls, company: Model) -> "ResCompany":
        return ResCompany(
            id = company.id,
            name = company.name,
            partner_id= company.partner_id.id,
            currency = ResCurrency.from_res_currency(company.currency_id),
            phone = company.phone,
            mobile = company.mobile,
            email = company.email
        )
