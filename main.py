from sys import argv

class Book():
    def __init__(self, filename):
        self.file_text = ""
        self.filename = filename
        self.letters_dict = {}

    def __raise_if_invalid_file(self, filename):
        if filename[-3:] != "txt":
            raise ValueError("only accepts txt files")

    def read_file(self):
        self.__raise_if_invalid_file(self.filename)

        with (open(self.filename) as f):
            self.file_text = f.read()

    def get_word_count(self):
        return len(self.file_text.split())

    def get_letter_count(self):
        self.read_file()
        char = self.file_text.lower()
        for c in char[:100]:
            if 96 < ord(c) < 122:
                letter = self.letters_dict.get(c)
                if letter is None:
                    self.letters_dict[c] = 1
                else:
                    self.letters_dict[c] += 1              
        return self.letters_dict

def get_char_num(dict):
    return dict["count"]

def print_report(book):
    char_dict = book.get_letter_count()
    char_report_list = []
    word_count = book.get_word_count()
    title = f"-- Processing file `{book.filename}` --"
    print(title)
    # print ('-' for i in range(len(title)))

    for (key,value) in char_dict.items():
        items = {}
        items["key"] = key
        items["count"] = value
        char_report_list.append(items)
        char_report_list.sort(reverse=True, key=get_char_num)

    # print(f"{word_count} words found!\nHere is an analysis of the most used letters:")


    for letter in char_report_list:
        print(f"'{letter['key'].upper()}' was found {letter['count']} times")


def main():
    if len(argv) != 2:
        raise ValueError("expecting a file to read")
    book_file = argv[1]
    book = Book(book_file)
    print_report(book)
        
if __name__ == "__main__":
    main()