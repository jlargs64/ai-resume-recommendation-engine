from typing import Literal, Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health_check() -> Literal["OK"]:
    return "OK"


# Auth Router
# User Router
# Job Router
@app.post("/resumes/process")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
