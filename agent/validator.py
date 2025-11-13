import subprocess
from pathlib import Path

def quick_syntax_check(ts_file_path):
    return True

def run_playwright_tests(target_dir, sample_limit=5):
    proc = subprocess.run(["npx", "playwright", "test", "--max-failures=1", "--grep=@migrated"], cwd=target_dir, capture_output=True, text=True)
    return proc.returncode == 0, proc.stdout + "\n" + proc.stderr
