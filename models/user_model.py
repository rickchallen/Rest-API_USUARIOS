from pydantic import BaseModel, EmailStr
from typing import Optional, List

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    is_active: bool

class Pagination(BaseModel):
    page: int
    page_size: int
    total: int
    
class UserListResponse(BaseModel):
    data: List[User]
    pagination: Pagination

class ErrorResponse(BaseModel):
    error: str
    message: str