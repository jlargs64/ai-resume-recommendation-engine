from fastapi import APIRouter, Depends

from app.services.job_service import create_job, delete_job, get_job, update_job

# from app.models.job_models import JobCreate, JobResponse

# router = APIRouter()

# @router.post("/jobs/", response_model=JobResponse)
# async def create_job_route(job: JobCreate):
#     return create_job(job)

# @router.get("/jobs/{job_id}", response_model=JobResponse)
# async def get_job_route(job_id: int):
#     return get_job(job_id)

# You would include update and delete routes here too
