from pydantic import BaseModel

# Define your data models here
class Building(BaseModel):
    name: str | None = None
