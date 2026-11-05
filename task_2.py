"""Task 2: palindrome checking using a double-ended queue."""

from collections import deque


def is_palindrome(text: str) -> bool:
    """Check whether text is a palindrome, ignoring case and whitespace."""
    normalized = "".join(char for char in text.casefold() if not char.isspace())
    characters = deque(normalized)

    while len(characters) > 1:
        if characters.popleft() != characters.pop():
            return False

    return True


def main() -> None:
    text = input("Введіть рядок для перевірки: ")
    if is_palindrome(text):
        print("Рядок є паліндромом.")
    else:
        print("Рядок не є паліндромом.")


if __name__ == "__main__":
    main()
