from pathlib import Path
import subprocess

def setup_target_project(target_dir):
    target = Path(target_dir)
    if not target.exists():
        print("🛠️ Initializing new Playwright TypeScript project (quiet)...")
        subprocess.run(["npx", "playwright", "install"], check=False)
        subprocess.run(["npx", "playwright", "new-project", target_dir, "--lang=ts", "--quiet"], check=False)
    else:
        print(f"🟡 Project already exists: {target_dir}")
    return target.resolve()

def save_ts_file(target_dir, relative_path, ts_code):
    dest = Path(target_dir) / "migrated" / relative_path.with_suffix(".ts")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(ts_code, encoding="utf-8")
    print(f"✅ Saved migrated file: {dest}")
    return dest
