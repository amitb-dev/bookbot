import stats as s
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    # 1. Data Processing:
    book_text = get_book_text(sys.argv[1])

    # 2. Analysis:
    word_count = s.word_count(book_text)
    chars = s.chars_count(book_text)
    sorted_chars = s.convert_and_filter(chars)

    # 3. Presentation:
    s.print_report(sys.argv[1], word_count, sorted_chars)

main()
