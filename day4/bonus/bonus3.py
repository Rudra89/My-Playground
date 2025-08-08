filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open(f"day4/bonus/files/bonus3/{filename}", "w")
    file.writelines("Hello")
    file.close()