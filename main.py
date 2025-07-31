import sys
from stats import get_num_words
from stats import get_num_chars
from stats import sort_dic

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    # book_text=get_book_text("./books/frankenstein.txt")
    # num_words = get_num_words(book_text) 
    # print(f"{num_words} words found in the document")
    # num_chars = get_num_chars(book_text)
    # print(f"{num_chars}")
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path= sys.argv[1]
    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {book_path}...\n")
    book_text= get_book_text(book_path)
    print("----------- Word Count ----------\n")
    print(f"Found {get_num_words(book_text)} total words\n")
    print("--------- Character Count -------\n")
    char_dic = get_num_chars(book_text)
    sorted_dic = sort_dic(char_dic)
    for c in sorted_dic:
        print(f"{c["name"]}: {c["num"]}\n")
    print("============= END ===============")



main()






