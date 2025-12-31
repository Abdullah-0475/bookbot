from stats import word_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    print(book_text)
    num_of_words = word_count(book_text)
    print(f"Found {num_of_words} total words")

main()