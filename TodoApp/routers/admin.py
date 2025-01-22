from fastapi import APIRouter, Depends, HTTPException, Path, Query
from starlette import status
from typing import Annotated
from sqlalchemy.orm import Session
# import models
from ..models import Todos
from ..database import engine, SessionLocal
from pydantic import BaseModel, Field, ConfigDict
# from routers import auth
from .auth import get_current_user

router = APIRouter(
    prefix='/admin',
    tags=['admin'])

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

# from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
# from jose import jwt, JWTError
# oauth2_bearer = OAuth2PasswordBearer(tokenUrl = 'auth/token')
# SECRET_KEY = 'b903c10a1ebd7ed293bba9a497dea7b46863042092e79cf5c8fd0f9c7f068b28'
# ALGORITHM = 'HS256'

# async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get('sub')
#         user_id: int = payload.get('id')
#         user_role: str = payload.get('role')
#         if username is None or user_id is None:
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = 'Could not validate user.')
        
#         return {'username': username, 'id': user_id, 'user_role': user_role}
#     except JWTError:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail = 'Could not validate user.')


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict,Depends(get_current_user)]


@router.get("/todo", status_code = status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code = 401, detail = 'Authentication failed')
    return db.query(Todos).all()

@router.delete("/todo/{todo_id}", status_code = status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code = 401, detail = 'Authentication failed')
    
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()

    if todo_model is None:
        raise HTTPException(status_code = 404, detail = 'Todo not found.')
    
    db.query(Todos).filter(Todos.id == todo_id).delete()

    db.commit()