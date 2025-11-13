import os
import subprocess
import tempfile
from urllib.parse import urlparse

def clone_repo(repo_url: str) -> str: 
    """
    Clone a GitHub repository to a temporary folder and return the local path.
    If the repo already exists in temp, it will remove it first.
    """
    parsed_url = urlparse(repo_url)
    repo_name = os.path.basename(parsed_url.path).replace(".git", "")
    
    # Clone to a temp folder
    temp_dir = os.path.join(tempfile.gettempdir(), repo_name)
    
    if os.path.exists(temp_dir):
        print(f"🗑️ Removing existing folder: {temp_dir}")
        subprocess.run(["rm", "-rf", temp_dir] if os.name != "nt" else ["rmdir", "/S", "/Q", temp_dir], check=True)
    
    print(f"📦 Cloning repository {repo_url} into {temp_dir}")
    subprocess.run(["git", "clone", repo_url, temp_dir], check=True)
    
    return temp_dir
