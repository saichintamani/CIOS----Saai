from dataclasses import dataclass


@dataclass
class Activity:
    platform: str
    date: str
    streak: int
    activity_count: int
    status: str