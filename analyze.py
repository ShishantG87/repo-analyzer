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

    languages = defaultdict(int)

    for f in files:
        ext = os.path.splitext(f["path"])[1].lower()

        if ext:
            languages[ext] += 1
        else:
            languages["no_ext"] += 1

    print("\nLanguages:")
    for lang, count in languages.items():
        print(f"  {lang}: {count}")

    # SMALL STEP: just sort first
    largest_files = sorted(files, key=lambda x: x["lines"], reverse=True)

    print("\nLargest file:")
    if largest_files:
        f = largest_files[0]
        print(f"  {f['path']} ({f['lines']} lines)")

if __name__ == "__main__":
    main()