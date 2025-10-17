from pydantic_settings import BaseSettings 
from pydantic import Field
from functools import lru_cache



class Settings(BaseSettings):
    POSTGRES_DB:str = Field(default="project")
    POSTGRES_USER:str = Field(default="projectcifra")
    POSTGRES_PASSWORD:str = Field(default="passwordbd")
    POSTGRES_HOST:str = Field(default="db")
    POSTGRES_PORT:str = Field(default="5432")
    
    
    
    
    
    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )
    
    
@lru_cache
def get_settings():
    return Settings()
settings = get_settings()
    


