from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Employees(BaseModel):
    id: int
    name: str
    employee_id: str
    age: int
    username: str
    password: str


class ReadEmployees(BaseModel):
    id: int
    name: str
    employee_id: str
    age: int
    username: str
    password: str
    class Config:
        from_attributes = True


