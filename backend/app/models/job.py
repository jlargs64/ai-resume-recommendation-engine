from sqlalchemy import Column, Integer, String

from app.core.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    company = Column(String)
    skills = Column(
        String,
    )
    description = Column(
        String,
    )
