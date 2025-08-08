files = ["file1.txt", "file2.txt", "file3.txt"]

for file in files:
    curr_file= open(f"day4/bonus/files/{file}", "r")
    print(curr_file.read())
    curr_file.close()