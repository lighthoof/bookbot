#reading the book from provided path
def readBook(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

#counting the number of words in the book
def countWords(text):
    words = text.split()

    return len(words)

#counting characters in the book
def countCharacters(text):
    char_counts = {}
    lowered_text = text.lower()
    #looping over the string one char at a time
    for char in lowered_text:
        if char in char_counts:
            char_counts[char] += 1
        elif char not in char_counts:
            char_counts[char] = 1

    return char_counts

#formatting char counts into a readable report
def formatCharCounts(unformatted_char_counts):
    char_report = "Character counts :"
    #sort counted characters alphabetically
    sorted_char_list = sorted(unformatted_char_counts)
    #loop through sorte char sequence and append the counts to a report string
    for char in sorted_char_list:
        char_report += f"{char} : {unformatted_char_counts[char]}\n"

    return char_report    

def main():
    book_path = "books/frankenstein.txt"
    book_text = readBook(book_path)
    word_count = countWords(book_text)
    counted_characters = countCharacters(book_text)


    print(f"Counted {word_count} words in the book\n" + formatCharCounts(counted_characters))

main()