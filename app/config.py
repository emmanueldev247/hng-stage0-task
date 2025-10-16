from os import getenv

class Settings:
    USER_EMAIL: str = getenv("USER_EMAIL", "john.doe@example.com")
    USER_NAME: str = getenv("USER_NAME", "John Doe")
    USER_STACK: str = getenv("USER_STACK", "Python/FastAPI")

    CATFACT_URL: str = getenv("CATFACT_URL", "https://catfact.ninja/fact")
    HTTP_TIMEOUT_SECONDS: float = float(getenv("HTTP_TIMEOUT_SECONDS", "5"))

    ALLOWED_ORIGINS: str = getenv("ALLOWED_ORIGINS", "*")

    PORT: int = int(getenv("PORT", "8000"))

settings = Settings()
