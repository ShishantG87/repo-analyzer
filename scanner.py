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
            files.append(full_path)

    return files