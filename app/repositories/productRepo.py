from fastapi import Response, status, HTTPException, Depends
from ..utils.model import *
from ..pydantic_schemas.product import *
from sqlalchemy.orm import Session
from ..db.database import get_db
from typing import Dict



def allProduct(db: Session):
    return get_allProducts(db=db)


def newProduct(db: Session, prod:ProdCreate):
    return create_new_product(db=db, prod=prod)


def singleProduct(id: int, db: Session):
    products = get_single_product(id=id, db=db)
    
    if not products:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Product not found!")
    
    return products