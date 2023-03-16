from fastapi import APIRouter, HTTPException, status, Query, Header, Form
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from core.models import Category
from core.schemas import CategoryDetail, CategoryCreateForm


category_router = APIRouter(prefix='/category')


@category_router.get('/', response_model=list[CategoryDetail])
async def categories_list():
    categories = await Category.select(select(Category).order_by(Category.id))
    return [CategoryDetail.from_orm(category) for category in categories]


@category_router.post('/', response_model=CategoryDetail, status_code=status.HTTP_201_CREATED)
async def create_category(category_form: CategoryCreateForm):
    category = Category(**category_form.dict())
    try:
        await category.save()
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='category exist')
    return CategoryDetail.from_orm(category)


@category_router.put('/', response_model=CategoryDetail, status_code=status.HTTP_202_ACCEPTED)
async def update_category(category_detail: CategoryDetail):
    category = await Category.get(category_detail.id)
    if category:
        category.name = category_detail.name
        try:
            await category.save()
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='category exist')
        return category_detail
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='category not found')


@category_router.get('/{category_id}', response_model=CategoryDetail)
async def get_category(
        category_id: int = Query(
            title='Category ID',
            description='Category Unique ID',
            ge=1
        )
):
    category = await Category.get(category_id)
    if category:
        return CategoryDetail.from_orm(category)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='category not found')


@category_router.delete('/{category_id}', status_code=status.HTTP_202_ACCEPTED)
async def delete_category(
        category_id: int = Query(
            title='Category ID',
            description='Category Unique ID',
            ge=1
        )
):
    category = await Category.get(category_id)
    if category:
        await category.delete()
        return {'detail': 'category delete successfully'}
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='category not found')


@category_router.post('/form')
async def form_endpoint(username: str = Form(), password: str = Form()):
    print(username)
    print(password)
    return {'detail': 'OK'}
