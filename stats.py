def get_word_count(text):
    """
    Counts the number of words in the given text.

    Args:
        text (str): The text to count words in.
    
    Returns:
        int: The number of words in the text.
    """
    words = text.split()
    return len(words)

def get_character_count(text):
    """
    Takes the text from the book as a string, and returns the number of times each character, (including symbols and spaces), appears in the string.

    Args:
        text (str): The text to count characters in.
    
    Returns:
        dict: A dictionary with characters as keys and their counts as values.
    """

    #make sure the text is all lowercase
    text = text.lower()

    #create an empty dictionary to hold character counts
    char_count = {}

    #main loop to count characters
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_character_count(char_count):
    """
    Sorts the character count dictionary by frequency in descending order.

    Args:
        char_count (dict): A dictionary with characters as keys and their counts as values.

    Returns:
        A sorted list of dictionaries with each dictionary having two key-value pairs: one for the character itself and one for that character's count (e.g. {"char": "b", "num": 4868}).
    """

    sorted_chars = sorted(
    (
        {"char": char, "num": num}
        for char, num in char_count.items()
    ),
    key=lambda d: d["num"],
    reverse=True
    )

    return sorted_chars