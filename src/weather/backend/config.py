from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

current_path = Path(__file__).resolve()
env_path = next((p / ".env" for p in current_path.parents if (p / ".env").exists()), None)


class Settings(BaseSettings):
    API_KEY: str

    model_config = SettingsConfigDict(
        env_file=env_path,
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings() # type: ignore
