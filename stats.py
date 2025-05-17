def word_count(book_string):
    count = 0
    book_list = book_string.split()
    for book in book_list:
        count += 1
    return count

def count_characters(book_string):
    char_count_dict = {}
    for book_char in book_string:
        char = book_char.lower()
        if char not in char_count_dict:
            char_count_dict[char] = 1
        else:
            char_count_dict[char] += 1
    return char_count_dict

def sort_on(dict):
    return dict["num"]

def pretty_print_list(num_char_dict):
    num_char_list = []
    for key, value in num_char_dict.items():
        num_char_list.append({"char": key, "num": value})
    num_char_list.sort(reverse=True, key=sort_on)
    return num_char_list