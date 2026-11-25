import argparse
from .config import LAB_BASE_URL, DEFAULT_MAX_ATTEMPTS, HARD_MAX_ATTEMPTS
from .graph import build_graph

def main():
    parser = argparse.ArgumentParser(description="PasswordLab localhost-only simulation agent")
    parser.add_argument("--mode", choices=["dictionary", "brute_force"], required=True)
    parser.add_argument("--max-attempts", type=int, default=DEFAULT_MAX_ATTEMPTS)
    parser.add_argument("--confirm", action="store_true",
                        help="Confirm the target is the synthetic localhost lab.")
    args = parser.parse_args()
    if args.max_attempts > HARD_MAX_ATTEMPTS or args.max_attempts < 1:
        parser.error(f"--max-attempts must be between 1 and {HARD_MAX_ATTEMPTS}")
    result = build_graph().invoke({
        "mode": args.mode, "target": LAB_BASE_URL,
        "max_attempts": args.max_attempts, "confirmed": args.confirm,
    })
    print("\\n=== PasswordLab Agent Report ===")
    print(result.get("report", result.get("error", "No report generated.")))
    if result.get("error"):
        print("Agent message:", result["error"])

if __name__ == "__main__":
    main()
