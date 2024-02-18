from sys import argv

def raise_if_invalid_file(filename):
    if filename[-3:] != "txt":
        raise ValueError("only accepts txt files")

def get_char_num(dict):
    return dict["count"]
        
def read_file(filename):
    raise_if_invalid_file(filename)
    with (open(filename) as f):
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_letter_count(text):
    letters_dict = {}
    char_list = text.lower()

    for c in char_list:
        if 96 < ord(c) < 122:
            char = letters_dict.get(c)
            if char is None:
                letters_dict[c] = 1
            else:
                letters_dict[c] += 1              
    return letters_dict

def print_report(filename):
    file_text = read_file(filename)
    char_dict = get_letter_count(file_text)
    word_count = get_word_count(file_text)
    char_report_list = []

    title = f"-- Processing file `{filename}` --"
    print(title)
    print('-' * len(title))

    for (key,value) in char_dict.items():
        items = {}
        items["key"] = key
        items["count"] = value
        char_report_list.append(items)
        char_report_list.sort(reverse=True, key=get_char_num)

    print(f"{word_count} words found!\nHere is an analysis of the most used letters:")
    for letter in char_report_list:
        print(f"'{letter['key'].upper()}' was found {letter['count']} times")

def main():
    if len(argv) != 2:
        raise ValueError("expecting a file to read")
    book_file = argv[1]
    print_report(book_file)
        
if __name__ == "__main__":
    main()