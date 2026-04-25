from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str
    role: str
    institution_id: int

class UserResponse(BaseModel):
    id: int
    email: str
    role: str
    institution_id: int

    class Config:
        from_attributes = True