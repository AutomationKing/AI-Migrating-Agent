from git import Repo
from pathlib import Path

def clone_repo(repo_url, target_dir="source_repo"):
    target = Path(target_dir)
    if target.exists():
        print(f"🟡 Repo already cloned: {target_dir}")
    else:
        print(f"📥 Cloning repo from {repo_url}")
        Repo.clone_from(repo_url, target)
    return target.resolve()
