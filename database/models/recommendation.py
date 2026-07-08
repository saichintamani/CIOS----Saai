from dataclasses import dataclass


@dataclass
class Recommendation:
    title: str
    description: str
    impact: str
    estimated_time: str
    priority: str