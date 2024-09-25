from contextlib import asynccontextmanager
from typing import Literal, Union

from fastapi import FastAPI

from app.core.database import Base, engine
from app.core.logger import get_logger

logger = get_logger()
# Create DB tables
Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Server ready!")
    # Seed data
    yield
    # Clean up


app = FastAPI(lifespan=lifespan)


@app.get("/health")
def health_check() -> Literal["OK"]:
    return "OK"


# Auth Router
# User Router
# Job Router
@app.post("/resumes/process")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
