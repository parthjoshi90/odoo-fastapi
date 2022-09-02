
from fastapi import APIRouter
from api.endpoints.partner import router as partner_routes
from api.endpoints.products import router as product_routes
from api.endpoints.company import router as company_routes

router = APIRouter()

router.include_router(partner_routes)
router.include_router(product_routes)
router.include_router(company_routes)