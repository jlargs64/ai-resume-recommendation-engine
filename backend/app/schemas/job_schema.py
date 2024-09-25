from pydantic import BaseModel


class JobBase(BaseModel):
    title: str
    company: str
    description: str


class JobCreate(JobBase):
    pass
