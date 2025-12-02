# Function count words in a book

def word_count(words):
    array_words = words.split()
    count = len(array_words)
    return(count)



def character_count(words):
    lowercase_letters = words.lower()
    letters = {}
    for n in lowercase_letters:
        if n in letters:
            letters[n] += 1
        else:
            letters[n] = 1
    return(letters)

def sort_on(items):
    return items["num"]

def build_report(letters):
    letter_report = []
    for n in letters:
        a = {}
        a["char"] = n
        a["num"] = letters[n]
        letter_report.append(a)
    
    letter_report.sort(reverse=True, key=sort_on)
    return(letter_report)












# import string
# alphabet_dict_lowercase = {letter: index + 1 for index, letter in enumerate(string.ascii_lowercase)}
# alphabet_dict_lowercase = {letter: index + 1 for index, letter in enumerate(string.ascii_lowercase)}
# print("Lowercase alphabet dictionary:")
# print(alphabet_dict_lowercase)