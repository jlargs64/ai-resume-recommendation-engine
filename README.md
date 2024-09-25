# AI Resume Recommendation Engine

This is an example repo of trying to tie together different skills into the same project. This app will allow users to apply to fictional jobs and rate the match based on natural language processing similar to sites like LinkedIn. I'll be using a combination of spacy + generative AI and LLMs to do this. Additionally, I'm showcasing my cloud development skills with this repository via LocalStack and AWS.

## How to run locally

### Backend

- Ensure you are in the `backend/` directory
- `poetry install --no-root`
- `fastapi dev main.py`

### Frontend

- Ensure you are in the `frontend/` directory
- `npm install`
- `npm run dev`

### Cloud Infrastructure

- `docker-compose up -d`

## Roadmap

- Create MVP of processing resumes in REST requests with Spacy and Langchain
- Implement frontend components for uploading a file
- Save data into sqlite database
  - Create a factory to allow for other relational DB like Postgresql or RDS
- Save data to S3 with LocalStack like resumes or profile pictures
- Seed database with fake job postings
- Add authentication to routes on backend/frontend
- Containerize frontend
- Containerize backend
- Save images to ECR
- Deployments
  - First I want to try a simple deployment with just ECS
- Tie everything together with Cloud Formation for IaaS
