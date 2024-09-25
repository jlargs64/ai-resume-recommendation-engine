from logging import Logger
from typing import List

import PyPDF2
from fastapi import Depends, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.logger import get_logger
from app.models.resume import Resume
from app.schemas.resume_schema import ResumeCreate


class ResumeService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.logger = get_logger("ResumeService")

    async def create_resume(self, resume: ResumeCreate) -> Resume:
        try:

            resume_text: str = await self.process_resume(resume.file)
            self.logger.info(resume_text)
            # Todo: Save to S3
            s3_url = ""
            db_resume = Resume(
                file_url=s3_url, text=resume_text, owner_id=resume.owner_id
            )
            self.db.add(db_resume)
            self.db.commit()
            self.db.refresh()
            return db_resume
        except Exception as e:
            self.logger.exception(e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_resume(self, resume_id: int) -> Resume | None:
        return self.db.query(Resume).filter(Resume.id == resume_id).first()

    def get_resume_by_user(self, user_id: int) -> List[Resume]:
        # Todo: add pagination
        return self.db.query(Resume).filter(Resume.owner_id == user_id).all()

    async def process_resume(self, resume_file: UploadFile) -> str:
        # Read the file
        content = await resume_file.read()

        # Use PyPDF2 to read the PDF
        pdf_reader = PyPDF2.PdfReader(content)

        # Extract text from each page
        pdf_text = ""
        for page in pdf_reader.pages:
            pdf_text += page.extract_text()
        return pdf_text


def get_resume_service(db: Session = Depends(get_db)) -> ResumeService:
    return ResumeService(db)
