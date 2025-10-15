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

def sort_on(items):
    return items["num"]

def convert_and_filter(chars_dict):
    report_list = []

    for char, num in chars_dict.items():
        if char.isalpha():
            cur_dict = {"char": char, "num": num}
            report_list.append(cur_dict)

    return sorted(report_list, reverse=True, key=sort_on)

def my_print(sorted_chars):
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

def print_report(path_to_book, word_count, sorted_chars):
    """Prints the final report to the console."""

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")

    # --- Word Count Section ---
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    # --- Character Count Section ---
    print("--------- Character Count -------")
    my_print(sorted_chars)

    print("============= END ===============")