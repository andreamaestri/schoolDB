from user import User
from database import Database
from typing import Tuple


def get_user_input() -> Tuple[str, int, int]:
    username = input("Enter your username: ")
    score = int(input("Enter your score: "))
    total_score = int(input("Enter the total score: "))
    return username, score, total_score


def print_user(user: User) -> None:
    print(user)


def main() -> None:
    db = Database("localhost", "root", "password", "test_scores")
    username, score, total_score = get_user_input()
    user = User(username, score, total_score)
    db.add_user(user)
    retrieved_user = db.get_user(username)
    if retrieved_user:
        print_user(retrieved_user)
    else:
        print("User not found.")
