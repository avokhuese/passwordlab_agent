# PasswordLab AI — Lab


## Safety model
- Fixed target: `http://127.0.0.1:8000`; only localhost is accepted.
- Server binds to `127.0.0.1`, never `0.0.0.0`.
- Synthetic accounts only; no real credentials.
- Hard ceiling: 200 attempts per run; runtime capped at 20 seconds.
- Explicit `--confirm` required.
- Tiny brute-force alphabet and maximum length of 3.
- No arbitrary targets, external network access, stealth, evasion, lockout bypass, or credential harvesting.

## Setup
Python 3.11+ recommended.

```bash
python -m venv .venv
source .venv/bin/activate
# Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

Start the server in terminal 1:
```bash
uvicorn passwordlab.server:app --host 127.0.0.1 --port 8000
```

Run in terminal 2:
```bash
python -m passwordlab.cli --mode dictionary --confirm
python -m passwordlab.cli --mode brute_force --confirm
```

Optional:
```bash
python -m passwordlab.cli --mode dictionary --max-attempts 50 --confirm
```

Dashboard:
```bash
streamlit run passwordlab/dashboard.py
```

Tests:
```bash
pytest -q
```

## Project structure
- `passwordlab/server.py`: synthetic FastAPI authentication service.
- `passwordlab/graph.py`: LangGraph workflow.
- `passwordlab/generators.py`: candidate generators.
- `passwordlab/safety.py`: fixed target and attempt-limit checks.
- `passwordlab/storage.py`: SQLite experiment log.
- `passwordlab/dashboard.py`: Streamlit results view.
- `STUDENT_LAB_GUIDE.md`: student instructions.

The agent is a deterministic LangGraph workflow and does not require an LLM API. An optional local LLM may explain results, but must never choose arbitrary targets, run arbitrary commands, or relax safety controls.
