import sys

def check_syntax(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            source = f.read()
        compile(source, file_path, "exec")
        print("No Syntax Errors Found")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except SyntaxError as e:
        print(f"Syntax Error at line {e.lineno}: {e.msg}")
        if e.text:
            print(e.text.rstrip())
            if e.offset:
                print(" " * (e.offset - 1) + "^")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        file_path = input("Enter Python file path: ").strip()
    else:
        file_path = sys.argv[1]
    check_syntax(file_path)
