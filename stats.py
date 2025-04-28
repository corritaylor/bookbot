def get_word_count(text):
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
        
    Returns:
        int: The number of words in the text.
    """
    return len(text.split())

def get_character_count(text):
    """
    Counts the number of characters in a given text.
    
    Args:
        text (str): The text to count characters in.
        
    Returns:
        int: The number of characters in the text.
    """
    
    char_dict = {} # Dictionary to store character counts
    text = text.lower() # Convert text to lowercase for case-insensitive counting
    # Iterate through each character in the text
    # and update the character count in the dictionary
    for char in text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict # Return the character count dictionary

def get_character_count_sorted(text):
    """
    Counts the number of characters in a given text and sorts them.
    
    Args:
        text (str): The text to count characters in.
        
    Returns:
        list: A sorted list of tuples containing characters and their counts.
    """
    my_list = [] # Dictionary to store character counts
    char_dict = get_character_count(text) # Get character counts
    for char, count in char_dict.items():
        my_list.append({"char": char, "num": count})
    my_list.sort(key=lambda x: x["num"], reverse=True) # Sort the list by count in descending order

    return my_list # Return the sorted character count list
    