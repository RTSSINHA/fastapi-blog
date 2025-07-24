from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum
from datetime import datetime


class Language(str, Enum):
    JAVA = "Java"
    PY = "Python"
    GO = "Go"

class Comment(BaseModel):
    text: Optional[str] = None


class Blog(BaseModel):
    title: str = Field(min_length=10)
    is_active: bool
    description: Optional[str] = None
    language: Language = Language.JAVA
    created_at: datetime = Field(default_factory=datetime.now)
    comments: List[Comment]



first_blog = Blog(title="First Blog", 
                  is_active=True, 
                  description="descriptions of the blog",
                  language=Language.PY,
                  comments = [{"text": "First Comment"}])


print(first_blog)
# print("Language type")
# print(type(first_blog.language))
# print(type(first_blog.title))

# import time
# time.sleep(5)

# second_blog = Blog(title="Second Blog", is_active=True)
# print(second_blog)

# print(first_blog.model_dump())
# print(first_blog.model_dump_json())
