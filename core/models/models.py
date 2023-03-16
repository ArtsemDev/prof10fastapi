from sqlalchemy import Column, VARCHAR

from .base import Base


class Category(Base):
    name: str = Column(VARCHAR(64), unique=True, nullable=False)

    def __repr__(self) -> str:
        return self.name
