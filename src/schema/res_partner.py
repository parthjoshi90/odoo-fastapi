from pydantic import BaseModel,Field
from typing import Dict, List, Optional
from odoo.models import Model
from typing import ForwardRef

ChildPartner = ForwardRef('ResPartner')

class User(BaseModel):
    id: Optional[int]
    name: str


class ResPartner(BaseModel):
    id: Optional[int]
    name: str
    email: Optional[str]
    is_company: bool
    type: Optional[str]
    ref: Optional[str]
    lang: Optional[str]
    tz: Optional[str]
    vat: Optional[str]
    employee: bool
    user_id: User = None
    child_ids: List[ChildPartner] = None

    @classmethod
    def from_res_partner(cls, p: Model) -> "ResPartner":
        return ResPartner(
            id=p.id,
            name=p.name,
            email=p.email,
            is_company=p.is_company,
            type=p.type,
            ref=p.ref,
            lang=p.lang,
            tz=p.tz,
            vat=p.vat,
            employee=p.employee,
            user_id= User(id=p.user_id.id,name=p.user_id.name),
            child_ids= [ResPartner.from_res_partner(c) for c in p.child_ids]
        )

ResPartner.update_forward_refs()
