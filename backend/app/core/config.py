from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "InsightFlow API"
    api_prefix: str = "/api/v1"
    max_upload_mb: int = 25
    temp_dir: Path = Path("/tmp/insightflow")
    frontend_origin: str = "http://localhost:3000"

    model_config = SettingsConfigDict(env_file=".env", env_prefix="INSIGHTFLOW_")


settings = Settings()
settings.temp_dir.mkdir(parents=True, exist_ok=True)
