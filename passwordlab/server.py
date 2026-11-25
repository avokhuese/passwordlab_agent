import hashlib
import hmac
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="PasswordLab Synthetic Authentication API")

def _digest(password: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 120_000)

# Synthetic classroom accounts only; password values are not exposed by the API.
_SALT = b"passwordlab-classroom-salt"
_USERS = {
    "student01": _digest("abc1", _SALT),
    "student02": _digest("sunshine", _SALT),
    "student03": _digest("c1a", _SALT),
    "student04": _digest("correct-horse", _SALT),
    "student05": _digest("123456", _SALT),
}

class LoginRequest(BaseModel):
    username: str = Field(min_length=1, max_length=32, pattern=r"^[a-zA-Z0-9_]+$")
    password: str = Field(min_length=1, max_length=64)

@app.get("/health")
def health():
    return {"status": "ok", "environment": "synthetic-local-lab"}

@app.get("/lab/accounts")
def accounts():
    return {"accounts": sorted(_USERS.keys())}

@app.post("/login")
def login(payload: LoginRequest):
    stored = _USERS.get(payload.username)
    candidate = _digest(payload.password, _SALT)
    ok = stored is not None and hmac.compare_digest(stored, candidate)
    return {"authenticated": bool(ok)}
