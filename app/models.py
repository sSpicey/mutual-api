from pydantic import BaseModel


class AverageWordsLengthRequest(BaseModel):
    phrase: str

class MatchedAndMismatchedWordsRequest(BaseModel):
    phrase1: str
    phrase2: str