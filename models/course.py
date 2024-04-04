from uuid import UUID

from pydantic import BaseModel


# Course:
    # name
    # location
    # holes

class Course(BaseModel):
    id: UUID
    name = str
    location = str
    holes = int



