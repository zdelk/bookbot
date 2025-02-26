from stats import (
    word_count, 
    char_count, 
    sort_dict)

import sys


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
filepath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        
    return file_contents
    

def print_report(filepath, num_words, char_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_dict:
        print(f"{item["name"]}: {item["num"]}")
    print("============= END ===============")
    
    
def main(filepath):
    text = get_book_text(filepath)
    num_words = word_count(text)
    char_dict = sort_dict(char_count(text))
    print_report(filepath, num_words, char_dict)



main(filepath)