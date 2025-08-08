files = ["1.one", "1.two", "1.three"]

new_files = [file.replace('.', ') ') + '.txt' for file in files]
print(new_files)