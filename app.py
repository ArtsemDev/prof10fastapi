from fastapi import FastAPI

from api import api_router


app = FastAPI(
    title='BelHard Professional 10!',
    description='Python Professional Group 10!'
)
app.include_router(router=api_router)
