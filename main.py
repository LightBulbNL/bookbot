def get_book_text(book):
    """
    Extracts and returns the text content of a book.

    Args:
        book (object): The filepath to the book file.
    
    Returns:
        str: The text content of the book.
    """
    with open (book) as f:
        text = f.read()
    return text

from stats import get_word_count
from stats import get_character_count


if __name__ == "__main__":
    book = "./books/frankenstein.txt"
    text = get_book_text(book)
    print(f"Found {get_word_count(text)} total words")
    print(get_character_count(text))