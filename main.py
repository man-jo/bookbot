import sys
from stats import get_character_dict, get_num_words, sort_char_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]

    text = get_book_text(filepath)
    num_words = get_num_words(text)
    char_dict = get_character_dict(text)
    sorted_dict = sort_char_dict(char_dict)

    print_report(filepath, num_words, sorted_dict)

def print_report(filepath, num_words, sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in sorted_dict:
        if c["char"].isalpha():
            print(f"{c['char']}: {c['n']}")
    print("============= END ===============")

main()