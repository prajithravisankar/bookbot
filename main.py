import sys
from stats import number_of_words_in_text, number_of_time_each_character_appears_in_text

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    bookpath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    text = get_book_text(bookpath)
    print(f"Found {number_of_words_in_text(text)} total words")
    print("--------- Character Count -------")
    char_count = number_of_time_each_character_appears_in_text(text)
    char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    for k, v in char_count:
        print(k + ": " + str(v))
    print("============= END ===============")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main()