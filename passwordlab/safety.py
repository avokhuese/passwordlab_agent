from urllib.parse import urlparse
from .config import LAB_BASE_URL, HARD_MAX_ATTEMPTS

class SafetyError(ValueError):
    """Raised when a simulation violates the lab safety policy."""

def validate_target(url: str) -> None:
    parsed = urlparse(url)
    if (
        parsed.scheme != "http"
        or parsed.hostname not in {"127.0.0.1", "localhost"}
        or parsed.port != 8000
        or parsed.path not in {"", "/"}
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
    ):
        raise SafetyError("Rejected: target must be the localhost lab on port 8000.")
    if parsed.port != urlparse(LAB_BASE_URL).port:
        raise SafetyError("Rejected: unexpected laboratory port.")

def validate_attempt_limit(limit: int) -> int:
    if not isinstance(limit, int) or limit < 1:
        raise SafetyError("Attempt limit must be a positive integer.")
    if limit > HARD_MAX_ATTEMPTS:
        raise SafetyError(f"Attempt limit exceeds hard ceiling {HARD_MAX_ATTEMPTS}.")
    return limit

def require_confirmation(confirmed: bool) -> None:
    if not confirmed:
        raise SafetyError("Execution not authorised. Re-run with --confirm.")
