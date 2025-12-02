# Program to read the contents of a file
import sys

from stats import word_count, character_count, build_report

print(len(sys.argv))
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

    
    



def main():
    path_to_file = sys.argv[1]
    words = get_book_text(path_to_file)
    num_words = word_count(words)
    letters = character_count(words)
    letter_report = build_report(letters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in letter_report:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        words = f.read()
        return(words)
    



main()




