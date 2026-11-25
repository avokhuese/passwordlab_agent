from itertools import product
from pathlib import Path
from .config import DATA_DIR, BRUTE_ALPHABET, BRUTE_MAX_LENGTH

def dictionary_candidates(path: Path | None = None):
    """Yield candidates from the supplied synthetic wordlist."""
    source = path or (DATA_DIR / "synthetic_dictionary.txt")
    with source.open("r", encoding="utf-8") as handle:
        for line in handle:
            candidate = line.strip()
            if candidate and len(candidate) <= 32:
                yield candidate

def bounded_bruteforce_candidates():
    """Generate a deliberately tiny, bounded candidate space."""
    for length in range(1, BRUTE_MAX_LENGTH + 1):
        for chars in product(BRUTE_ALPHABET, repeat=length):
            yield "".join(chars)
