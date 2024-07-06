from typing import Optional

from pydantic import BaseModel


class STasksAdd(BaseModel):
    # Class for init tasks
    name: str
    description: Optional[str] = None


class Tasks(STasksAdd):
    # Class for DataBase ID
    id: int
