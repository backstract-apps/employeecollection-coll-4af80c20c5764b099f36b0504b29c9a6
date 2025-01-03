from sqlalchemy.orm import Session
from typing import List
from fastapi import UploadFile
import models, schemas
import boto3

from pathlib import Path

async def get_employees(db: Session, id: int):

    employees_all = db.query(models.Employees).all()
    res = {
        'employees_all': employees_all,
    }
    return res

async def get_employees_id(db: Session, id: int):

    employees_one = db.query(models.Employees).filter(models.Employees.id == id).first()
    res = {
        'employees_one': employees_one,
    }
    return res

async def post_employees(db: Session, id: int, name: str, employee_id: str, age: int, username: str, password: str, emaidid: str):

    record_to_be_added = {'id': id, 'name': name, 'employee_id': employee_id, 'age': age, 'username': username, 'password': password}
    new_employees = models.Employees(**record_to_be_added)
    db.add(new_employees)
    db.commit()
    db.refresh(new_employees)
    employees_inserted_record = new_employees


    userid: bool = True



    isuserid: bool = userid



    test: str = "test"



    name: str = username



    userlist = []  # Creating new list



# Add element to the list 'userlist'
    userlist.insert(0, 'username')


   # Remove element(s) from the list 'userlist'
    userlist.pop(0)  # Remove from the front
    userlist.remove('test')  # Remove specific value


    user_records: str = employee_id


    # employee data
    employee_data = []  # Creating new list



# Add element to the list 'employee_data'
    employee_data.insert(0, 'name')
    res = {
        'list_data': userlist,
        'user_test': test,
        'isuserdetails': isuserid,
        'hui': user_records,
    }
    return res

async def put_employees_id(db: Session, id: str, name: str, employee_id: str, age: str, username: str, password: str):

    employees_edited_record = db.query(models.Employees).filter(models.Employees.id == id).first()
    for key, value in {'id': id, 'name': name, 'employee_id': employee_id, 'age': age, 'username': username, 'password': password}.items():
          setattr(employees_edited_record, key, value)
    db.commit()
    db.refresh(employees_edited_record)
    employees_edited_record = employees_edited_record

    res = {
        'employees_edited_record': employees_edited_record,
    }
    return res

async def delete_employees_id(db: Session, name: str):

    employees_deleted = None
    record_to_delete = db.query(models.Employees).filter(models.Employees.name == name).first()

    if record_to_delete:
          db.delete(record_to_delete)
          db.commit()
          employees_deleted = record_to_delete
    res = {
        'employees_deleted': employees_deleted,
    }
    return res

