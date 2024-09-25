from fastapi import File
from pydantic import BaseModel


class ResumeBase(BaseModel):
    file_url: str
    text: str


class ResumeCreate(BaseModel):
    file: File
    owner_id: int


class Resume(ResumeBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
