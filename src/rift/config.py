# src/rift/config.py

from functools import lru_cache

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    openai_api_key: SecretStr
    rift_model: str = "gpt-6-luna"
    rift_sandbox_image: str = "rift-sandbox:dev"
    rift_max_tool_calls: int = Field(default=60, gt=0)
    rift_max_step_attempts: int = Field(default=3, gt=0)
    rift_run_timeout_s: int = Field(default=900, gt=0)


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore[call-arg]  # required fields come from env
