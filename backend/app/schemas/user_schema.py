from pydantic import BaseModel

from app.models.resume import Resume


class UserBase(BaseModel):
    email: str
    name: str
    profile_pic_url: str | None = None


class UserCreate(UserBase):
    plain_text_password: str


class User(UserBase):
    id: int
    resumes: list[Resume] = []

    class Config:
        orm_mode = True
