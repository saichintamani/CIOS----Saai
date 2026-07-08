from dataclasses import dataclass


@dataclass
class Report:
    date: str
    github_status: str
    top_project: str
    recommendation: str
    score: int