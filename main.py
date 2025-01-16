def readBook(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    print(readBook("books/frankenstein.txt"))

main()