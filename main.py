# Importing necessary functions from stats module
import sys
from stats import get_word_count
from stats import get_character_count
from stats import get_character_count_sorted

def get_book_text(file_path):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        file_path (str): The path to the book file.
        
    Returns:
        str: The content of the book.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

if __name__ == "__main__":
    # Check if there are enough command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Get the book path from command-line arguments
    book_path = sys.argv[1]
    
    # Now use the book path from the command line
    book_content = get_book_text(book_path)
    
    num_words = get_word_count(book_content)
    print(f"Found {num_words} total words")
    
    character_count = get_character_count(book_content)
    #print(character_count)
    
    sorted_character_count = get_character_count_sorted(book_content)
    for item in sorted_character_count:
        char = item["char"]
        count = item["num"]
        if char.isalpha():
            print(f"{char}: {count}")