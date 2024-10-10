from pydantic import BaseModel

class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int

class CreateUser(UpdateUser):
    username: str

class CreateTask(BaseModel):
    title: str
    content: str
    priority: str

class UpdateTask(CreateTask):
    pass