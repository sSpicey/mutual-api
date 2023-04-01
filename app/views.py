from fastapi import APIRouter
from controllers import reverse_integer, average_words_length, matched_and_mismatched_words

reverse_integer_router = APIRouter()
average_words_length_router = APIRouter()
matched_and_mismatched_words_router = APIRouter()

@reverse_integer_router.get("/reverse_integer/{number}")
def get_reverse_integer(number: int):
    return {"reverse_integer": reverse_integer(number)}

@average_words_length_router.post("/medium_length")
def post_average_words_length(phrase: str):
    return {"medium_length": average_words_length(phrase)}

@matched_and_mismatched_words_router.post("/common_words")
def post_matched_and_mismatched_words(phrase1: str, phrase2: str):
    uncommon_words, common_words = matched_and_mismatched_words(phrase1, phrase2)
    return {"uncommon_words": uncommon_words, "common_words": common_words}
