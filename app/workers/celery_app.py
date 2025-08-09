from celery import Celery
from app.core.config import settings

celery = Celery(__name__)
celery.conf.update(
    broker_url=settings.CELERY_BROKER_URL,
    result_backend=settings.CELERY_RESULT_BACKEND,
    timezone=settings.CELERY_TIMEZONE,
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    beat_schedule={
        # Every 2 minutes, ask the local agent to run a tiny script.
        "auto-exec-projects": {
            "task": "tasks.autoexec.run_demo",
            "schedule": 120.0,
        }
    },
)

import app.workers.tasks.autoexec  # noqa: F401
