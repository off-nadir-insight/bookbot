def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    first_499_characters = book_text[:499]
    print(f"{get_word_count(book_text)} words in the book.")
    char_dict = get_char_count(book_text)
    print(f"p: {char_dict["p"]}")
    print(f"r: {char_dict["r"]}")
    print(f"o: {char_dict["o"]}")

def get_book_text(path):
    with open(path) as file:
        return file.read()

def get_word_count(input_string):
    words_list = input_string.split()
    return len(words_list)

def get_char_count(input_string):
    char_count = {}
    for char in input_string:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

main()