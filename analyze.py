import sys
from scanner import scan_directory

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze.py <folder_path>")
        return

    path = sys.argv[1]

    files = scan_directory(path)

    print(f"Total files: {len(files)}")

if __name__ == "__main__":
    main()