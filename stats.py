def word_count(book_text):
    words = book_text.split()
    return len(words)

def character_count(book_text):
    char = {}
    for t in book_text.lower():
        if t in char:
            char[t] += 1
        else:
            char[t] = 1
    return char

def sorted_list_count_dict(char_count):
    sorted_list = []
    for k,v in char_count.items():
        sorted_list.append({"char": k, "num": v})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(items):
    return items["num"]