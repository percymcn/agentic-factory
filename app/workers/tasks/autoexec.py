import json
import requests
from app.core.config import settings
from loguru import logger

def _headers():
    h = {"Content-Type": "application/json"}
    if settings.CF_ACCESS_CLIENT_ID and settings.CF_ACCESS_CLIENT_SECRET:
        h["CF-Access-Client-Id"] = settings.CF_ACCESS_CLIENT_ID
        h["CF-Access-Client-Secret"] = settings.CF_ACCESS_CLIENT_SECRET
    if settings.AUTOOPS_BEARER:
        h["Authorization"] = f"Bearer {settings.AUTOOPS_BEARER}"
    return h

from app.workers.celery_app import celery  # noqa

@celery.task(name="tasks.autoexec.run_demo")
def run_demo():
    payload = {
        "name": "auto-demo",
        "script": "echo '[autoexec] Hello from Celery' && python3 -V"
    }
    try:
        r = requests.post(f"{settings.OPS_AGENT_BASE}/run",
                          headers=_headers(), data=json.dumps(payload), timeout=30)
        r.raise_for_status()
        logger.info(f"Agent job launched: {r.text}")
        return {"ok": True, "agent_response": r.json()}
    except Exception as e:
        logger.error(f"Agent call failed: {e}")
        return {"ok": False, "error": str(e)}
