def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    count_letter = letter_count(text)
    count_word = no_of_words(text)
    report(path, count_word, count_letter)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def no_of_words(para):
    words = para.split()
    return len(words)

def letter_count(text):
    letter_count_dict = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char.isalpha():
            if char not in letter_count_dict:
                letter_count_dict[char] = 1
            else:
                letter_count_dict[char] += 1
    return letter_count_dict

def sort_on(dict):
    return dict["num"]

def report(path, count_words, count_letters):
    print(f"\n--Begin report of {path} --")
    print(f"{count_words} words found in the document\n")

    letter_list = []
    for letter in count_letters:
        temp_dict = {}
        temp_dict = {"letter": letter,"num": count_letters[letter]}
        letter_list.append(temp_dict)
    letter_list.sort(reverse = True, key = sort_on)
    
    for char in letter_list:
        print(f"The '{char["letter"]}' was found {char["num"]} times")
    print("--End report--")
    

main()