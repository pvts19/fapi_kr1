import re
from pydantic import BaseModel, Field, field_validator


# 1.3*
class CalcRequest(BaseModel):
    num1: float
    num2: float


# 1.4
class User(BaseModel):
    name: str
    id: int


# 1.5*
class UserAge(BaseModel):
    name: str
    age: int


# 2.1 + 2.2
class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)

    @field_validator("message")
    @classmethod
    def ban_bad_words(cls, v: str) -> str:
        
        pattern = r"\b(кринж|рофл|вайб)[а-яё]*\b"
        if re.search(pattern, v, flags=re.IGNORECASE):
            raise ValueError("Использование недопустимых слов")
        return v