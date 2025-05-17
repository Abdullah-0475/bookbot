import sys
from stats import word_count, count_characters, pretty_print_list

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {path}...')
    
    print("---------- Word Count ----------")
    book = get_book_text(path)
    num_words = word_count(book)
    print(f'Found {num_words} total words')
    
    print("---------- Character Count ----------")
    num_chars = count_characters(book)
    num_chars_list = pretty_print_list(num_chars)
    for char in num_chars_list:
        if char["char"].isalpha():
            print(f'{char["char"]}: {char["num"]}')
    print("============ END ============")

main()
    
    