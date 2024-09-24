from sqlalchemy import Column, Integer, String

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    name = Column(
        String,
    )
    profile_pic_url = Column(
        String,
    )
    hashed_password = Column(String)
