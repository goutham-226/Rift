# src/rift/config.py

from functools import lru_cache

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="RIFT_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Standard OpenAI variable name, so it skips the RIFT_ prefix.
    openai_api_key: SecretStr = Field(validation_alias="OPENAI_API_KEY")

    model: str = "gpt-6-luna"
    sandbox_image: str = "rift-sandbox:dev"
    max_tool_calls: int = Field(default=60, gt=0)
    max_step_attempts: int = Field(default=3, gt=0)
    run_timeout_s: int = Field(default=900, gt=0)


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore[call-arg]  # required fields come from env
