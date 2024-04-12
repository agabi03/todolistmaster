from pydantic import BaseModel


class STaskADD(BaseModel):
    name: str
    description: str | None = None

    class Config:
        orm_mode = True
        from_attributes = True


class STask(STaskADD):
    id: int


class STaskID(BaseModel):
    ok: bool = True
    id: int
