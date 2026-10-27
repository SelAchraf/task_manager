from pathlib import Path
from task_manager.models import Task

class JsonTaskStorage:
    def __init__(self, path: Path) -> None: ...
    def load(self) -> list[Task]: ...     # missing file -> []; corrupt file -> StorageError
    def save(self, tasks: list[Task]) -> None: ...
