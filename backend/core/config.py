import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "FastBLOG 🔥"
    PROJECT_VERSION: str = "1.0.0"

    DATABASE_URL: str = os.getenv("POSTGRES_URI")


settings = Settings()
