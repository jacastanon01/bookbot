class Book():
    def __init__(self, filename):
        self.file_text = ""
        self.filename = filename
        self.letters_dict = {}

    def read_file(self):
        file_length = len(self.filename)
        if self.filename[-3:] != "txt":
            raise ValueError("only accepts txt files")

        with (open(self.filename) as f):
            self.file_text = f.read()

    def count_words(self):
        return len(self.file_text.split())

    def count_letters(self):
        self.read_file()
        lower_text = self.file_text.lower()
        for c in lower_text[:100]:
            if 96 < ord(c) < 122:
                letter = self.letters_dict.get(c)
                if letter is None:
                    self.letters_dict[c] = 1
                else:
                    self.letters_dict[c] += 1
                
        print(self.letters_dict)


def main():
    book = Book("../books/frankenstein.txt")
    book.count_letters()
    # print(book.count_words())
    # print(book.file_text[:100])
        
if __name__ == "__main__":
    main()