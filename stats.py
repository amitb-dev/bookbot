def word_count(book_text):
    return len(book_text.split())

def chars_count(book_text):
    total_count = {}
    
    for char in book_text:
        char_lower = char.lower()

        if char_lower in total_count:
            total_count[char_lower] += 1
        else:
            total_count[char_lower] = 1
    
    return total_count