import sys
import os
from collections import defaultdict
from scanner import scan_directory

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze.py <folder_path>")
        return

    path = sys.argv[1]

    files = scan_directory(path)
    total_lines = sum(f["lines"] for f in files)

    print(f"Total files: {len(files)}")
    print(f"Total lines: {total_lines}")

    print("\nExtensions:")
    for f in files:
        ext = os.path.splitext(f["path"])[1]
        print(ext)

if __name__ == "__main__":
    main()