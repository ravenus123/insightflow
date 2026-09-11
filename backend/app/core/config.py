from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "InsightFlow API"
    api_prefix: str = "/api/v1"
    max_upload_mb: int = 25
    data_dir: Path = Path("./.data/uploads")
    frontend_origin: str = "http://localhost:3000"
    database_url: str = "sqlite:///./.data/insightflow.db"
    jwt_secret: str = "change-me-in-production"
    jwt_exp_minutes: int = 60 * 24
    model_config = SettingsConfigDict(env_file=".env", env_prefix="INSIGHTFLOW_")

settings = Settings()
settings.data_dir.mkdir(parents=True, exist_ok=True)
settings.data_dir.parent.mkdir(parents=True, exist_ok=True)
