from pydantic import BaseModel

class ExampleBody(BaseModel):
        name: str
        desc: str