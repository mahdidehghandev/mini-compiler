from lexer import Lexer


def read_file(entry):

    try:
        with open(entry, "r", encoding="utf-8") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{entry}' not found. Please check the file name and try again.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def main(file_name):
    text = read_file(file_name)
    
    lexer = Lexer(text)
    try:
        tokens = lexer.tokenize()
        for token in lexer.tokens:
            print(token)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main('input.txt')
