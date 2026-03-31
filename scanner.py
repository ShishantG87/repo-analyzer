import os

def scan_directory(path):
    files = []

    for root, dirs, filenames in os.walk(path):
        # skip hidden folders
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        for name in filenames:
            if name.startswith('.'):
                continue

            full_path = os.path.join(root, name)

            try:
                with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                    line_count = sum(1 for _ in f)
            except:
                line_count = 0

            files.append({
                "path": full_path,
                "lines": line_count
            })

    return files