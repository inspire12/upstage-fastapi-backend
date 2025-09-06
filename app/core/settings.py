from pydantic import computed_field
from pydantic_settings import BaseSettings
from pydantic_core import MultiHostUrl

class Settings(BaseSettings):
    PROJECT_NAME: str = 'upstage-backend'
    API_V1_STR: str = '/api/v1'



settings = Settings()