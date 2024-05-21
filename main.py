def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    first_499_characters = book_text[:499]
    print(f"{get_word_count(book_text)} words in the book.")

def get_book_text(path):
    with open(path) as file:
        return file.read()

def get_word_count(input_string):
    words_list = input_string.split()
    return len(words_list)

main()