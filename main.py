from stats import get_num_words, character_distrib, sort_char_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main(filepath):
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    char_dict = character_distrib(text)
    sorted_dict = sort_char_dict(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in sorted_dict:
        if c["char"].isalpha():
            print(f"{c['char']}: {c['n']}")
    print("============= END ===============")

main('books/frankenstein.txt')