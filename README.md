BookBot CLI Analyzer
BookBot is a command-line utility built in Python that analyzes the text from any provided book file to calculate foundational metrics and report the most frequent characters.

This project was developed as the core programming assignment for the fundamentals section of the Boot.dev curriculum.

📊 Features
This tool performs the following tasks on the provided book text:

File Input: Reads the entire contents of a book file using command-line arguments (sys.argv) and safe I/O practices (with open(...)).

Word Count: Calculates the total number of words in the text.

Character Frequency: Counts the occurrences of every alphabetical character, ignoring case and filtering out symbols and spaces for the final report.

Data Sorting: Sorts the final character counts from highest frequency to lowest using the Python list.sort() method with a custom key function.

Clean Reporting: Prints a fully structured and formatted analysis report to the console.

🚀 Usage
To run the BookBot analysis tool, execute the script from your project root (/bookbot) and pass the relative path to the book file as the first command-line argument.

Requirements
Python 3.8+

The target book file must be present (e.g., in the books/ directory).

Execution
# Example 1: Analyze Frankenstein
python3 main.py books/frankenstein.txt

# Example 2: Analyze Moby Dick
python3 main.py books/mobydick.txt


Argument Error Handling
If no file path is provided, the tool will exit with an error status and print the usage instructions:

$ python3 main.py
Usage: python3 main.py <path_to_book>
