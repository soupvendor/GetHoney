from pydantic import BaseSettings


class Settings(BaseSettings):
    db_path: str = "../data/gethoney.db"

    class Config:
        env_file = ".env"


settings = Settings()
