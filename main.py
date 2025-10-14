from stats import word_count, chars_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(path_to_book)
    print(f"Found {word_count(book_text)} total words")
    print(chars_count(book_text))
    
main()