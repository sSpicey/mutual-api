from fastapi import FastAPI
from app.views import inverted_number_router, medium_length_router, common_words_router
from app import controllers
import uvicorn

app = FastAPI()

app.include_router(inverted_number_router)
app.include_router(medium_length_router)

app.include_router(common_words_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
