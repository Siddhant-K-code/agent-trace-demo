def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in text."""
    return len(text.split())


def char_count(text: str, include_spaces: bool = True) -> int:
    """Return the number of characters in text, optionally excluding whitespace."""
    if include_spaces:
        return len(text)
    return sum(not character.isspace() for character in text)
