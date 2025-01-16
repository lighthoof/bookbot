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
        if char in char_counts and char.isalpha():
            char_counts[char] += 1
        elif char not in char_counts and char.isalpha():
            char_counts[char] = 1

    return char_counts

#sorting char counts alphabetically
def sortedCharCountsAlph(unformatted_char_counts):
    char_counts = {}
    #sort counted characters alphabetically
    sorted_char_list = sorted(unformatted_char_counts)
    #loop through sorte char sequence and append the counts to a report string
    for char in sorted_char_list:
        char_counts[char] = unformatted_char_counts[char]

    return char_counts    

def sortedCharCountsNum(unformatted_char_counts): 
    #function to return value of "num" to use in sort
    def sort_on(dict):
        return dict["num"]
    
    char_counts = {}
    list_of_char_counts = []

    #convert input dictionary into a list of dictionaries for sorting
    for char in unformatted_char_counts:
        char_count_dict = {}
        char_count_dict["name"] = char
        char_count_dict["num"] = unformatted_char_counts[char]
        list_of_char_counts.append(char_count_dict)
    
    #sort the list of dictionaries
    list_of_char_counts.sort(reverse=True, key=sort_on)
    
    #convert list of dictionaries back to a dictionary
    for dict in list_of_char_counts:
        char_counts[dict["name"]] = dict["num"]

    return char_counts

def formatReport(word_count,char_count):

    return

def main():
    book_path = "books/frankenstein.txt"
    book_text = readBook(book_path)
    word_count = countWords(book_text)
    counted_characters = countCharacters(book_text)

    #print(sortedCharCountsAlph(counted_characters))
    sortedCharCountsNum(counted_characters)
    #print(f"Counted {word_count} words in the book\n" + formatCharCounts(counted_characters))

main()