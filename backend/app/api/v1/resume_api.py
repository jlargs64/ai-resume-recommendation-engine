from typing import Annotated

import PyPDF2
from fastapi import APIRouter, File, Form, HTTPException, UploadFile, status

from app.core.logger import get_logger

resume_api_router_v1 = APIRouter("/v1/resume")
logger = get_logger()


@resume_api_router_v1.post("/")
async def create_resume(
    resume_file: Annotated[UploadFile, File()],
    file_name: Annotated[str, Form()],
):
    try:
        # Ensure the uploaded file is a PDF
        if resume_file.content_type != "application/pdf":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="File must be a PDF"
            )
        # Save to S3
        # Save to DB
        # Read the file
        content = await resume_file.read()

        # Use PyPDF2 to read the PDF
        pdf_reader = PyPDF2.PdfReader(content)

        # Extract text from each page
        pdf_text = ""
        for page in pdf_reader.pages:
            pdf_text += page.extract_text()
        # Todo: spacy to get job keywords and save them in resume
        return {"contents": pdf_text}
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
