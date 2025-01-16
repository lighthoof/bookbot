def readBook(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def countWords(text):
    words = text.split()
    return len(words)

def main():
    book_path = "books/frankenstein.txt"
    book_text = readBook(book_path)
    word_count = countWords(book_text)
    print(f"Counted {word_count} words in the book")

main()