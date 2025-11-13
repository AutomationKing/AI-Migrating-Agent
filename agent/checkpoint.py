import json
from pathlib import Path

class Checkpoint:
    def __init__(self, path):
        self.path = Path(path)
        if not self.path.exists():
            self._data = {"completed": [], "failed": [], "in_progress": []}
            self._save()
        else:
            self._data = json.loads(self.path.read_text(encoding="utf-8"))

    def _save(self):
        self.path.write_text(json.dumps(self._data, indent=2), encoding="utf-8")

    def mark_in_progress(self, filename):
        if filename not in self._data["in_progress"]:
            self._data["in_progress"].append(filename)
            self._save()

    def mark_completed(self, filename):
        if filename in self._data["in_progress"]:
            self._data["in_progress"].remove(filename)
        if filename not in self._data["completed"]:
            self._data["completed"].append(filename)
        self._save()

    def mark_failed(self, filename, reason=None):
        if filename in self._data["in_progress"]:
            self._data["in_progress"].remove(filename)
        if filename not in self._data["failed"]:
            self._data["failed"].append({"file": filename, "reason": reason})
        self._save()

    def is_done(self, filename):
        return filename in self._data["completed"]
