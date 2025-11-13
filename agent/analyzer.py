from pathlib import Path

def analyze_project(repo_path):
    p = Path(repo_path)
    java_files = list(p.rglob("*.java"))
    feature_files = list(p.rglob("*.feature"))
    print(f"📊 Found {len(java_files)} Java files and {len(feature_files)} feature files.")
    return {"java": java_files, "features": feature_files}
