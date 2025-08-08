contents = ["Content of file 1", "Content of file 2", "Content of file 3"]

filenames = ["file1.txt", "file2.txt", "file3.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"day4/bonus/files/{filename}", "w")
    file.write(content)
    file.close()

print("Content added to files!")