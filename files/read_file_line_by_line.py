
def write_text_file(file_path, file_contents):
    with open(file_path, "w") as f:
        f.write(file_contents)


# first, write to a text file
file_path = "text_file.txt"
file_contents = "Red\nBlue\nGreen\nPurple\n"

write_text_file(file_path, file_contents)

with open(file_path, "r") as f:
    while True:
        file_line = f.readline()
        if not file_line:
            break
        # file_line still contains the "\n"
        # we need to either: file_line.strip or file_line[:-1]
        print("%s" % file_line.strip())
