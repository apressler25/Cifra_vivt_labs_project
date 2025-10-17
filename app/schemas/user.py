from datetime import datetime
from pydantic import BaseModel, ConfigDict



class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id:int | None = None
    created_at:datetime | None = None
    updated_at:datetime | None = None
    username:str
    first_name: str
    lastname: str
    age:int 
    


class UserList(BaseModel):
    count:int 
    users:list[UserSchema]



class UpdateUserSchema(UserSchema): 
    username:str | None = None
    first_name: str | None = None
    lastname: str | None = None
    age:int | None = None