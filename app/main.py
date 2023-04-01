from fastapi import FastAPI
from views import reverse_integer_router, average_words_length_router, matched_and_mismatched_words_router
import uvicorn

app = FastAPI()

app.include_router(reverse_integer_router)
app.include_router(average_words_length_router)
app.include_router(matched_and_mismatched_words_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
