# -*- coding: utf-8 -*-

from fastapi import APIRouter, Depends, Query
from service.partner_service import get_partners, get_partner_by_id
from schema.filters.partner_filter import PartnerFilter
from typing import Optional
from odoo.env import odoo_env
from odoo.api import Environment
router = APIRouter()

def get_partner_filters(
    is_company: Optional[bool] = None,
    limit: int = Query(5, ge=1),
    offset: int = Query(0, ge=0),
) -> PartnerFilter:
    return PartnerFilter(
        is_company=is_company,
        limit=limit,
        offset=offset,
    )


@router.get("/partners", tags=["ResPartner"])
def get_all_partners(
    filters: PartnerFilter = Depends(get_partner_filters),
    env: Environment = Depends(odoo_env)
    ):
    partners = get_partners(
        env,
        is_company=filters.is_company,
        limit = filters.limit,
        offset = filters.offset
    )
    return partners

@router.get("/partner/{partner_id}", tags=["ResPartner"])
def get_partner(
    partner_id: int,
    env: Environment = Depends(odoo_env)
    ):
    partners = get_partner_by_id(env, partner_id)
    return partners
