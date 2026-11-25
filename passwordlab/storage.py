import sqlite3
from datetime import datetime, timezone
from .config import DB_PATH

def connect():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS experiments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL,
            mode TEXT NOT NULL,
            attempts INTEGER NOT NULL,
            successes INTEGER NOT NULL,
            elapsed_seconds REAL NOT NULL,
            status TEXT NOT NULL
        )
    """)
    conn.commit()
    return conn

def save_experiment(mode: str, attempts: int, successes: int, elapsed: float, status: str):
    with connect() as conn:
        conn.execute(
            "INSERT INTO experiments(created_at, mode, attempts, successes, elapsed_seconds, status) VALUES (?, ?, ?, ?, ?, ?)",
            (datetime.now(timezone.utc).isoformat(), mode, attempts, successes, elapsed, status),
        )
        conn.commit()
