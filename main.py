def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    book_word_count = get_word_count(book_text)
    char_dict = get_char_count(book_text)
    list_for_sort = create_dict_list(char_dict)
    list_for_sort.sort(reverse=True, key=sort_on)
    book_report(book_path, book_word_count, list_for_sort)

def get_book_text(path):
    with open(path) as file:
        return file.read()

def get_word_count(input_string):
    words_list = input_string.split()
    return len(words_list)

def get_char_count(input_string):
    char_count = {}
    for char in input_string:
        if not char.isalpha():
            continue
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def book_report(book_path="", word_count=0, char_list=[]):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for char in char_list:
        print(f"The '{char["char"]}' character was found {char["count"]} times")
    print(f"--- End report ---")

def sort_on(dict):
    return dict["count"]

def create_dict_list(dict):
    list_of_dicts = []
    for char in dict.keys():
        list_of_dicts.append({"char": char, "count": dict[char]})
    return list_of_dicts

main()