from dataclasses import dataclass


@dataclass
class Project:
    name: str
    score: int
    category: str
    priority: str
    recommendation: str