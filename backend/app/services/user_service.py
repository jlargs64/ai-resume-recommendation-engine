from logging import Logger
from typing import List

from argon2 import PasswordHasher
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.logger import get_logger
from app.models.user import User
from app.schemas.user_schema import UserCreate


class UserService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.password_hasher = PasswordHasher()
        self.logger = get_logger("UserService")

    def get_user(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def get_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        # Todo: add pagination
        return self.db.query(User).offset(skip).limit(limit).all()

    def create_user(self, user: UserCreate) -> User:
        try:
            hashed_password = self.password_hasher.hash(user.plain_text_password)
            profile_pic_url = (
                user.profile_pic_url
                if len(profile_pic_url) > 0 or profile_pic_url is not None
                else ""
            )
            db_user = User(
                email=user.email,
                name=user.name,
                hashed_password=hashed_password,
                profile_pic_url=profile_pic_url,
            )
            self.db.add(db_user)
            self.db.commit()
            self.db.refresh()
            return db_user
        except Exception as e:
            self.logger.exception(e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db)
