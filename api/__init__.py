from fastapi import APIRouter

from .apiv1 import api_v1_router


api_router = APIRouter(prefix='/api')
api_router.include_router(router=api_v1_router)
