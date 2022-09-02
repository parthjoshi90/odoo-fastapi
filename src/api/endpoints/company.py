from fastapi import APIRouter,Depends, Query
from service.company_service import get_companies, get_company_by_id
from odoo.env import odoo_env
from odoo.api import Environment
from schema.filters.company_filter import CompanyFilters

router = APIRouter()


def get_company_filter(
    limit: int = Query(5, ge=1),
    offset: int = Query(0, ge=0)
):
    return CompanyFilters(
        limit=limit,
        offset=offset
    )

@router.get("/companies", tags=["Res Companies"])
def list_companies(
    filters: CompanyFilters = Depends(get_company_filter),
    env: Environment = Depends(odoo_env)
    ):
    comapnies = get_companies(
        env,
        limit=filters.limit,
        offset= filters.offset
    )
    return comapnies

@router.get("/comapny/{company_id}", tags=["Res Companies"])
def get_comapny(company_id: int, env: Environment = Depends(odoo_env)):
    company = get_company_by_id(env, company_id)
    return company
