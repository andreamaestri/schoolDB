## Core Classes and Functions

### `User` class
- `__init__(self, username: str, score: int, total_score: int)` - Initializes a new instance of the `User` class with the given `username`, `score`, and `total_score`.
- `get_percentage(self) -> float` - Calculates and returns the percentage of the user's score out of their total score.
- `__str__(self) -> str` - Returns a string representation of the `User` instance.

### `Database` class
- `__init__(self, host: str, username: str, password: str, database: str)` - Initializes a new instance of the `Database` class with the given connection details.
- `add_user(self, user: User) -> None` - Adds a new user to the database.
- `get_user(self, username: str) -> Union[User, None]` - Retrieves a user from the database with the given `username`. Returns `None` if the user is not found.

### `main` function
- `get_user_input() -> Tuple[str, int, int]` - Prompts the user to enter their username, score, and total score, and returns the values as a tuple.
- `print_user(user: User) -> None` - Prints the given `User` instance to the console.
- `main() -> None` - The main function that runs the application.

## File: `user.py`
