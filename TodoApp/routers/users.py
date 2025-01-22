from fastapi import APIRouter, Depends, HTTPException, Path, Query
from starlette import status
from typing import Annotated
from sqlalchemy.orm import Session
# import models
from ..models import Todos, Users
from ..database import engine, SessionLocal
from pydantic import BaseModel, Field, ConfigDict
# from routers import auth
from .auth import get_current_user
from passlib.context import CryptContext




router = APIRouter(
    prefix='/users',
    tags=['users'])

# router.include_router(auth.router)

# models.Base.metadata.create_all(bind=engine)

'''
sqlite3 todos.db w ps
.mode box <- lepiej kolumna wyglada w sqllite3
.mode table
.mode markdown
'''

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict,Depends(get_current_user)]
bcrypt_context =  CryptContext(schemes=['bcrypt'], deprecated = 'auto')

class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length = 6)

@router.get("/", status_code = status.HTTP_200_OK)
async def get_user_informations(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code = 401, detail = 'Authentication failed')
    return db.query(Users).filter(Users.id == user.get('id')).first()

@router.put("/password", status_code = status.HTTP_204_NO_CONTENT)
async def change_password(user: user_dependency, db: db_dependency, user_verification: UserVerification):
    if user is None:
        raise HTTPException(status_code = 401, detail = 'Authentication failed')
    user_model = db.query(Users).filter(Users.id == user.get('id')).first()

    if not bcrypt_context.verify(user_verification.password, user_model.hashed_password):
        raise HTTPException(status_code = 401, detail = 'Error on password change')
    
    user_model.hashed_password = bcrypt_context.hash(user_verification.new_password)

    db.add(user_model)

    db.commit()