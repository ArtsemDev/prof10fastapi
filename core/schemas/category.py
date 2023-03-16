from pydantic import BaseModel, Field
# from pydantic.types import Decimal


class CategoryCreateForm(BaseModel):
    name: str = Field(
        title='Category Name',
        description='Category Name',
        max_length=64
    )


class CategoryDetail(CategoryCreateForm):
    id: int = Field(
        title='Category ID',
        description='Category Unique ID',
        ge=1
    )

    class Config:
        orm_mode = True
