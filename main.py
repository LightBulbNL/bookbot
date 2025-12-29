import sys
from stats import get_word_count
from stats import get_character_count
from stats import sort_character_count

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

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    character_count = get_character_count(text)

    sorted_chars = sort_character_count(character_count)

    char_lines = "\n".join(
        f"{d['char']}: {d['num']}"
        for d in sorted_chars
    )

    print(f"""
    ============ BOOKBOT ============
    Analyzing book found at {book_path}...
    ----------- Word Count ----------
    Found {get_word_count(text)} total words
    --------- Character Count -------
    {char_lines}
    ============= END ===============
    """)

if __name__ == "__main__":
    main()