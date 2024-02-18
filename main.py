from sys import argv

class Book():
    def __init__(self, filename):
        self.file_text = ""
        self.filename = filename
        self.letters_dict = {}
        self.char_report_list = []

    def __raise_if_invalid_file(self, filename):
        if filename[-3:] != "txt":
            raise ValueError("only accepts txt files")

    def __get_char_num(self, dict):
        return dict["count"]
        
    def read_file(self):
        self.__raise_if_invalid_file(self.filename)

        with (open(self.filename) as f):
            self.file_text = f.read()

    def get_word_count(self):
        return len(self.file_text.split())

    def get_letter_count(self):
        self.read_file()
        char_list = self.file_text.lower()
        for c in char_list:
            if 96 < ord(c) < 122:
                char = self.letters_dict.get(c)
                if char is None:
                    self.letters_dict[c] = 1
                else:
                    self.letters_dict[c] += 1              
        return self.letters_dict

    def print_report(self):
        char_dict = self.get_letter_count()
        word_count = self.get_word_count()
        title = f"-- Processing file `{self.filename}` --"
        print(title)
        print('-' * len(title))

        for (key,value) in char_dict.items():
            items = {}
            items["key"] = key
            items["count"] = value
            self.char_report_list.append(items)
            self.char_report_list.sort(reverse=True, key=self.__get_char_num)

        print(f"{word_count} words found!\nHere is an analysis of the most used letters:")
        for letter in self.char_report_list:
            print(f"'{letter['key'].upper()}' was found {letter['count']} times")

def main():
    if len(argv) != 2:
        raise ValueError("expecting a file to read")
    book_file = argv[1]
    book = Book(book_file)
    book.print_report()
        
if __name__ == "__main__":
    main()