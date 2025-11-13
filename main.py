import sys
import yaml
import os
from utils.github_handler import clone_repo
from agent.worker import process_all_files
import sys
import os

# Add project root to PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.github_handler import clone_repo
from agent.worker import process_all_files


def main():
    print("🚀 Starting AI Migration Agent...")

    # Load config
    config_path = os.path.join("config", "settings.yaml")
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    # Get GitHub repo URL
    if len(sys.argv) >= 2:
        repo_url = sys.argv[1]
    else:
        repo_url = config.get("github_repo")

    if not repo_url:
        print("❌ No GitHub repo provided! Please pass it as argument or add to config/settings.yaml")
        sys.exit(1)

    print(f"📦 Cloning repository: {repo_url}")

    # Clone repo to local folder
    project_path = clone_repo(repo_url)

    # Start migration
    print(f"⚙️ Starting migration for project: {project_path}")
    process_all_files(project_path, config)

    print("✅ Migration complete!")
    print(f"🗂️ Migrated files stored in: {config.get('target_project', 'playwright-migrated')}")

if __name__ == "__main__":
    main()
