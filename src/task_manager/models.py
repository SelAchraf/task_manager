from dataclasses import dataclass

@dataclass
class Task:
    id: int
    title: str
    status: str = "todo"        # "todo" or "done"
    created_at: str = ""        # ISO timestamp
