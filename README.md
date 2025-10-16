# HNGi13 — Stage 0 Task (Backend) — Dynamic Profile `/me` (FastAPI)

A tiny FastAPI service that exposes `GET /me`, returning your profile and a **random cat fact** fetched from `https://catfact.ninja/fact`.  
It always includes a fresh **UTC ISO 8601** timestamp and sets `Cache-Control: no-store`.

## Endpoint (spec)

### GET /me

Content-Type: application/json

#### Response shape (exact keys):

```json
{
  "status": "success",
  "user": {
    "email": "<your email>",
    "name": "<your full name>",
    "stack": "<your backend stack>"
  },
  "timestamp": "<current UTC time in ISO 8601 format>",
  "fact": "<random cat fact from Cat Facts API>"
}
```

If the Cat Facts API fails or times out, the endpoint responds 200 with a fallback string in fact:

"[fallback] couldn’t fetch cat fact right now—try again soon"

## Stack

- Python 3.10+
- FastAPI + Uvicorn
- httpx (async) with timeouts
- Optional CORS (defaults to \*)

## Local Setup

1. #### Clone & enter

   ```bash
   git clone <your-repo-url> hng-stage0-task
   cd hng-stage0-task
   ```

2. #### Create venv & install

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. #### Environment

   Copy .env.example → .env and fill your values.

   Vars:

   ```
   USER_EMAIL — your email
   USER_NAME — your full name
   USER_STACK — e.g. Python/FastAPI
   CATFACT_URL — https://catfact.ninja/fact
   HTTP_TIMEOUT_SECONDS — default 3
   ALLOWED_ORIGINS — default *
   PORT — default 8000
   ```

4. #### Run

   ```bash
   ./run.sh

   # or

   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

5. #### Verify
   ```bash
   curl -i http://127.0.0.1:8000/me
   curl -i http://127.0.0.1:8000/health
   # docs at: http://127.0.0.1:8000/docs
   ```

## License

MIT
