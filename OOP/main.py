from sys import argv
from book import Book

def main():
    if len(argv) != 2:
        raise ValueError("expecting a file to read")
    book_file = argv[1]
    book = Book(book_file)
    book.print_report()
        
if __name__ == "__main__":
    main()