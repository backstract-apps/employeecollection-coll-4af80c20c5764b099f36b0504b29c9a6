from fastapi import APIRouter, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/employees/')
async def get_employees( id: int , db: Session = Depends(get_db)):
    return await service.get_employees(db , id)

@router.get('/employees/id')
async def get_employees_id( id: int , db: Session = Depends(get_db)):
    return await service.get_employees_id(db , id)

@router.post('/employees/')
async def post_employees( id: int, name: str, employee_id: str, age: int, username: str, password: str, emaidid: str , db: Session = Depends(get_db)):
    return await service.post_employees(db , id, name, employee_id, age, username, password, emaidid)

@router.put('/employees/id/')
async def put_employees_id( id: str, name: str, employee_id: str, age: str, username: str, password: str , db: Session = Depends(get_db)):
    return await service.put_employees_id(db , id, name, employee_id, age, username, password)

@router.delete('/employees/id')
async def delete_employees_id( name: str , db: Session = Depends(get_db)):
    return await service.delete_employees_id(db , name)

