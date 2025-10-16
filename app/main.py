from datetime import datetime, timezone
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
import httpx

from .config import settings

app = FastAPI(title="HNG Stage 0 Task")

if settings.ALLOWED_ORIGINS == "*" or not settings.ALLOWED_ORIGINS:
    allow_origins = ["*"]
else:
    allow_origins = [o.strip() for o in settings.ALLOWED_ORIGINS.split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=False,
    allow_methods=["GET", "OPTIONS"],
    allow_headers=["*"],
)

def utc_now_iso_z() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

@app.get("/health")
async def health():
    return {"ok": True, "timestamp": utc_now_iso_z()}

@app.get("/me")
async def me(response: Response):
    # prevent caching
    response.headers["Cache-Control"] = "no-store"

    fact_text = None
    try:
        async with httpx.AsyncClient(timeout=settings.HTTP_TIMEOUT_SECONDS) as client:
            r = await client.get(settings.CATFACT_URL)
            r.raise_for_status()
            data = r.json()
            fact_text = data.get("fact")
    except Exception:
        fact_text = "[fallback] couldn’t fetch cat fact right now—try again soon"

    payload = {
        "status": "success",
        "user": {
            "email": settings.USER_EMAIL,
            "name": settings.USER_NAME,
            "stack": settings.USER_STACK,
        },
        "timestamp": utc_now_iso_z(),
        "fact": fact_text or "[fallback] no fact available",
    }
    return payload
