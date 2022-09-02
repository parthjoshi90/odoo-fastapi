from pydantic import BaseModel, Field


class BaseFilter(BaseModel):
    limit: int = Field(80, ge=1)
    offset: int = Field(0, ge=0)
