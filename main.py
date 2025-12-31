import sys
from stats import word_count, character_count, sorted_list_count_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_location = sys.argv[1]
    book_text = get_book_text(book_location)
    num_of_words = word_count(book_text)
    char_count = character_count(book_text)
    print("============= BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")
    print("----------- Word Count -----------")
    print(f"Found {num_of_words} total words")
    print("----------- Character Count -----------")
    sorted_list = sorted_list_count_dict(char_count)
    for i in sorted_list:
        if i['char'].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END =============")
    
    

main()