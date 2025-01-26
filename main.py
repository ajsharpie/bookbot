def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = count_characters(text)
    sorted_count = sort_count(char_count)   
    print_report(word_count, sorted_count)

    
def get_book_text(path):
    with open(path) as f:
        return f.read()  
       
          
def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    string = text.lower()
    character_counts = {}
    for char in string:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts


def sort_on(dict):
    return dict["value"]


def sort_count(dict):
    list_of_chars = []
    for key in dict:
        new_dict = {"char": key, "value": dict[key]}
        list_of_chars.append(new_dict)
    list_of_chars.sort(reverse=True, key=sort_on)
    return list_of_chars


def print_report(words, chars):
    print(f"--- Book Report ---")
    print(f"This book contains {words}")
    for i in chars:
        char = i["char"]
        if char.isalpha() == True:
            value = i["value"]
            print(f"The character '{char}' was found {value} times") 
    print("--- End of Report ---")
    

main()     