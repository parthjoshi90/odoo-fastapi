
from schema.res_company import ResCompany
from odoo.api import Environment
from odoo.exceptions import MissingError
from typing import List
from fastapi import HTTPException


def get_companies(
    env: Environment,
    limit=5,
    offset=0
    ) -> List[ResCompany]:
    company_ids = env["res.company"].search([], offset=offset, limit=limit)
    return [ResCompany.from_res_company(company_id) for company_id in company_ids]


def get_company_by_id(env: Environment, company_id) -> ResCompany:
    try:
        company_id = env["res.company"].browse([company_id])
        return ResCompany.from_res_company(company_id)
    except MissingError as error:
        raise HTTPException(status_code=400, detail=f"Company With Id {company_id.id} does not found.")
