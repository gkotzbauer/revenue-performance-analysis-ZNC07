#!/usr/bin/env python3
import os, subprocess, sys

SCRIPTS_DIR = os.path.dirname(__file__)
PIPELINE_SCRIPTS = [
    "interactive_benchmark_code_v2.py",
    "final_rev_perf_weekly_model_generator v12w.py",
    "merge_invoice_summary_alignment.py"
]

def main():
    for script in PIPELINE_SCRIPTS:
        path = os.path.join(SCRIPTS_DIR, script)
        if not os.path.isfile(path):
            print(f"ERROR: Missing {script}", file=sys.stderr)
            sys.exit(1)
        print(f"▶ Running {script}...")
        res = subprocess.run([sys.executable, path], check=False)
        if res.returncode != 0:
            print(f"✖ {script} failed ({res.returncode})", file=sys.stderr)
            sys.exit(res.returncode)
    print("✅ Pipeline complete.")

if __name__ == "__main__":
    main()
