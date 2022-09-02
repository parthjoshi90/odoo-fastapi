from schema.filters.base_filter import BaseFilter
from typing import Optional


class PartnerFilter(BaseFilter):
    is_company: Optional[bool]
