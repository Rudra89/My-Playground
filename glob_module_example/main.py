import glob

file_paths = glob.glob("day11/files/*.txt")

for file_path in file_paths:
    with open(file_path, 'r') as file:
        print(file.read().upper())