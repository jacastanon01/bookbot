from sys import argv

class Book():
    def __init__(self, filename):
        self.file_text = ""
        self.filename = filename
        self.letters_dict = {}

    def __raise_if_invalid_file(filename):
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

def print_report(book):
    print('-- Processing franketstein --')
    print(book.filename)

def main():
    if len(argv) != 2:
        raise ValueError("expecting a file to read")
    book_file = argv[1]
    book = Book(book_file)
    print_report(book)
        
if __name__ == "__main__":
    main()