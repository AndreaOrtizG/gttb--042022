from dotenv import load_dotenv
from pydantic import BaseSettings, Field

load_dotenv(".env")


class Settings(BaseSettings):

    DATABASE_URL: str = Field(...)
    SECRET_KEY: str = Field(...)
    ALGORITHM: str = Field(...)

    class Config:
        env_file = ".env"


def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()
