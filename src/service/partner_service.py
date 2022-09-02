from typing import List
from schema.res_partner import ResPartner
from odoo.api import Environment
from odoo.exceptions import MissingError
from fastapi.exceptions import HTTPException

def get_partners(
    env: Environment,
    is_company=None,
    limit=5,
    offset=0
    ) -> List[ResPartner]:
    domain = [('is_company','=',is_company)]
    partner_ids = env["res.partner"].search(domain, offset=offset, limit=limit)
    return [ResPartner.from_res_partner(partner_id) for partner_id in partner_ids]


def get_partner_by_id(env: Environment, partner_id) -> ResPartner:
    try:
        partner_id = env["res.partner"].browse([partner_id])
        return ResPartner.from_res_partner(partner_id)
    except MissingError as error:
        raise HTTPException(status_code=400, detail=f"Partner With Id {partner_id.id} does not found.")
