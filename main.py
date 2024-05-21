def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    first_499_characters = book_text[:499]
    print(first_499_characters)

def get_book_text(path):
    with open(path) as file:
        return file.read()

main()