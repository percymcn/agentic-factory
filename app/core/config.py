from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "AgenticFactory"
    APP_ENV: str = "prod"
    APP_PORT: int = 9123
    UVICORN_WORKERS: int = 2
    API_KEY: str = "supersecret123"

    # Celery/Redis
    REDIS_URL: str = "redis://redis:6379/0"
    CELERY_BROKER_URL: str = "redis://redis:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://redis:6379/1"
    CELERY_TIMEZONE: str = "UTC"

    # Tell the app how to reach the local agent
    OPS_AGENT_BASE: str = "http://host.docker.internal:49123"
    CF_ACCESS_CLIENT_ID: str | None = None
    CF_ACCESS_CLIENT_SECRET: str | None = None
    AUTOOPS_BEARER: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
