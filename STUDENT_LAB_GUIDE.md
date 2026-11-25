# Student Guide

## Scenario
You are a junior security engineering team assessing password resilience for a fictional organisation. The supplied local application contains five synthetic accounts. Build and evaluate a LangGraph agent that coordinates two bounded simulations and reports defensive lessons.

## Task 1 — Environment and threat model
- Install dependencies and start the local FastAPI service.
- Inspect `/health` and `/lab/accounts`.
- Draw the trust-boundary diagram.
- Explain why localhost scope and synthetic credentials matter.

## Task 2 — LangGraph workflow
- Trace state through `validate_scope`, `load_accounts`, `plan_attack`, `execute_simulation`, and `analyse_results`.
- Explain conditional routing and rejection behaviour.

## Task 3 — Dictionary simulation
- Run dictionary mode with a maximum of 100 attempts.
- Record attempts, successes, elapsed time and observed success rate.
- Explain how wordlist ordering affects results.


## Task 4 — Bounded brute-force simulation
- Run brute-force mode with a maximum of 100 attempts.
- Explain the configured alphabet and length boundary.
- Explain exponential growth.

## Task 5 — Compare and interpret
Compare attempts, successful authentications, observed success rate, and elapsed time. Do not claim that lab timings predict production attack times.

## Task 6 — Defensive recommendations
Justify long unique passwords, password managers, MFA, rate limiting, progressive delays, monitoring, secure password hashing and breached-password screening.

## Task 7 — Safety tests
- Run `pytest -q`.
- Demonstrate rejection of external hostnames and non-lab ports.
- Demonstrate rejection of attempt limits above the hard ceiling.
- Explain why arbitrary target URLs are not accepted.


## Reflection
1. Why does dictionary success suggest password predictability?
2. How does password length affect search-space size?
3. Why is an attempt limit a safety control?
4. What can a rule-based LangGraph workflow do without an LLM?
5. What risks arise if an LLM can choose arbitrary targets or tools?
6. Why do laboratory results not predict production attack times?
