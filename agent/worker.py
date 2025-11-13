from agent.migrator import migrate_java_to_ts
import os

def process_all_files(project_path: str, config: dict):
    """
    Process all files in the cloned repo.
    """
    print(f"⚙️ Processing files in {project_path} with {config.get('max_workers', 5)} workers...")

    for root, dirs, files in os.walk(project_path):
        for file in files:
            if file.endswith(".java") or file.endswith(".feature"):
                file_path = os.path.join(root, file)
                print(f"📄 Found file to migrate: {file_path}")
                migrate_java_to_ts(file_path, config)

    print("✅ All files processed.")
