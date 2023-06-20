from dataclasses import dataclass


@dataclass
class User:
    username: str
    score: int
    total_score: int

    def get_percentage(self) -> float:
        return (self.score / self.total_score) * 100

    def __str__(self) -> str:
        return f"{self.username}: {self.score}/{self.total_score} ({self.get_percentage()}%)"
